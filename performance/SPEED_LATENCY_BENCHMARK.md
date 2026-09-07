# Speed & Latency Benchmark

Requested explicitly by Professor Geronazzo: a quantitative characterization
of our current implementation's computational performance, independent of
Raspberry Pi deployment (which is confirmed optional for this course).

Contributed by: **[your name here]**

## Measured pipeline performance

| Metric | Average | Minimum | Maximum |
|---|---|---|---|
| Achievable Frame Rate | 15.54 FPS | 9.38 FPS | 29.98 FPS |
| Camera Capture Latency | 8.14 ms | 1.60 ms | 26.80 ms |
| MediaPipe Extraction Time | 43.80 ms | 13.90 ms | 126.20 ms |
| TFLite Inference Time | 0.19 ms | 0.10 ms | 0.80 ms |
| Overall Pipeline Latency | 54.78 ms | 18.10 ms | 148.90 ms |

![Speed and latency benchmark table](performance/speed_latency_benchmark.png)

## The key finding

**MediaPipe's hand-detection step is the actual bottleneck, not the trained
classifier.** On average, MediaPipe extraction takes 43.80 ms — about 80% of
the 54.78 ms total pipeline latency. The classifier itself (whichever of
FC / CNN / Transformer is deployed) responds in under 1 ms, which is
negligible by comparison.

**What this means for our accuracy-vs-speed trade-off discussion:** the
accuracy differences between our three architectures barely matter for
real-time performance, since classification time is a rounding error next
to hand detection. The real lever for speed is upstream of model choice —
a faster or lower-resolution detection stage, not swapping classifiers.

**Honesty note:** these numbers were measured for our currently deployed
classifier configuration in `app.py`. We recommend repeating this
benchmark explicitly for each of the three trained architectures
individually to confirm the finding holds across all of them (see
`benchmark_speed.py`).
