# Ollama Model Benchmark

Generated: 2026-06-25T19:36:39

## Per-Run Results

| Model | Prompt | Phase | Run | Think | Load sec | Wall sec | Tok/sec | Prompt tokens | Output tokens | Loaded GiB | VRAM GiB |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| qwen3:14b | chat-explain | cold | 1 | N | 4.06 | 17.948 | 23.01 | 41 | 316 | 13.55 | 13.55 |
| qwen3:14b | chat-explain | warm | 1 | N | 0.129 | 15.1 | 22.94 | 41 | 342 | 13.55 | 13.55 |
| qwen3:14b | chat-troubleshoot | cold | 1 | N | 1.836 | 42.581 | 22.63 | 46 | 919 | 13.55 | 13.55 |
| qwen3:14b | chat-troubleshoot | warm | 1 | N | 0.123 | 42.105 | 22.6 | 46 | 947 | 13.55 | 13.55 |
| qwen3:14b | chat-summarize | cold | 1 | N | 1.837 | 12.402 | 23.03 | 82 | 239 | 13.55 | 13.55 |
| qwen3:14b | chat-summarize | warm | 1 | N | 0.126 | 9.32 | 22.99 | 82 | 210 | 13.55 | 13.55 |
| qwen3:14b | ps-graph-device-list | cold | 1 | N | 1.841 | 166.413 | 21.56 | 65 | 3545 | 13.55 | 13.55 |
| qwen3:14b | ps-graph-device-list | warm | 1 | N | 0.119 | 121.769 | 21.89 | 65 | 2659 | 13.55 | 13.55 |
| qwen3:14b | ps-graph-stale-users | cold | 1 | N | 1.843 | 217.863 | 21.21 | 60 | 4578 | 13.55 | 13.55 |
| qwen3:14b | ps-graph-stale-users | warm | 1 | N | 0.117 | 216.602 | 21.2 | 60 | 4586 | 13.55 | 13.55 |
| qwen3:14b | ps-graph-app-assignment | cold | 1 | N | 1.849 | 195.458 | 21.34 | 52 | 4128 | 13.55 | 13.55 |
| qwen3:14b | ps-graph-app-assignment | warm | 1 | N | 0.117 | 142.698 | 21.71 | 52 | 3092 | 13.55 | 13.55 |
| qwen3:14b | runbook-offboard | cold | 1 | N | 1.846 | 68.28 | 22.41 | 66 | 1485 | 13.55 | 13.55 |
| qwen3:14b | runbook-offboard | warm | 1 | N | 0.123 | 75.629 | 22.32 | 66 | 1683 | 13.55 | 13.55 |
| qwen3:14b | runbook-cert-rotation | cold | 1 | N | 2.06 | 112.418 | 21.99 | 53 | 2423 | 13.55 | 13.55 |
| qwen3:14b | runbook-cert-rotation | warm | 1 | N | 0.118 | 103.092 | 22.03 | 53 | 2266 | 13.55 | 13.55 |
| qwen3:14b | script-daily-health | cold | 1 | N | 1.849 | 145.094 | 21.74 | 66 | 3110 | 13.55 | 13.55 |
| qwen3:14b | script-daily-health | warm | 1 | N | 0.12 | 147.443 | 21.7 | 66 | 3194 | 13.55 | 13.55 |
| qwen3:14b | clf-intent | cold | 1 | N | 2.056 | 13.96 | 22.91 | 101 | 268 | 13.55 | 13.55 |
| qwen3:14b | clf-intent | warm | 1 | N | 0.128 | 12.715 | 22.84 | 101 | 286 | 13.55 | 13.55 |
| qwen3:14b | clf-risk | cold | 1 | N | 1.859 | 13.583 | 22.97 | 82 | 265 | 13.55 | 13.55 |
| qwen3:14b | clf-risk | warm | 1 | N | 0.125 | 8.624 | 23.0 | 82 | 194 | 13.55 | 13.55 |
| qwen3:14b | clf-ambiguous | cold | 1 | N | 1.851 | 24.934 | 22.73 | 100 | 520 | 13.55 | 13.55 |
| qwen3:14b | clf-ambiguous | warm | 1 | N | 0.125 | 12.14 | 22.85 | 100 | 273 | 13.55 | 13.55 |
| qwen3:14b | ga-deprecated-module | cold | 1 | N | 2.058 | 129.952 | 21.86 | 85 | 2791 | 13.55 | 13.55 |
| qwen3:14b | ga-deprecated-module | warm | 1 | N | 0.121 | 147.811 | 21.69 | 85 | 3201 | 13.55 | 13.55 |
| qwen3:14b | ga-param-names | cold | 1 | N | 2.053 | 110.963 | 21.96 | 90 | 2387 | 13.55 | 13.55 |
| qwen3:14b | ga-param-names | warm | 1 | N | 0.121 | 189.417 | 21.33 | 90 | 4035 | 13.55 | 13.55 |
| qwen3:14b | ga-pagination | cold | 1 | N | 1.846 | 175.688 | 21.47 | 96 | 3728 | 13.55 | 13.55 |
| qwen3:14b | ga-pagination | warm | 1 | N | 0.128 | 239.113 | 21.01 | 96 | 5017 | 13.55 | 13.55 |
| qwen3:14b | ga-error-handling | cold | 1 | N | 1.845 | 347.318 | 20.3 | 120 | 7009 | 13.55 | 13.55 |
| qwen3:14b | ga-error-handling | warm | 1 | N | 0.11 | 285.128 | 20.68 | 120 | 5888 | 13.55 | 13.55 |
| qwen3:14b | ctx-short-ps | cold | 1 | N | 2.066 | 71.294 | 22.4 | 25 | 1548 | 13.55 | 13.55 |
| qwen3:14b | ctx-short-ps | warm | 1 | N | 0.124 | 54.477 | 22.52 | 25 | 1222 | 13.55 | 13.55 |
| qwen3.6:35b | chat-explain | cold | 1 | N | 9.276 | 39.338 | 54.04 | 41 | 1614 | 21.97 | 21.97 |
| qwen3.6:35b | chat-explain | warm | 1 | N | 0.208 | 30.104 | 51.24 | 41 | 1528 | 21.97 | 21.97 |
| qwen3.6:35b | chat-troubleshoot | cold | 1 | N | 8.507 | 39.058 | 54.01 | 46 | 1635 | 21.97 | 21.97 |
| qwen3.6:35b | chat-troubleshoot | warm | 1 | N | 0.197 | 40.26 | 51.85 | 46 | 2073 | 21.97 | 21.97 |
| qwen3.6:35b | chat-summarize | cold | 1 | N | 8.491 | 28.348 | 53.86 | 82 | 1053 | 21.97 | 21.97 |
| qwen3.6:35b | chat-summarize | warm | 1 | N | 0.201 | 15.863 | 51.45 | 82 | 802 | 21.97 | 21.97 |
| qwen3.6:35b | ps-graph-device-list | cold | 1 | N | 8.487 | 118.052 | 51.91 | 65 | 5671 | 21.97 | 21.97 |
| qwen3.6:35b | ps-graph-device-list | warm | 1 | N | 0.198 | 81.585 | 51.68 | 65 | 4199 | 21.97 | 21.97 |
| qwen3.6:35b | ps-graph-stale-users | cold | 1 | N | 8.487 | 129.06 | 51.98 | 59 | 6253 | 21.97 | 21.97 |
| qwen3.6:35b | ps-graph-stale-users | warm | 1 | N | 0.199 | 98.328 | 51.69 | 59 | 5067 | 21.97 | 21.97 |
| qwen3.6:35b | ps-graph-app-assignment | cold | 1 | N | 8.491 | 108.36 | 52.26 | 52 | 5205 | 21.97 | 21.97 |
| qwen3.6:35b | ps-graph-app-assignment | warm | 1 | N | 0.206 | 105.593 | 51.8 | 52 | 5452 | 21.97 | 21.97 |
| qwen3.6:35b | runbook-offboard | cold | 1 | N | 8.487 | 81.158 | 51.78 | 66 | 3752 | 21.97 | 21.97 |
| qwen3.6:35b | runbook-offboard | warm | 1 | N | 0.205 | 80.802 | 51.43 | 66 | 4138 | 21.97 | 21.97 |
| qwen3.6:35b | runbook-cert-rotation | cold | 1 | N | 8.481 | 77.065 | 52.2 | 53 | 3567 | 21.97 | 21.97 |
| qwen3.6:35b | runbook-cert-rotation | warm | 1 | N | 0.198 | 88.586 | 51.51 | 53 | 4546 | 21.97 | 21.97 |
| qwen3.6:35b | script-daily-health | cold | 1 | N | 8.535 | 143.338 | 51.17 | 66 | 6884 | 21.97 | 21.97 |
| qwen3.6:35b | script-daily-health | warm | 1 | N | 0.199 | 106.411 | 51.75 | 66 | 5491 | 21.97 | 21.97 |
| qwen3.6:35b | clf-intent | cold | 1 | N | 8.526 | 27.158 | 54.05 | 101 | 989 | 21.97 | 21.97 |
| qwen3.6:35b | clf-intent | warm | 1 | N | 0.227 | 17.923 | 51.41 | 101 | 906 | 21.97 | 21.97 |
| qwen3.6:35b | clf-risk | cold | 1 | N | 8.807 | 25.196 | 54.96 | 82 | 887 | 21.97 | 21.97 |
| qwen3.6:35b | clf-risk | warm | 1 | N | 0.21 | 23.224 | 51.18 | 82 | 1174 | 21.97 | 21.97 |
| qwen3.6:35b | clf-ambiguous | cold | 1 | N | 8.486 | 34.487 | 53.05 | 100 | 1364 | 21.97 | 21.97 |
| qwen3.6:35b | clf-ambiguous | warm | 1 | N | 0.218 | 25.593 | 51.15 | 100 | 1294 | 21.97 | 21.97 |
| qwen3.6:35b | ga-deprecated-module | cold | 1 | N | 8.482 | 110.499 | 52.14 | 84 | 5306 | 21.97 | 21.97 |
| qwen3.6:35b | ga-deprecated-module | warm | 1 | N | 0.2 | 117.788 | 51.43 | 84 | 6042 | 21.97 | 21.97 |
| qwen3.6:35b | ga-param-names | cold | 1 | N | 8.492 | 108.89 | 52.0 | 90 | 5201 | 21.97 | 21.97 |
| qwen3.6:35b | ga-param-names | warm | 1 | N | 0.201 | 109.776 | 51.53 | 90 | 5641 | 21.97 | 21.97 |
| qwen3.6:35b | ga-pagination | cold | 1 | N | 8.53 | 110.345 | 51.97 | 96 | 5277 | 21.97 | 21.97 |
| qwen3.6:35b | ga-pagination | warm | 1 | N | 0.204 | 98.817 | 51.7 | 96 | 5093 | 21.97 | 21.97 |
| qwen3.6:35b | ga-error-handling | cold | 1 | N | 8.483 | 156.968 | 51.16 | 120 | 7572 | 21.97 | 21.97 |
| qwen3.6:35b | ga-error-handling | warm | 1 | N | 0.209 | 130.377 | 51.21 | 120 | 6658 | 21.97 | 21.97 |
| qwen3.6:35b | ctx-short-ps | cold | 1 | N | 8.534 | 26.463 | 55.07 | 24 | 977 | 21.97 | 21.97 |
| qwen3.6:35b | ctx-short-ps | warm | 1 | N | 0.219 | 36.214 | 52.15 | 24 | 1873 | 21.97 | 21.97 |
| qwen3:8b | chat-explain | cold | 1 | N | 1.551 | 10.703 | 38.97 | 41 | 353 | 9.28 | 9.28 |
| qwen3:8b | chat-explain | warm | 1 | N | 0.122 | 9.809 | 38.48 | 41 | 371 | 9.28 | 9.28 |
| qwen3:8b | chat-troubleshoot | cold | 1 | N | 1.554 | 15.804 | 38.5 | 46 | 545 | 9.28 | 9.28 |
| qwen3:8b | chat-troubleshoot | warm | 1 | N | 0.122 | 17.541 | 38.29 | 46 | 665 | 9.28 | 9.28 |
| qwen3:8b | chat-summarize | cold | 1 | N | 1.561 | 7.851 | 38.91 | 82 | 240 | 9.28 | 9.28 |
| qwen3:8b | chat-summarize | warm | 1 | N | 0.125 | 9.458 | 38.43 | 82 | 357 | 9.28 | 9.28 |
| qwen3:8b | ps-graph-device-list | cold | 1 | N | 1.574 | 62.303 | 37.44 | 65 | 2269 | 9.28 | 9.28 |
| qwen3:8b | ps-graph-device-list | warm | 1 | N | 0.122 | 116.658 | 36.47 | 65 | 4246 | 9.28 | 9.28 |
| qwen3:8b | ps-graph-stale-users | cold | 1 | N | 1.592 | 88.895 | 36.92 | 60 | 3219 | 9.28 | 9.28 |
| qwen3:8b | ps-graph-stale-users | warm | 1 | N | 0.124 | 95.272 | 36.76 | 60 | 3493 | 9.28 | 9.28 |
| qwen3:8b | ps-graph-app-assignment | cold | 1 | N | 1.592 | 105.951 | 36.69 | 52 | 3825 | 9.28 | 9.28 |
| qwen3:8b | ps-graph-app-assignment | warm | 1 | N | 0.119 | 117.285 | 36.5 | 52 | 4271 | 9.28 | 9.28 |
| qwen3:8b | runbook-offboard | cold | 1 | N | 1.564 | 56.695 | 37.48 | 66 | 2062 | 9.28 | 9.28 |
| qwen3:8b | runbook-offboard | warm | 1 | N | 0.123 | 28.655 | 37.94 | 66 | 1079 | 9.28 | 9.28 |
| qwen3:8b | runbook-cert-rotation | cold | 1 | N | 1.564 | 58.17 | 37.44 | 53 | 2115 | 9.28 | 9.28 |
| qwen3:8b | runbook-cert-rotation | warm | 1 | N | 0.123 | 61.384 | 37.33 | 53 | 2283 | 9.28 | 9.28 |
| qwen3:8b | script-daily-health | cold | 1 | N | 1.561 | 112.516 | 36.5 | 66 | 4045 | 9.28 | 9.28 |
| qwen3:8b | script-daily-health | warm | 1 | N | 0.121 | 129.482 | 36.2 | 66 | 4677 | 9.28 | 9.28 |
| qwen3:8b | clf-intent | cold | 1 | N | 1.561 | 7.523 | 38.93 | 101 | 226 | 9.28 | 9.28 |
| qwen3:8b | clf-intent | warm | 1 | N | 0.124 | 5.514 | 38.53 | 101 | 206 | 9.28 | 9.28 |
| qwen3:8b | clf-risk | cold | 1 | N | 1.555 | 10.226 | 38.65 | 82 | 330 | 9.28 | 9.28 |
| qwen3:8b | clf-risk | warm | 1 | N | 0.124 | 8.26 | 38.45 | 82 | 311 | 9.28 | 9.28 |
| qwen3:8b | clf-ambiguous | cold | 1 | N | 1.591 | 7.592 | 38.86 | 100 | 228 | 9.28 | 9.28 |
| qwen3:8b | clf-ambiguous | warm | 1 | N | 0.126 | 5.122 | 38.57 | 100 | 191 | 9.28 | 9.28 |
| qwen3:8b | ga-deprecated-module | cold | 1 | N | 1.555 | 120.687 | 36.35 | 85 | 4325 | 9.28 | 9.28 |
| qwen3:8b | ga-deprecated-module | warm | 1 | N | 0.121 | 107.691 | 36.51 | 85 | 3922 | 9.28 | 9.28 |
| qwen3:8b | ga-param-names | cold | 1 | N | 1.591 | 87.125 | 36.94 | 90 | 3155 | 9.28 | 9.28 |
| qwen3:8b | ga-param-names | warm | 1 | N | 0.12 | 76.424 | 37.07 | 90 | 2824 | 9.28 | 9.28 |
| qwen3:8b | ga-pagination | cold | 1 | N | 1.567 | 157.197 | 35.83 | 96 | 5571 | 9.28 | 9.28 |
| qwen3:8b | ga-pagination | warm | 1 | N | 0.117 | 195.991 | 35.28 | 96 | 6902 | 9.28 | 9.28 |
| qwen3:8b | ga-error-handling | cold | 1 | N | 1.559 | 131.3 | 36.17 | 120 | 4687 | 9.28 | 9.28 |
| qwen3:8b | ga-error-handling | warm | 1 | N | 0.118 | 114.235 | 36.39 | 120 | 4147 | 9.28 | 9.28 |
| qwen3:8b | ctx-short-ps | cold | 1 | N | 1.566 | 34.728 | 37.94 | 25 | 1255 | 9.28 | 9.28 |
| qwen3:8b | ctx-short-ps | warm | 1 | N | 0.125 | 47.05 | 37.61 | 25 | 1762 | 9.28 | 9.28 |

JSONL: `ollama-benchmark-consolidated.jsonl`
CSV: `ollama-benchmark-consolidated.csv`
Responses: `ollama-responses-consolidated.md`
