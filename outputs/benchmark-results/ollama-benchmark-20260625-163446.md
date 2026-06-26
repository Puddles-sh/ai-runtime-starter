# Ollama Model Benchmark

Generated: 2026-06-25T16:50:01

## Per-Run Results

| Model | Prompt | Phase | Run | Think | Load sec | Wall sec | Tok/sec | Prompt tokens | Output tokens | Loaded GiB | VRAM GiB |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| qwen3:14b | chat-explain | cold | 1 | N | 1.827 | 16.905 | 22.95 | 41 | 343 | 13.55 | 13.55 |
| qwen3:14b | chat-explain | warm | 1 | N | 0.127 | 14.472 | 22.9 | 41 | 327 | 13.55 | 13.55 |
| qwen3:14b | chat-troubleshoot | cold | 1 | N | 1.835 | 30.765 | 22.75 | 46 | 655 | 13.55 | 13.55 |
| qwen3:14b | chat-troubleshoot | warm | 1 | N | 0.122 | 26.44 | 22.75 | 46 | 597 | 13.55 | 13.55 |
| qwen3:14b | chat-summarize | cold | 1 | N | 2.056 | 15.244 | 22.92 | 82 | 298 | 13.55 | 13.55 |
| qwen3:14b | chat-summarize | warm | 1 | N | 0.127 | 14.015 | 22.86 | 82 | 316 | 13.55 | 13.55 |
| qwen3:14b | ps-graph-device-list | cold | 1 | N | 2.062 | 216.733 | 21.19 | 65 | 4546 | 13.55 | 13.55 |
| qwen3:14b | ps-graph-device-list | warm | 1 | N | 0.121 | 132.527 | 21.8 | 65 | 2882 | 13.55 | 13.55 |
| qwen3:14b | ps-graph-stale-users | cold | 1 | N | 2.092 | 165.395 | 21.54 | 60 | 3514 | 13.55 | 13.55 |
| qwen3:14b | ps-graph-stale-users | warm | 1 | N | 0.117 | 188.492 | 21.35 | 60 | 4018 | 13.55 | 13.55 |

JSONL: `ollama-benchmark-20260625-163446.jsonl`
CSV: `ollama-benchmark-20260625-163446.csv`
Responses: `ollama-responses-20260625-163446.md`
