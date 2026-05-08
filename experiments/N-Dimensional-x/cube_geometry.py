from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Iterable

import numpy as np


ArrayLike = Iterable[float] | np.ndarray


@dataclass
class SampledGeometry:
    """
    A geometry defined by a set of points, edges and lables for them.

    points:
        Array of shape (n_points, dimensions).

    edges:
        Optional list of index pairs into points.
        Can be used to define wireframes or other connections between points.

    labels:
        Optional list of labels for the points, edges or faces.
    """

    points: np.ndarray
    edges: list[tuple[int, int]] | None = None
    labels: list[str] | None = None

    @property
    def point_count(self) -> int:
        return len(self.points)

    @property
    def edge_count(self) -> int | None:
        return len(self.edges) if self.edges is not None else None

    @property
    def dimension(self) -> int:
        if self.points.ndim != 2:
            raise ValueError("points must be a 2D array of shape (n_points, dimension)")
        return self.points.shape[1]

    def copy(self) -> "SampledGeometry":
        return SampledGeometry(
            points=self.points.copy(),
            edges=None if self.edges is None else list(self.edges),
            labels=None if self.labels is None else list(self.labels),
        )


def as_point(values: ArrayLike) -> np.ndarray:
    """
    Convert a 1D point-like input into a float numpy array.
    """

    point = np.asarray(list(values) if not isinstance(values, np.ndarray) else values, dtype=float)

    if point.ndim != 1:
        raise ValueError("A point must be one-dimensional")

    return point

def as_points(values: ArrayLike | Iterable[ArrayLike]) -> np.ndarray:
    """
    Convert a collection of points into a 2D float array.

    Returns an ndarray of shape (n_points, dimension)
    """
    points = np.asarray(values, dtype=float)

    if points.ndim != 2:
        raise ValueError("Points must have shape (n_points, dimension)")

    return points

def validate_same_dimension(points: np.ndarray, expected_dimension: int) -> None:
    """
    Ensure the given point array lives in the expected dimension.
    """
    if points.shape[1] != expected_dimension:
        raise ValueError(
            f"Expected points in dimension {expected_dimension}"
            f"but got dimension {points.shape[1]}"
        )


def normalize_vector(vector: ArrayLike) -> np.ndarray:
    """
    Return a unit-length copy of a vector.

    Projection bases are easiest to reason about when their direction vectors
    have length 1. This helper keeps that normalization step explicit.
    """
    vector = as_point(vector)
    length = np.linalg.norm(vector)

    if length == 0:
        raise ValueError("Cannot normalize the zero vector")

    return vector / length


def orthonormalize_basis(basis: np.ndarray, tolerance: float = 1e-10) -> np.ndarray:
    """
    Turn a list of basis vectors into an orthonormal basis with Gram-Schmidt.

    The input is interpreted row-wise:
        basis[0] is the first view direction,
        basis[1] is the second view direction,
        and so on.

    This is useful for visualization configs. We can write intuitive view
    directions by hand and let the code remove overlap between them.
    """
    basis = np.asarray(basis, dtype=float)

    if basis.ndim != 2:
        raise ValueError("basis must have shape (target_dimension, source_dimension)")

    orthonormal_vectors: list[np.ndarray] = []

    for vector in basis:
        candidate = vector.copy()

        for previous_vector in orthonormal_vectors:
            projection_length = np.dot(candidate, previous_vector)
            candidate = candidate - projection_length * previous_vector

        candidate_length = np.linalg.norm(candidate)

        if candidate_length <= tolerance:
            raise ValueError(
                "Projection basis contains dependent directions; "
                "choose directions that span the target view space"
            )

        orthonormal_vectors.append(candidate / candidate_length)

    return np.asarray(orthonormal_vectors, dtype=float)

def apply_linear_map(points: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    """
    Apply a linear transformation to every point.
    """
    points = as_points(points)
    matrix = np.asarray(matrix, dtype=float)

    if matrix.ndim != 2:
        raise ValueError("matrix must be 2-dimensional")

    input_dimension = points.shape[1]

    if matrix.shape != (input_dimension, input_dimension):
        raise ValueError(
            f"matrix must have shape ({input_dimension}, {input_dimension}), "
            f"but got {matrix.shape}"
        )

    return (matrix @ points.T).T


def rotation_matrix(
    dimension: int,
    axis_a: int,
    axis_b: int,
    angle_radians: float,
) -> np.ndarray:
    """
    Build an N-dimensional rotation matrix for one coordinate plane.

    In 2D, there is only one rotation plane: x-y.
    In 4D, there are six coordinate planes: x-y, x-z, x-w, y-z, y-w, z-w.

    Rotating in the x-w plane is especially useful here because it makes the
    fourth coordinate move into and out of the visible projection.
    """
    if dimension < 2:
        raise ValueError("dimension must be at least 2")

    if axis_a == axis_b:
        raise ValueError("axis_a and axis_b must be different")

    for axis in (axis_a, axis_b):
        if axis < 0 or axis >= dimension:
            raise ValueError(f"Axis {axis} is out of range for dimension {dimension}")

    cosine = np.cos(angle_radians)
    sine = np.sin(angle_radians)

    matrix = np.eye(dimension)
    matrix[axis_a, axis_a] = cosine
    matrix[axis_b, axis_b] = cosine
    matrix[axis_a, axis_b] = -sine
    matrix[axis_b, axis_a] = sine

    return matrix


def rotate_in_plane(
    points: np.ndarray,
    axis_a: int,
    axis_b: int,
    angle_radians: float,
) -> np.ndarray:
    """
    Rotate points in the coordinate plane spanned by two axes.
    """
    points = as_points(points)
    matrix = rotation_matrix(
        dimension=points.shape[1],
        axis_a=axis_a,
        axis_b=axis_b,
        angle_radians=angle_radians,
    )

    return apply_linear_map(points, matrix)

def translate(points: np.ndarray, offset: ArrayLike) -> np.ndarray:
    """
    Translate very point by the same offset vector.
    """
    points = as_points(points)
    offset = as_point(offset)

    validate_same_dimension(points, len(offset))
    return points + offset


def project_orthographic(points: np.ndarray, keep_axes: list[int]) -> np.ndarray:
    """
    Orthographically porject points from R^n into a lower-dimensional
    coordinate subspace

    Example:
        keep_axes = [0, 1] gives an R^n -> R^2 projection
        keep_axes = [0, 2, 4] gives an R^n -> R^3 projection
    """
    points = as_points(points)

    if not keep_axes:
        raise ValueError("keep_axes is required")

    dimension = points.shape[1]

    for axis in keep_axes:
        if axis < 0 or axis >= dimension:
            raise ValueError(f"Axis {axis} is out of range for dimension {dimension}")

    return points[:, keep_axes]


def project_onto_basis(
    points: np.ndarray,
    basis: np.ndarray,
    *,
    orthonormalize: bool = True,
) -> np.ndarray:
    """
    Project N-dimensional points onto a lower-dimensional view basis.

    points shape:
        (n_points, source_dimension)

    basis shape:
        (target_dimension, source_dimension)

    result shape:
        (n_points, target_dimension)

    Unlike project_orthographic, this does not merely drop hidden coordinates.
    Every basis vector can include a fourth-coordinate component, so the hidden
    direction can visibly affect the projected 3D result.
    """
    points = as_points(points)
    basis = np.asarray(basis, dtype=float)

    if basis.ndim != 2:
        raise ValueError("basis must have shape (target_dimension, source_dimension)")

    source_dimension = points.shape[1]

    if basis.shape[1] != source_dimension:
        raise ValueError(
            f"Basis vectors must live in dimension {source_dimension}, "
            f"but got dimension {basis.shape[1]}"
        )

    if orthonormalize:
        basis = orthonormalize_basis(basis)

    return points @ basis.T

def slice_by_coordinate(
    points: np.ndarray,
    axis: int,
    value: float,
    tolerance: float = 1e-8,
) -> np.ndarray:
    """
    Keep only the points whose coordinate on one axis is close to a chosen value.

    This is a very simple discrete slice, not true geometric intersection.
    """
    points = as_points(points)
    dimension = points.shape[1]

    if axis < 0 or axis >= dimension:
        raise ValueError(f"Axis {axis} is out of range for dimension {dimension}")

    mask = np.abs(points[:, axis] - value) <= tolerance
    return points[mask]

def build_geometry(points: ArrayLike | Iterable[ArrayLike], edges: list[tuple[int, int]] | None = None) -> SampledGeometry:
    """
    Convenience constructor for SampledGeometry.
    """
    return SampledGeometry(points=as_points(points), edges=edges)

def hypercube_vertices(dimension: int, half_extent: float = 1.0) -> np.ndarray:
    """
    Generate all vertices of an n-dimensional hypercube centered at the origin.

    For dimension = n, there are 2^n vertices.

    With half_extent = 1.0, the coordinates are all combinations of -1 and +1
    """
    if dimension < 1:
        raise ValueError("dimension must be at least 1")

    coordinates = [-half_extent, half_extent]
    vertices = list(product(coordinates, repeat=dimension))
    return np.asarray(vertices, dtype=float)

def hypercube_edges(dimension: int) -> list[tuple[int, int]]:
    """
    Generate edge connectivity for an n-dimensional hypercube.

    Two vertices are connected if they differ in exactly on coordinate.
    """
    vertices = hypercube_vertices(dimension)
    edge_list: list[tuple[int, int]] = []

    for index_a, vertex_a in enumerate(vertices):
        for index_b in range(index_a + 1, len(vertices)):
            vertex_b = vertices[index_b]

            differance_count = np.count_nonzero(vertex_a != vertex_b)

            if differance_count == 1:
                edge_list.append((index_a, index_b))

    return edge_list

def make_hypercube(dimension: int, half_extent: float = 1.0) -> SampledGeometry:
    """
    Cerate a hypercube as sampled geometry.
    """
    points = hypercube_vertices(dimension=dimension, half_extent=half_extent)
    edges = hypercube_edges(dimension=dimension)
    return SampledGeometry(points=points, edges=edges)


