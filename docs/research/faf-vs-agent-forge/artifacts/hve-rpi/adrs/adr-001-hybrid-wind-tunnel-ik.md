# ADR-001: Hybrid Canvas2D Wind-Tunnel + Analytical 2-Bone SVG Rig for Pelican Tour Pro

* **Status**: Accepted (`2026-10-24`)
* **Authoring Skill**: `adr-author` (`microsoft/hve-core@3.3.101`, MADR v4.0.0 + Y-Statement)
* **Y-Statement**: In the context of **real-time multi-terrain avian cycling simulation (`demo-hve-pelican.html`)**, facing **60FPS wind-tunnel fluid streamline rendering alongside zero-slip skeletal pedaling**, we decided for **a dual-layer Canvas2D + inline SVG architecture with closed-form Law-of-Cosines 2-bone IK and longitudinal cycling dynamics** and neglected **pure CSS keyframe animation or external WebGL engines**, to achieve **exact $0.00\text{ px}$ pedal locking, interactive $-10\%\text{ to }+15\%$ gradient physics, live $C_d A$ aerodynamic wake telemetry, and strict zero-dependency `default-src 'none'` CSP portability**.
