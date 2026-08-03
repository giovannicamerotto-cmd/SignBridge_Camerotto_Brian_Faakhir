# Results & Evaluation

This section covers model comparison results, how to read the confusion
matrices, and an honest discussion of what our evaluation does and does
not currently measure.

Contributed by: **[your name here]**

---

## 1. Results — Per-Model Evaluation

We trained three architectures on the identical dataset, split, and
metrics, so the comparison is fair:

| Model | Accuracy | Macro F1 | Weighted F1 |
|---|---|---|---|
| Fully-Connected (baseline) | 0.89 | 0.88 | 0.89 |
| CNN | 0.90 | 0.90 | 0.90 |
| Transformer | 0.94 | 0.93 | 0.94 |

**Fully-Connected (baseline):** the simplest architecture — it treats
the whole gesture window as one flat list of numbers, with no built-in
sense of "what happened first." Any timing information has to be
learned implicitly, if at all. This is why it's the weakest of the
three, and why it's used as our baseline (the reference every other
model has to beat).

![Fully-Connected architecture](results/architecture_fc.png)
![Fully-Connected confusion matrix](results/confusion_matrix_fc.png)

**CNN:** adds convolutional layers that slide across nearby frames,
letting the model learn short local motion patterns (e.g. "fingers
closing over 2–3 frames") instead of memorizing a flat vector. Modest
accuracy gain over the baseline.

![CNN architecture](results/architecture_cnn.png)
![CNN confusion matrix](results/confusion_matrix_cnn.png)

**Transformer:** uses self-attention, so every frame can directly
"look at" every other frame, not just its neighbors. It learns which
1–2 frames actually decided the sign and focuses on those — this is
why it performs best overall.

![Transformer architecture](results/architecture_transformer.png)
![Transformer confusion matrix](results/confusion_matrix_transformer.png)

---

## 2. Reading the Confusion Matrix

For any single gesture class, every prediction falls into one of four
buckets:

- **True Positive (TP):** the gesture *was* that class, and the model
  said so correctly.
- **False Negative (FN):** the gesture *was* that class, but the model
  missed it.
- **False Positive (FP):** the gesture *was a different* class, but the
  model wrongly called it this class.
- **True Negative (TN):** the gesture was *not* this class, and the
  model correctly didn't call it this class.

**The formulas:**

```
Accuracy  = (TP + TN) / (TP + TN + FP + FN)
Precision = TP / (TP + FP)     -- of what we called this class, how much was right
Recall    = TP / (TP + FN)     -- of what actually was this class, how much we caught
F1        = 2 * (Precision * Recall) / (Precision + Recall)
```

**Worked example** (Transformer, one gesture class, from our own
confusion matrix): TP = 7, FN = 3, FP = 0, TN = 53 (out of 63 samples).

```
Precision = 7 / 7  = 1.00
Recall    = 7 / 10 = 0.70
F1        = 2 * (1.00 * 0.70) / (1.00 + 0.70) = 0.82
```

This matches our classification report exactly, confirming the metrics
are computed correctly and not just copy-pasted from a library without
understanding what they mean.

---

## 3. Results — Head-to-Head

| Model | Accuracy | Relative compute (estimate, not measured) |
|---|---|---|
| Fully-Connected | 0.89 | Lowest |
| CNN | 0.90 | Medium |
| Transformer | 0.94 | Highest |

![Accuracy comparison chart](results/results_head_to_head.png)

The Transformer wins on accuracy because self-attention lets it weigh
the most informative frames instead of treating every frame equally.
But accuracy alone doesn't tell the whole story — see below.

---

## 4. Accuracy Isn't Everything

**What we measured:** classification quality — accuracy, precision,
recall, F1 — for all three models, on the same held-out test set.

**What we did *not* measure:** inference speed (latency in milliseconds,
or frames-per-second). This matters here because SignBridge controls a
robot in real time. A model that's more accurate but slower to respond
could actually be *less* safe — for a gesture like STOP, a delayed
reaction matters. Speed also affects dynamic gestures directly, since
they're read from a short window of frames: a slower model effectively
"sees" less motion per second.

**Recommendation for completing this evaluation:** time each model's
prediction on the same machine (e.g. `time.perf_counter()` around 100+
repeated predictions, averaged), report milliseconds per prediction and
the resulting FPS, and repeat the test on the target Raspberry Pi
hardware, not just a laptop. Plot accuracy against measured speed before
picking a model for production — the most accurate model on paper may
not be the right one to actually deploy.

**Why we're stating this directly instead of leaving it out:** an
honest, named limitation is stronger than an unverified claim. This is
also flagged as a concrete next step in our final presentation.
