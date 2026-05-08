# N-Dimensional-x

This expiriment focusses on understanding and visualizing the behavior of geometric shapes in N-dimensional spaces.
We strive to explore the geometric properties of these shapes, gain insights and maybe connect them to other mathematical concepts or real-world applications - by discovery.

## Architecture

I define an "architecture" - be it a simple one - as this very much still is a software project.
The core challange is not to implement the mathematical concepts (which is comparatively easy), but to design a software architecture that allows for easy and variable experimentation, while also being efficient and maintainable.
Strict pipelines: Parameterization and Initialization -> Transformation and Projection -> Visualization and Analysis.

We use Python for mathematical exploration, numerical experiments, and reference implementations.

Later, when the mathematical pipeline is stable, an interactive frontend can be added:

- Svelte + TypeScript for UI and interaction.
- A browser renderer based on WebGL or WebGPU for high-performance visualization.

The important constraint is architectural rather than technological: the mathematical core should stay renderer-agnostic. The same sampled objects, projections, and slices should be usable from a notebook, a script, or a future interactive frontend.

## Design Direction

The project should be organized around a strict geometry pipeline:

1. Define an object in N dimensions.
2. Sample or parameterize it.
3. Apply transformations.
4. Slice it or project it into a viewable space.
5. Render or analyze the resulting representation.

That means the core outputs should be simple, reusable data forms such as:

- point clouds
- polylines
- meshes where applicable
- scalar fields or metadata for coloring and analysis

## Current Target: Rotating 4D Hypercube

The first intuitive visualization target is:

> A rotating 4D hypercube projected into 3D, where the fourth coordinate visibly affects the shape.

Run from this folder:

```powershell
python .\main.py
```

For a quick test without rendering:

```powershell
python .\main.py --dry-run
```

The demo is configured through:

```text
configs/rotating_hypercube.toml
```

Important parameters:

- `rotation.axis_a` and `rotation.axis_b` choose the 4D rotation plane.
- `projection.basis` chooses the 4D-to-3D viewing directions.
- nonzero `w` components in `projection.basis` make the fourth coordinate visible instead of being discarded.
- `projection.hidden_axis` controls which coordinate is used for color.
- `animation.frames` and `animation.interval_ms` control motion smoothness and speed.


