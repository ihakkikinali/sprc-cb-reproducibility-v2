# SPRC-CB: Reproducibility Repository

This anonymised repository accompanies the manuscript

> **Structural Prompt-Response Consistency for Label-Free Failure Screening in Promptable Medical Segmentation**

and provides the fixed per-image scored outputs and analysis scripts used for the submitted manuscript. The package is designed to let reviewers reproduce the principal numerical results and statistical analyses directly, without requiring GPU access, large segmentation checkpoints, or dataset downloads.

## Review-package scope

The review package focuses on **deterministic analysis reproducibility**. It includes:

- the canonical 600-image polyp scored output used for the pooled and per-site analyses;
- ten cross-modality scored files (five datasets × two backbones) used for the common Dice < 0.70 scope analysis;
- robustness summary and bootstrap artifacts for box noise, detector-derived prompts, and the MedSAM cross-model check;
- sensitivity summary and paired-bootstrap artifacts for the one-factor-at-a-time design analysis;
- standalone scripts for the pooled main table, per-site confidence intervals, external case-clustered bootstrap, robustness summaries, and sensitivity summaries.

A consolidated set of end-to-end inference notebooks, including environment-specific public-dataset mount and checkpoint setup, will be added to the archival public release upon acceptance. The notebooks are not required to reproduce the manuscript statistics provided in this review package.

---

## Repository layout

```text
sprc-cb-reproducibility/
├── README.md
├── LICENSE
├── requirements.txt
├── analysis_scripts/
│   ├── reproduce_main_table.py
│   ├── per_site_ci_polyp.py
│   ├── cluster_bootstrap_external.py
│   ├── summarize_robustness.py
│   ├── reproduce_sensitivity_table.py
│   └── README.md
├── results/
│   ├── polyp_main/
│   ├── external/
│   ├── robustness/
│   ├── sensitivity/
│   └── README.md
├── notebooks/
│   └── README.md
└── data_manifests/
    └── README.md
```

---

## Quick start

Install the lightweight analysis dependencies:

```bash
pip install -r requirements.txt
```

### Main pooled results (Table 1 / Supplementary Fig. S1)

```bash
python analysis_scripts/reproduce_main_table.py
```

Reference result at Dice < 0.70:

| Score | AUPRC | AUROC |
|---|---:|---:|
| SPRC-CB | 0.552 | 0.931 |
| SAM confidence | 0.379 | 0.916 |

### Per-site bootstrap confidence intervals (Supplementary Table S1)

```bash
python analysis_scripts/per_site_ci_polyp.py
```

### Cross-modality scope analysis (Table 3)

```bash
python analysis_scripts/cluster_bootstrap_external.py --target failure70
```

### Robustness summaries

```bash
python analysis_scripts/summarize_robustness.py
```

### Sensitivity summary (Supplementary Table S8 support)

```bash
python analysis_scripts/reproduce_sensitivity_table.py
```

---

## Scored outputs

The CSV files in `results/` are the fixed analysis artifacts corresponding to the submitted manuscript. The principal score columns are named explicitly (`sprc_cb_score` and `sam_confidence_risk`) so that the statistical analyses can be reproduced without dependence on environment-specific inference code.

The canonical polyp file additionally includes the comparator scores used in the pooled evaluation: SPRC++-R, mask-IoU disagreement, and linear SPRC.

---

## Datasets

All datasets used in the study are publicly available under their original licences. No dataset images, masks, or model checkpoints are redistributed here. Dataset attribution and source information are listed in `data_manifests/README.md`.

## Anonymisation

This repository contains no author-identifying metadata or personal credentials and is intended for double-anonymous peer review.

## Citation

A citation record will be added to the archival public release upon acceptance.

## License

MIT (see `LICENSE`).
