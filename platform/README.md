# Platform core (severable)

Runtime-neutral schemas, gate registry, and staged imports.

- **manifest.yaml** — platform version and supported OS
- **schemas/** — workspace + plugin JSON Schema
- **gates/registry.yaml** — HITL gate definitions
- **imports/** — FarmRTK + MATM copies (generalize per REFACTOR_TODO)

Python runtime: `src/platform/`