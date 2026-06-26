# Ollama Model Benchmark

Generated: 2026-06-26T07:30:34

## Per-Run Results

| Model | Prompt | Phase | Run | Think | Load sec | Wall sec | Tok/sec | Prompt tokens | Output tokens | Loaded GiB | VRAM GiB |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| gemma4:26b | chat-explain | cold | 1 | N | 33.337 | 48.032 | 50.77 | 44 | 717 | 16.22 | 16.22 |
| gemma4:26b | chat-explain | cold | 2 | N | 55.626 | 69.902 | 49.65 | 44 | 672 | 16.22 | 16.22 |
| gemma4:26b | chat-explain | cold | 3 | N | 64.675 | 80.023 | 49.74 | 44 | 735 | 16.22 | 16.22 |
| gemma4:26b | chat-troubleshoot | cold | 1 | N | 97.213 | 115.946 | 48.41 | 53 | 874 | 16.22 | 16.22 |
| gemma4:26b | chat-troubleshoot | cold | 2 | N | 122.626 | 145.307 | 48.04 | 53 | 1056 | 16.22 | 16.22 |
| gemma4:26b | chat-troubleshoot | cold | 3 | N | 81.961 | 101.156 | 48.7 | 53 | 901 | 16.22 | 16.22 |
| gemma4:26b | chat-summarize | cold | 1 | N | 89.354 | 114.478 | 49.71 | 92 | 1208 | 16.02 | 16.02 |
| gemma4:26b | chat-summarize | cold | 2 | N | 98.91 | 112.789 | 49.31 | 92 | 644 | 16.02 | 16.02 |
| gemma4:26b | chat-summarize | cold | 3 | N | 83.277 | 98.879 | 49.78 | 92 | 744 | 16.02 | 16.02 |
| gemma4:26b | ps-graph-device-list | cold | 1 | N | 105.077 | 140.976 | 48.59 | 72 | 1707 | 16.24 | 16.24 |
| gemma4:26b | ps-graph-device-list | cold | 2 | N | 131.51 | 165.292 | 46.42 | 72 | 1533 | 16.24 | 16.24 |
| gemma4:26b | ps-graph-device-list | cold | 3 | N | 148.015 | 188.47 | 45.96 | 72 | 1818 | 16.24 | 16.24 |
| gemma4:26b | ps-graph-app-assignment | cold | 1 | N | 97.305 | 148.071 | 45.32 | 58 | 2262 | 16.24 | 16.24 |
| gemma4:26b | ps-graph-app-assignment | cold | 2 | N | 77.822 | 128.837 | 44.81 | 58 | 2248 | 16.24 | 16.24 |
| gemma4:26b | ps-graph-app-assignment | cold | 3 | N | 87.84 | 139.366 | 44.89 | 58 | 2276 | 16.24 | 16.24 |
| gemma4:26b | runbook-offboard | cold | 1 | N | 105.14 | 143.224 | 45.9 | 72 | 1707 | 16.24 | 16.24 |
| gemma4:26b | runbook-offboard | cold | 2 | N | 81.779 | 124.445 | 45.28 | 72 | 1896 | 16.24 | 16.24 |
| gemma4:26b | runbook-offboard | cold | 3 | N | 86.099 | 127.045 | 45.55 | 72 | 1828 | 16.24 | 16.24 |
| gemma4:26b | runbook-cert-rotation | cold | 1 | N | 79.107 | 131.017 | 44.47 | 60 | 2267 | 16.24 | 16.24 |
| gemma4:26b | runbook-cert-rotation | cold | 2 | N | 133.621 | 181.736 | 45.1 | 60 | 2123 | 16.24 | 16.24 |
| gemma4:26b | runbook-cert-rotation | cold | 3 | N | 79.924 | 134.323 | 44.37 | 60 | 2375 | 16.24 | 16.24 |
| gemma4:26b | script-daily-health | cold | 1 | N | 100.903 | 146.675 | 44.57 | 70 | 2005 | 16.22 | 16.22 |
| gemma4:26b | script-daily-health | cold | 2 | N | 141.708 | 198.166 | 44.71 | 70 | 2482 | 16.22 | 16.22 |
| gemma4:26b | script-daily-health | cold | 3 | N | 112.573 | 146.948 | 46.34 | 70 | 1560 | 16.22 | 16.22 |
| gemma4:26b | clf-intent | cold | 1 | N | 55.132 | 64.026 | 50.94 | 110 | 419 | 16.02 | 16.02 |
| gemma4:26b | clf-intent | cold | 2 | N | 59.653 | 69.41 | 50.8 | 110 | 463 | 16.02 | 16.02 |
| gemma4:26b | clf-intent | cold | 3 | N | 73.413 | 81.672 | 51.42 | 110 | 396 | 16.02 | 16.02 |
| gemma4:26b | clf-risk | cold | 1 | N | 71.361 | 78.751 | 51.47 | 88 | 349 | 16.02 | 16.02 |
| gemma4:26b | clf-risk | cold | 2 | N | 128.143 | 137.772 | 50.76 | 88 | 455 | 16.02 | 16.02 |
| gemma4:26b | clf-risk | cold | 3 | N | 71.47 | 79.796 | 51.05 | 88 | 396 | 16.02 | 16.02 |
| gemma4:26b | clf-ambiguous | cold | 1 | N | 65.82 | 75.561 | 50.35 | 107 | 458 | 16.02 | 16.02 |
| gemma4:26b | clf-ambiguous | cold | 2 | N | 75.694 | 109.022 | 46.93 | 107 | 1530 | 16.02 | 16.02 |
| gemma4:26b | clf-ambiguous | cold | 3 | N | 78.193 | 92.915 | 49.75 | 107 | 696 | 16.02 | 16.02 |
| gemma4:26b | ga-param-names | cold | 1 | N | 94.424 | 127.447 | 46.65 | 151 | 1502 | 16.27 | 16.27 |
| gemma4:26b | ga-param-names | cold | 2 | N | 104.508 | 142.856 | 45.76 | 151 | 1717 | 16.27 | 16.27 |
| gemma4:26b | ga-param-names | cold | 3 | N | 71.165 | 112.311 | 45.69 | 151 | 1836 | 16.27 | 16.27 |
| gemma4:26b | ga-pagination | cold | 1 | N | 93.544 | 138.707 | 45.55 | 104 | 2012 | 16.27 | 16.27 |
| gemma4:26b | ga-pagination | cold | 2 | N | 89.559 | 133.181 | 45.74 | 104 | 1957 | 16.27 | 16.27 |
| gemma4:26b | ga-pagination | cold | 3 | N | 75.112 | 119.676 | 45.4 | 104 | 1984 | 16.27 | 16.27 |
| gemma4:26b | ctx-short-ps | cold | 1 | N | 73.661 | 94.529 | 47.71 | 31 | 962 | 16.02 | 16.02 |
| gemma4:26b | ctx-short-ps | cold | 2 | N | 100.07 | 116.679 | 48.72 | 31 | 771 | 16.02 | 16.02 |
| gemma4:26b | ctx-short-ps | cold | 3 | N | 66.108 | 84.268 | 48.07 | 31 | 844 | 16.02 | 16.02 |
| gemma4:26b | ctx-medium-ps | cold | 1 | N | 86.07 | 123.769 | 45.86 | 154 | 1687 | 16.22 | 16.22 |
| gemma4:26b | ctx-medium-ps | cold | 2 | N | 97.715 | 124.337 | 46.82 | 154 | 1214 | 16.22 | 16.22 |
| gemma4:26b | ctx-medium-ps | cold | 3 | N | 60.709 | 93.131 | 46.5 | 154 | 1466 | 16.22 | 16.22 |
| gemma4:26b | ctx-long-ps | cold | 1 | N | 102.773 | 152.627 | 44.38 | 685 | 2131 | 16.27 | 16.27 |
| gemma4:26b | ctx-long-ps | cold | 2 | N | 111.382 | 163.085 | 44.06 | 685 | 2212 | 16.27 | 16.27 |
| gemma4:26b | ctx-long-ps | cold | 3 | N | 99.626 | 156.803 | 43.24 | 685 | 2415 | 16.27 | 16.27 |
| qwen3.6:35b | chat-explain | cold | 1 | N | 10.453 | 37.04 | 57.5 | 41 | 1515 | 21.48 | 21.48 |
| qwen3.6:35b | chat-explain | cold | 2 | N | 8.754 | 29.866 | 58.31 | 41 | 1221 | 21.48 | 21.48 |
| qwen3.6:35b | chat-explain | cold | 3 | N | 8.753 | 23.032 | 58.45 | 41 | 824 | 21.48 | 21.48 |
| qwen3.6:35b | chat-troubleshoot | cold | 1 | N | 8.756 | 48.736 | 53.25 | 46 | 2119 | 21.48 | 21.48 |
| qwen3.6:35b | chat-troubleshoot | cold | 2 | N | 8.766 | 41.191 | 54.22 | 46 | 1744 | 21.48 | 21.48 |
| qwen3.6:35b | chat-troubleshoot | cold | 3 | N | 8.497 | 47.743 | 52.83 | 46 | 2064 | 21.48 | 21.48 |
| qwen3.6:35b | chat-summarize | cold | 1 | N | 8.511 | 47.983 | 53.11 | 82 | 2083 | 21.39 | 21.39 |
| qwen3.6:35b | chat-summarize | cold | 2 | N | 8.797 | 34.388 | 54.84 | 82 | 1389 | 21.39 | 21.39 |
| qwen3.6:35b | chat-summarize | cold | 3 | N | 8.755 | 38.848 | 54.59 | 82 | 1629 | 21.39 | 21.39 |
| qwen3.6:35b | ps-graph-device-list | cold | 1 | N | 8.762 | 104.324 | 51.82 | 65 | 4940 | 21.64 | 21.64 |
| qwen3.6:35b | ps-graph-device-list | cold | 2 | N | 8.757 | 113.099 | 51.72 | 65 | 5385 | 21.64 | 21.64 |
| qwen3.6:35b | ps-graph-device-list | cold | 3 | N | 8.766 | 109.292 | 51.63 | 65 | 5178 | 21.64 | 21.64 |
| qwen3.6:35b | ps-graph-app-assignment | cold | 1 | N | 8.515 | 92.631 | 52.23 | 52 | 4383 | 21.64 | 21.64 |
| qwen3.6:35b | ps-graph-app-assignment | cold | 2 | N | 8.516 | 133.689 | 51.58 | 52 | 6446 | 21.64 | 21.64 |
| qwen3.6:35b | ps-graph-app-assignment | cold | 3 | N | 8.767 | 143.162 | 51.52 | 52 | 6914 | 21.64 | 21.64 |
| qwen3.6:35b | runbook-offboard | cold | 1 | N | 8.772 | 74.774 | 52.64 | 66 | 3463 | 21.64 | 21.64 |
| qwen3.6:35b | runbook-offboard | cold | 2 | N | 8.756 | 84.845 | 51.92 | 66 | 3937 | 21.64 | 21.64 |
| qwen3.6:35b | runbook-offboard | cold | 3 | N | 8.757 | 83.121 | 51.65 | 66 | 3828 | 21.64 | 21.64 |
| qwen3.6:35b | runbook-cert-rotation | cold | 1 | N | 8.752 | 80.222 | 51.67 | 53 | 3682 | 21.64 | 21.64 |
| qwen3.6:35b | runbook-cert-rotation | cold | 2 | N | 8.766 | 75.619 | 52.5 | 53 | 3497 | 21.64 | 21.64 |
| qwen3.6:35b | runbook-cert-rotation | cold | 3 | N | 8.761 | 78.73 | 52.42 | 53 | 3657 | 21.64 | 21.64 |
| qwen3.6:35b | script-daily-health | cold | 1 | N | 8.754 | 65.0 | 51.35 | 66 | 2876 | 21.48 | 21.48 |
| qwen3.6:35b | script-daily-health | cold | 2 | N | 8.775 | 120.004 | 51.81 | 66 | 5751 | 21.48 | 21.48 |
| qwen3.6:35b | script-daily-health | cold | 3 | N | 8.78 | 125.21 | 51.27 | 66 | 5958 | 21.48 | 21.48 |
| qwen3.6:35b | clf-intent | cold | 1 | N | 8.523 | 32.471 | 52.78 | 101 | 1247 | 21.39 | 21.39 |
| qwen3.6:35b | clf-intent | cold | 2 | N | 8.755 | 32.695 | 53.29 | 101 | 1259 | 21.39 | 21.39 |
| qwen3.6:35b | clf-intent | cold | 3 | N | 8.505 | 33.112 | 53.4 | 101 | 1298 | 21.39 | 21.39 |
| qwen3.6:35b | clf-risk | cold | 1 | N | 8.79 | 35.852 | 53.98 | 82 | 1447 | 21.39 | 21.39 |
| qwen3.6:35b | clf-risk | cold | 2 | N | 8.754 | 35.084 | 53.38 | 82 | 1392 | 21.39 | 21.39 |
| qwen3.6:35b | clf-risk | cold | 3 | N | 8.775 | 28.193 | 54.63 | 82 | 1047 | 21.39 | 21.39 |
| qwen3.6:35b | clf-ambiguous | cold | 1 | N | 8.755 | 36.736 | 54.0 | 100 | 1492 | 21.39 | 21.39 |
| qwen3.6:35b | clf-ambiguous | cold | 2 | N | 8.748 | 42.767 | 54.31 | 100 | 1832 | 21.39 | 21.39 |
| qwen3.6:35b | clf-ambiguous | cold | 3 | N | 8.501 | 46.284 | 53.3 | 100 | 1996 | 21.39 | 21.39 |
| qwen3.6:35b | ga-param-names | cold | 1 | N | 8.747 | 108.346 | 51.85 | 140 | 5146 | 21.97 | 21.97 |
| qwen3.6:35b | ga-param-names | cold | 2 | N | 8.759 | 121.8 | 51.72 | 140 | 5831 | 21.97 | 21.97 |
| qwen3.6:35b | ga-param-names | cold | 3 | N | 8.761 | 107.618 | 52.08 | 140 | 5133 | 21.97 | 21.97 |
| qwen3.6:35b | ga-pagination | cold | 1 | N | 8.763 | 118.613 | 52.29 | 96 | 5728 | 21.97 | 21.97 |
| qwen3.6:35b | ga-pagination | cold | 2 | N | 8.758 | 92.575 | 52.75 | 96 | 4406 | 21.97 | 21.97 |
| qwen3.6:35b | ga-pagination | cold | 3 | N | 8.756 | 118.539 | 51.91 | 96 | 5684 | 21.97 | 21.97 |
| qwen3.6:35b | ctx-short-ps | cold | 1 | N | 8.51 | 37.388 | 54.33 | 24 | 1561 | 21.39 | 21.39 |
| qwen3.6:35b | ctx-short-ps | cold | 2 | N | 8.755 | 39.613 | 53.83 | 24 | 1652 | 21.39 | 21.39 |
| qwen3.6:35b | ctx-short-ps | cold | 3 | N | 8.758 | 59.439 | 52.91 | 24 | 2671 | 21.39 | 21.39 |
| qwen3.6:35b | ctx-medium-ps | cold | 1 | N | 8.763 | 118.575 | 51.96 | 144 | 5690 | 21.48 | 21.48 |
| qwen3.6:35b | ctx-medium-ps | cold | 2 | N | 8.77 | 85.167 | 52.49 | 144 | 3994 | 21.48 | 21.48 |
| qwen3.6:35b | ctx-medium-ps | cold | 3 | N | 8.763 | 112.069 | 52.54 | 144 | 5412 | 21.48 | 21.48 |
| qwen3.6:35b | ctx-long-ps | cold | 1 | N | 8.75 | 187.507 | 51.31 | 630 | 9123 | 21.97 | 21.97 |
| qwen3.6:35b | ctx-long-ps | cold | 2 | N | 8.751 | 153.333 | 50.82 | 630 | 7296 | 21.97 | 21.97 |
| qwen3.6:35b | ctx-long-ps | cold | 3 | N | 8.755 | 175.686 | 50.64 | 630 | 8406 | 21.97 | 21.97 |

## Averaged Results — Standard Mode

| Model | Prompt | Phase | Avg Tok/sec | ±Stddev | Avg Wall sec | Avg Output tokens | Loaded GiB |
|---|---|---:|---:|---:|---:|---:|---:|
| gemma4:26b | chat-explain | cold | 50.053 | 0.622 | 65.986 | 708 | 16.22 |
| gemma4:26b | chat-troubleshoot | cold | 48.383 | 0.331 | 120.803 | 944 | 16.22 |
| gemma4:26b | chat-summarize | cold | 49.6 | 0.254 | 108.715 | 865 | 16.02 |
| gemma4:26b | ps-graph-device-list | cold | 46.99 | 1.405 | 164.913 | 1686 | 16.24 |
| gemma4:26b | ps-graph-app-assignment | cold | 45.007 | 0.274 | 138.758 | 2262 | 16.24 |
| gemma4:26b | runbook-offboard | cold | 45.577 | 0.311 | 131.571 | 1810 | 16.24 |
| gemma4:26b | runbook-cert-rotation | cold | 44.647 | 0.396 | 149.025 | 2255 | 16.24 |
| gemma4:26b | script-daily-health | cold | 45.207 | 0.984 | 163.93 | 2016 | 16.22 |
| gemma4:26b | clf-intent | cold | 51.053 | 0.325 | 71.703 | 426 | 16.02 |
| gemma4:26b | clf-risk | cold | 51.093 | 0.357 | 98.773 | 400 | 16.02 |
| gemma4:26b | clf-ambiguous | cold | 49.01 | 1.826 | 92.499 | 895 | 16.02 |
| gemma4:26b | ga-param-names | cold | 46.033 | 0.535 | 127.538 | 1685 | 16.27 |
| gemma4:26b | ga-pagination | cold | 45.563 | 0.17 | 130.521 | 1984 | 16.27 |
| gemma4:26b | ctx-short-ps | cold | 48.167 | 0.512 | 98.492 | 859 | 16.02 |
| gemma4:26b | ctx-medium-ps | cold | 46.393 | 0.489 | 113.746 | 1456 | 16.22 |
| gemma4:26b | ctx-long-ps | cold | 43.893 | 0.588 | 157.505 | 2253 | 16.27 |
| qwen3.6:35b | chat-explain | cold | 58.087 | 0.513 | 29.979 | 1187 | 21.48 |
| qwen3.6:35b | chat-troubleshoot | cold | 53.433 | 0.713 | 45.89 | 1976 | 21.48 |
| qwen3.6:35b | chat-summarize | cold | 54.18 | 0.935 | 40.406 | 1700 | 21.39 |
| qwen3.6:35b | ps-graph-device-list | cold | 51.723 | 0.095 | 108.905 | 5168 | 21.64 |
| qwen3.6:35b | ps-graph-app-assignment | cold | 51.777 | 0.394 | 123.161 | 5914 | 21.64 |
| qwen3.6:35b | runbook-offboard | cold | 52.07 | 0.512 | 80.913 | 3743 | 21.64 |
| qwen3.6:35b | runbook-cert-rotation | cold | 52.197 | 0.458 | 78.19 | 3612 | 21.64 |
| qwen3.6:35b | script-daily-health | cold | 51.477 | 0.291 | 103.405 | 4862 | 21.48 |
| qwen3.6:35b | clf-intent | cold | 53.157 | 0.331 | 32.759 | 1268 | 21.39 |
| qwen3.6:35b | clf-risk | cold | 53.997 | 0.625 | 33.043 | 1295 | 21.39 |
| qwen3.6:35b | clf-ambiguous | cold | 53.87 | 0.517 | 41.929 | 1773 | 21.39 |
| qwen3.6:35b | ga-param-names | cold | 51.883 | 0.182 | 112.588 | 5370 | 21.97 |
| qwen3.6:35b | ga-pagination | cold | 52.317 | 0.421 | 109.909 | 5273 | 21.97 |
| qwen3.6:35b | ctx-short-ps | cold | 53.69 | 0.72 | 45.48 | 1961 | 21.39 |
| qwen3.6:35b | ctx-medium-ps | cold | 52.33 | 0.321 | 105.27 | 5032 | 21.48 |
| qwen3.6:35b | ctx-long-ps | cold | 50.923 | 0.347 | 172.175 | 8275 | 21.97 |

JSONL: `ollama-benchmark-20260626-044847.jsonl`
CSV: `ollama-benchmark-20260626-044847.csv`
Responses: `ollama-responses-20260626-044847.md`
