# Hardware Requirements

This guide provides practical sizing for local/self-hosted deployments using Ollama (or compatible inference runtimes).

## Sizing Tiers

| Tier | CPU | RAM | GPU | Target Models | Use Case |
| --- | --- | --- | --- | --- | --- |
| Minimal | 8 cores | 32 GB | Optional (8 GB VRAM) | 3B-8B quantized | Personal experiments |
| Recommended | 12-16 cores | 64 GB | 24 GB VRAM | 8B-14B | Daily engineering workflow |
| Production | 32+ cores | 128+ GB | 48-80 GB+ total VRAM | 14B-70B (distributed/quantized) | Multi-user persistent orchestration |

## Storage

- NVMe SSD strongly recommended
- 100+ GB free for models, checkpoints, embeddings, and logs
- Use dedicated volumes for Postgres durability

## Networking

- Stable low-latency local network between app, model host, and database
- Consider reverse proxy and TLS termination for multi-user deployments

## Notes

- Quantized models reduce VRAM at quality/performance trade-offs.
- For production, plan observability and backup capacity in addition to inference hardware.
