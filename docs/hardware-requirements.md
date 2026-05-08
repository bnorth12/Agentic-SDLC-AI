# Hardware Requirements

## Minimal (Prototyping)
- CPU: Modern 8+ core
- RAM: 32 GB
- GPU: 8–12 GB VRAM (e.g., RTX 3060/4060) or Apple M1/M2
- Storage: 500 GB SSD
- Models: 7B–13B quantized (Llama 3.1 8B, Mistral, etc.)

## Recommended (Daily Use)
- CPU: 12+ core
- RAM: 64–128 GB
- GPU: RTX 4090 (24 GB) or better / Apple M3 Max / M4 Pro (64+ GB unified)
- Storage: 1–2 TB NVMe SSD
- Models: 32B–70B quantized

## Production / Heavy Workloads
- Multi-GPU server (2–4 × 4090 or A6000)
- 128–256 GB RAM
- Dedicated storage array
- Supports 70B+ models or multiple simultaneous agents

**Notes**:
- Ollama works great for most use cases.
- Use quantized models (Q4_K_M / Q5_K_M) for best performance.
- CPU-only is possible but slow for larger models.