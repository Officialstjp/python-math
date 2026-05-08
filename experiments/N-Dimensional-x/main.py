from __future__ import annotations

import argparse
import copy
import tomllib
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

from cube_geometry import (
    SampledGeometry,
    make_hypercube,
    orthonormalize_basis,
    project_onto_basis,
    rotate_in_plane,
)


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_CONFIG_PATH = SCRIPT_DIR / "configs" / "rotating_hypercube.toml"

DEFAULT_CONFIG: dict[str, Any] = {
    "geometry": {
        "dimension": 4,
        "half_extent": 1.0,
    },
    "rotation": {
        "axis_a": 0,
        "axis_b": 3,
        "start_angle": 0.0,
        "end_angle": 2.0 * np.pi,
    },
    "projection": {
        "target_dimension": 3,
        "hidden_axis": 3,
        "orthonormalize_basis": True,
        "basis": [
            [1.0, 0.0, 0.0, 0.45],
            [0.0, 1.0, 0.0, 0.35],
            [0.0, 0.0, 1.0, 0.75],
        ],
    },
    "animation": {
        "frames": 180,
        "interval_ms": 40,
        "repeat": True,
    },
    "plot": {
        "axis_limit": 1.9,
        "point_size": 72,
        "edge_linewidth": 1.5,
        "edge_alpha": 0.78,
        "color_map": "viridis",
        "figure_width": 9.0,
        "figure_height": 7.0,
        "view_elevation": 22,
        "view_azimuth": 35,
    },
}


def deep_merge(base: dict[str, Any], overrides: dict[str, Any]) -> dict[str, Any]:
    """
    Merge nested configuration dictionaries without mutating either input.
    """
    merged = copy.deepcopy(base)

    for key, value in overrides.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = copy.deepcopy(value)

    return merged


def load_config(config_path: Path) -> dict[str, Any]:
    """
    Load a TOML config and apply it on top of readable defaults.
    """
    if not config_path.is_file():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, "rb") as config_file:
        loaded_config = tomllib.load(config_file)

    return deep_merge(DEFAULT_CONFIG, loaded_config)


def axis_name(axis_index: int) -> str:
    """
    Human-readable axis names for titles and labels.
    """
    known_names = ["x", "y", "z", "w"]

    if axis_index < len(known_names):
        return known_names[axis_index]

    return f"axis {axis_index}"


def build_projection_basis(config: dict[str, Any], source_dimension: int) -> np.ndarray:
    """
    Read the 4D-to-3D projection basis from config and validate its shape.
    """
    projection_config = config["projection"]
    target_dimension = int(projection_config["target_dimension"])
    basis = np.asarray(projection_config["basis"], dtype=float)

    expected_shape = (target_dimension, source_dimension)

    if basis.shape != expected_shape:
        raise ValueError(
            f"Projection basis must have shape {expected_shape}, but got {basis.shape}"
        )

    if target_dimension != 3:
        raise ValueError("This first animation target expects a 3D projection basis")

    if bool(projection_config["orthonormalize_basis"]):
        basis = orthonormalize_basis(basis)

    return basis


def build_angles(config: dict[str, Any]) -> np.ndarray:
    """
    Build the animation angle sequence from config.
    """
    rotation_config = config["rotation"]
    frame_count = int(config["animation"]["frames"])

    if frame_count < 2:
        raise ValueError("animation.frames must be at least 2")

    return np.linspace(
        float(rotation_config["start_angle"]),
        float(rotation_config["end_angle"]),
        frame_count,
        endpoint=False,
    )


def project_frame(
    geometry: SampledGeometry,
    basis: np.ndarray,
    axis_a: int,
    axis_b: int,
    hidden_axis: int,
    angle_radians: float,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Rotate the 4D geometry and project it into 3D for one animation frame.

    Returns:
        projected_points: shape (n_points, 3)
        hidden_values: current coordinate values on the hidden axis
    """
    rotated_points = rotate_in_plane(
        geometry.points,
        axis_a=axis_a,
        axis_b=axis_b,
        angle_radians=angle_radians,
    )
    projected_points = project_onto_basis(
        rotated_points,
        basis,
        orthonormalize=False,
    )
    hidden_values = rotated_points[:, hidden_axis]

    return projected_points, hidden_values


def compute_plot_ranges(
    geometry: SampledGeometry,
    basis: np.ndarray,
    config: dict[str, Any],
    angles: np.ndarray,
) -> tuple[float, float]:
    """
    Estimate stable visible and color ranges across the full animation.
    """
    rotation_config = config["rotation"]
    projection_config = config["projection"]

    max_projected_coordinate = 0.0
    max_hidden_coordinate = 0.0

    for angle_radians in angles:
        projected_points, hidden_values = project_frame(
            geometry,
            basis,
            axis_a=int(rotation_config["axis_a"]),
            axis_b=int(rotation_config["axis_b"]),
            hidden_axis=int(projection_config["hidden_axis"]),
            angle_radians=float(angle_radians),
        )
        max_projected_coordinate = max(
            max_projected_coordinate,
            float(np.max(np.abs(projected_points))),
        )
        max_hidden_coordinate = max(
            max_hidden_coordinate,
            float(np.max(np.abs(hidden_values))),
        )

    configured_axis_limit = float(config["plot"]["axis_limit"])
    axis_limit = max(configured_axis_limit, max_projected_coordinate * 1.08)
    hidden_limit = max(max_hidden_coordinate, 1e-8)

    return axis_limit, hidden_limit


def configure_3d_axis(axis_3d: Any, axis_limit: float, config: dict[str, Any]) -> None:
    """
    Apply stable axis limits and view settings to the 3D plot.
    """
    axis_3d.set_xlim(-axis_limit, axis_limit)
    axis_3d.set_ylim(-axis_limit, axis_limit)
    axis_3d.set_zlim(-axis_limit, axis_limit)
    axis_3d.set_xlabel("projected axis 1")
    axis_3d.set_ylabel("projected axis 2")
    axis_3d.set_zlabel("projected axis 3")
    axis_3d.set_box_aspect((1, 1, 1))
    axis_3d.grid(True)
    axis_3d.view_init(
        elev=float(config["plot"]["view_elevation"]),
        azim=float(config["plot"]["view_azimuth"]),
    )


def draw_frame(
    axis_3d: Any,
    geometry: SampledGeometry,
    projected_points: np.ndarray,
    hidden_values: np.ndarray,
    angle_radians: float,
    axis_limit: float,
    color_norm: Normalize,
    color_map: Any,
    config: dict[str, Any],
) -> None:
    """
    Draw one animation frame.

    For clarity, the whole axis is redrawn each frame. That is perfectly fine
    for 16 vertices and 32 edges, and it keeps the animation logic readable.
    """
    axis_3d.clear()
    configure_3d_axis(axis_3d, axis_limit, config)

    plot_config = config["plot"]

    for start_index, end_index in geometry.edges or []:
        edge_hidden_value = 0.5 * (hidden_values[start_index] + hidden_values[end_index])
        edge_color = color_map(color_norm(edge_hidden_value))

        axis_3d.plot(
            [projected_points[start_index, 0], projected_points[end_index, 0]],
            [projected_points[start_index, 1], projected_points[end_index, 1]],
            [projected_points[start_index, 2], projected_points[end_index, 2]],
            color=edge_color,
            linewidth=float(plot_config["edge_linewidth"]),
            alpha=float(plot_config["edge_alpha"]),
        )

    axis_3d.scatter(
        projected_points[:, 0],
        projected_points[:, 1],
        projected_points[:, 2],
        c=hidden_values,
        cmap=color_map,
        norm=color_norm,
        s=float(plot_config["point_size"]),
        edgecolors="black",
        linewidths=0.5,
    )

    rotation_config = config["rotation"]
    axis_a = axis_name(int(rotation_config["axis_a"]))
    axis_b = axis_name(int(rotation_config["axis_b"]))
    hidden_axis = axis_name(int(config["projection"]["hidden_axis"]))
    degrees = np.degrees(angle_radians)

    axis_3d.set_title(
        f"4D hypercube rotating in the {axis_a}-{axis_b} plane\n"
        f"projected into 3D, colored by current {hidden_axis} ({degrees:5.1f} deg)"
    )


def build_animation(config: dict[str, Any]) -> FuncAnimation:
    """
    Create the rotating 4D hypercube animation.
    """
    geometry_config = config["geometry"]
    rotation_config = config["rotation"]
    projection_config = config["projection"]
    plot_config = config["plot"]

    hypercube = make_hypercube(
        dimension=int(geometry_config["dimension"]),
        half_extent=float(geometry_config["half_extent"]),
    )
    basis = build_projection_basis(config, source_dimension=hypercube.dimension)
    angles = build_angles(config)
    axis_limit, hidden_limit = compute_plot_ranges(hypercube, basis, config, angles)

    figure = plt.figure(
        figsize=(float(plot_config["figure_width"]), float(plot_config["figure_height"])),
    )
    axis_3d = figure.add_subplot(111, projection="3d")

    color_norm = Normalize(vmin=-hidden_limit, vmax=hidden_limit)
    color_map = plt.get_cmap(str(plot_config["color_map"]))
    scalar_mappable = ScalarMappable(norm=color_norm, cmap=color_map)
    scalar_mappable.set_array([])

    colorbar = figure.colorbar(scalar_mappable, ax=axis_3d, shrink=0.72, pad=0.1)
    colorbar.set_label(f"current {axis_name(int(projection_config['hidden_axis']))} coordinate")

    def update_frame(frame_index: int) -> list[Any]:
        angle_radians = float(angles[frame_index])
        projected_points, hidden_values = project_frame(
            hypercube,
            basis,
            axis_a=int(rotation_config["axis_a"]),
            axis_b=int(rotation_config["axis_b"]),
            hidden_axis=int(projection_config["hidden_axis"]),
            angle_radians=angle_radians,
        )
        draw_frame(
            axis_3d,
            hypercube,
            projected_points,
            hidden_values,
            angle_radians,
            axis_limit,
            color_norm,
            color_map,
            config,
        )
        return []

    return FuncAnimation(
        figure,
        update_frame,
        frames=len(angles),
        interval=int(config["animation"]["interval_ms"]),
        repeat=bool(config["animation"]["repeat"]),
    )


def print_dry_run_summary(config: dict[str, Any]) -> None:
    """
    Print a quick non-visual check of the configured geometry pipeline.
    """
    geometry_config = config["geometry"]
    rotation_config = config["rotation"]
    projection_config = config["projection"]

    hypercube = make_hypercube(
        dimension=int(geometry_config["dimension"]),
        half_extent=float(geometry_config["half_extent"]),
    )
    basis = build_projection_basis(config, source_dimension=hypercube.dimension)
    first_angle = float(rotation_config["start_angle"])
    projected_points, hidden_values = project_frame(
        hypercube,
        basis,
        axis_a=int(rotation_config["axis_a"]),
        axis_b=int(rotation_config["axis_b"]),
        hidden_axis=int(projection_config["hidden_axis"]),
        angle_radians=first_angle,
    )

    print("Rotating 4D hypercube dry run")
    print(f"  Source dimension: {hypercube.dimension}")
    print(f"  Vertex count: {hypercube.point_count}")
    print(f"  Edge count: {hypercube.edge_count}")
    print(f"  Projection basis shape: {basis.shape}")
    print(f"  Projected point shape: {projected_points.shape}")
    print(
        "  Hidden coordinate range in first frame: "
        f"{hidden_values.min():.3f} to {hidden_values.max():.3f}"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Animate a rotating 4D hypercube projected into 3D.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to the TOML configuration file.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate the configured pipeline without opening a plot window.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config_path = args.config if args.config.is_absolute() else SCRIPT_DIR / args.config
    config = load_config(config_path)

    if args.dry_run:
        print_dry_run_summary(config)
        return 0

    animation = build_animation(config)
    plt.show()

    # Keep the animation object alive until the plot window is closed.
    _ = animation
    return 0


if __name__ == "__main__":
    raise SystemExit(main())