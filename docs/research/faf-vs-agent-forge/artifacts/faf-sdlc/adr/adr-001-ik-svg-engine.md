# ADR-001: Hybrid Canvas 2D Vector Renderer with Analytical 2-Bone IK Closure

- **Status**: Accepted (`FAF-architect`)
- **Context**: We need 60 FPS smooth biomechanical pedaling, dynamic gular pouch physics, road parallax, and an engineering X-Ray vector overlay inside a single zero-dependency file publishable on GitHub Pages.
- **Decision**: Use a high-DPI (`devicePixelRatio`) HTML5 Canvas 2D vector pipeline backed by a deterministic `AnalyticalTwoBoneIKSolver` module and critically damped spring integrators.
- **Consequences**: Guarantees 0.0 px foot-to-pedal detachment error, sub-2ms frame render time, and immediate X-Ray vector inspection.
