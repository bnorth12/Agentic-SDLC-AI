# Plugins — severable packs

**Parent:** [FRAMEWORK_DECOMPOSITION.md](../docs/charter/FRAMEWORK_DECOMPOSITION.md)

## Layout

```
plugins/
  _template/          Copy to create new pack
  packs/
    engineering-sdlc/   FarmRTK-derived SE skills (imports/)
    threat-modeling/    MATM LangGraph wrapper
    github-devops/      Actions + gh CLI templates
```

## Manifest

Each pack requires `plugin.manifest.yaml` validated against `platform/schemas/plugin-manifest.schema.json`.

## Loader

```python
from src.platform.plugins import PluginLoader
for p in PluginLoader().discover():
    print(p.id, p.version)
```