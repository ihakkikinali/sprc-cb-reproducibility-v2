# Analysis Scripts

These scripts reproduce the principal manuscript statistics from the fixed scored outputs in `../results/`.

The review package treats the per-image `sprc_cb_score` field as the canonical submitted SPRC-CB risk score and applies the same failure definitions and bootstrap protocols described in the manuscript. No model inference is required for these analyses.

## Scripts

### `reproduce_main_table.py`
Reproduces the pooled four-polyp-benchmark AUPRC/AUROC results for SPRC-CB, SPRC++-R, SAM confidence, mask-IoU disagreement, and linear SPRC at Dice < 0.70, < 0.80, and < 0.50.

```bash
python analysis_scripts/reproduce_main_table.py
```

### `per_site_ci_polyp.py`
Reproduces per-site AUPRC values and 95% paired-bootstrap intervals for the four polyp benchmarks.

```bash
python analysis_scripts/per_site_ci_polyp.py
```

### `cluster_bootstrap_external.py`
Reproduces the cross-modality scope analysis. Case-clustered bootstrap is used for BraTS2021, LiTS17, and PROMISE12; image-level bootstrap is used for ISIC2018 and BUSI, consistent with the manuscript.

```bash
python analysis_scripts/cluster_bootstrap_external.py --target failure70
```

### `summarize_robustness.py`
Prints the manuscript-facing robustness results from the included summary/bootstrap artifacts.

```bash
python analysis_scripts/summarize_robustness.py
```

### `reproduce_sensitivity_table.py`
Prints the one-factor-at-a-time sensitivity summary and paired-bootstrap comparisons against the fixed reference configuration.

```bash
python analysis_scripts/reproduce_sensitivity_table.py
```
