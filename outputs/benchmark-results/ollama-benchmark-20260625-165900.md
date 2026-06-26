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
| qwen2.5-coder:32b | chat-explain | cold | 1 | N | 54.105 | 66.922 | 10.51 | 60 | 130 | 26.29 | 26.29 |
| qwen2.5-coder:32b | chat-explain | warm | 1 | N | 0.125 | 14.211 | 10.54 | 60 | 147 | 26.29 | 26.29 |
| qwen2.5-coder:32b | chat-troubleshoot | cold | 1 | N | 77.097 | 102.016 | 10.43 | 65 | 254 | 26.29 | 26.29 |
| qwen2.5-coder:32b | chat-troubleshoot | warm | 1 | N | 0.129 | 32.332 | 10.42 | 65 | 334 | 26.29 | 26.29 |
| qwen2.5-coder:32b | chat-summarize | cold | 1 | N | 87.966 | 95.509 | 10.49 | 101 | 73 | 26.29 | 26.29 |
| qwen2.5-coder:32b | chat-summarize | warm | 1 | N | 0.133 | 6.883 | 10.54 | 101 | 70 | 26.29 | 26.29 |
| qwen2.5-coder:32b | ps-graph-device-list | cold | 1 | N | 88.881 | 161.971 | 10.24 | 84 | 742 | 26.29 | 26.29 |
| qwen2.5-coder:32b | ps-graph-device-list | warm | 1 | N | 0.138 | 50.737 | 10.29 | 84 | 519 | 26.29 | 26.29 |
| qwen2.5-coder:32b | ps-graph-stale-users | cold | 1 | N | 71.575 | 140.763 | 10.27 | 79 | 704 | 26.29 | 26.29 |
| qwen2.5-coder:32b | ps-graph-stale-users | warm | 1 | N | 0.132 | 79.252 | 10.29 | 79 | 812 | 26.29 | 26.29 |
| qwen2.5-coder:32b | ps-graph-app-assignment | cold | 1 | N | 85.666 | 157.265 | 10.31 | 71 | 732 | 26.29 | 26.29 |
| qwen2.5-coder:32b | ps-graph-app-assignment | warm | 1 | N | 0.126 | 77.476 | 10.35 | 71 | 799 | 26.29 | 26.29 |
| qwen2.5-coder:32b | runbook-offboard | cold | 1 | N | 81.627 | 144.946 | 10.25 | 85 | 642 | 26.29 | 26.29 |
| qwen2.5-coder:32b | runbook-offboard | warm | 1 | N | 0.136 | 65.489 | 10.31 | 85 | 672 | 26.29 | 26.29 |
| qwen2.5-coder:32b | runbook-cert-rotation | cold | 1 | N | 72.241 | 192.742 | 10.24 | 72 | 1227 | 26.29 | 26.29 |
| qwen2.5-coder:32b | runbook-cert-rotation | warm | 1 | N | 0.119 | 124.959 | 10.22 | 72 | 1274 | 26.29 | 26.29 |
| qwen2.5-coder:32b | script-daily-health | cold | 1 | N | 62.297 | 139.107 | 10.23 | 85 | 779 | 26.29 | 26.29 |
| qwen2.5-coder:32b | script-daily-health | warm | 1 | N | 0.124 | 68.587 | 10.31 | 85 | 704 | 26.29 | 26.29 |
| qwen2.5-coder:32b | clf-intent | cold | 1 | N | 111.971 | 115.896 | 10.75 | 120 | 35 | 26.29 | 26.29 |
| qwen2.5-coder:32b | clf-intent | warm | 1 | N | 0.139 | 3.616 | 10.69 | 120 | 36 | 26.29 | 26.29 |
| qwen2.5-coder:32b | clf-risk | cold | 1 | N | 72.334 | 76.361 | 10.73 | 101 | 37 | 26.29 | 26.29 |
| qwen2.5-coder:32b | clf-risk | warm | 1 | N | 0.134 | 4.032 | 10.56 | 101 | 40 | 26.29 | 26.29 |
| qwen2.5-coder:32b | clf-ambiguous | cold | 1 | N | 95.624 | 100.804 | 10.58 | 119 | 48 | 26.29 | 26.29 |
| qwen2.5-coder:32b | clf-ambiguous | warm | 1 | N | 0.146 | 4.564 | 10.67 | 119 | 46 | 26.29 | 26.29 |
| qwen2.5-coder:32b | ga-deprecated-module | cold | 1 | N | 80.683 | 138.836 | 10.29 | 104 | 591 | 26.29 | 26.29 |
| qwen2.5-coder:32b | ga-deprecated-module | warm | 1 | N | 0.142 | 66.921 | 10.3 | 104 | 686 | 26.29 | 26.29 |
| qwen2.5-coder:32b | ga-param-names | cold | 1 | N | 81.698 | 139.997 | 10.28 | 109 | 592 | 26.29 | 26.29 |
| qwen2.5-coder:32b | ga-param-names | warm | 1 | N | 0.128 | 67.975 | 10.26 | 109 | 694 | 26.29 | 26.29 |
| qwen2.5-coder:32b | ga-pagination | cold | 1 | N | 92.709 | 149.302 | 10.21 | 115 | 570 | 26.29 | 26.29 |
| qwen2.5-coder:32b | ga-pagination | warm | 1 | N | 0.136 | 79.294 | 10.29 | 115 | 812 | 26.29 | 26.29 |
| qwen2.5-coder:32b | ga-error-handling | cold | 1 | N | 100.738 | 202.914 | 10.2 | 139 | 1033 | 26.29 | 26.29 |
| qwen2.5-coder:32b | ga-error-handling | warm | 1 | N | 0.139 | 96.894 | 10.28 | 139 | 992 | 26.29 | 26.29 |
| qwen2.5-coder:32b | ctx-short-ps | cold | 1 | N | 77.309 | 106.094 | 10.34 | 44 | 293 | 26.29 | 26.29 |
| qwen2.5-coder:32b | ctx-short-ps | warm | 1 | N | 0.124 | 17.146 | 10.43 | 44 | 176 | 26.29 | 26.29 |
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

JSONL: `ollama-benchmark-20260625-165900.jsonl`
CSV: `ollama-benchmark-20260625-165900.csv`
Responses: `ollama-responses-20260625-165900.md`
