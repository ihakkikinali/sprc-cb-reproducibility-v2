# Results

This directory contains the fixed scored outputs and statistical artifacts corresponding to the submitted manuscript.

## `polyp_main/`

`sprc_cb_scored_results.csv` contains 600 images from Kvasir-SEG, CVC-ClinicDB, CVC-ColonDB, and ETIS-Larib. Key fields:

- `base_dice`, `base_iou`
- `failure70`, `failure80`, `severe50`
- `sprc_cb_score`
- `sprc_pp_r_score`
- `sam_confidence_risk`
- `mask_iou_disagreement`
- `linear_sprc_score`

This file reproduces Table 1, Supplementary Fig. S1, and Supplementary Table S1.

## `external/`

Ten scored CSVs (five datasets × two backbones), each containing calibration/test split information, explicit case/resampling identifiers, failure targets, SPRC-CB risk, and confidence risk.

These files reproduce the common Dice < 0.70 cross-modality scope analysis in Table 3 using `cluster_bootstrap_external.py`.

## `robustness/`

Manuscript-facing summary and bootstrap artifacts for:

- synthetic box-localisation noise;
- detector-derived prompts;
- SAM ViT-B / MedSAM cross-model evaluation.

Use `analysis_scripts/summarize_robustness.py` for a compact report.

## `sensitivity/`

One-factor-at-a-time sensitivity artifacts:

- `sensitivity_summary.csv`
- `sensitivity_summary_pivot.csv`
- `sensitivity_delta_pivot.csv`
- `sensitivity_bootstrap.csv`
- `sensitivity_kvasir_index.csv`

Use `analysis_scripts/reproduce_sensitivity_table.py` to print the fixed-reference comparisons supporting Supplementary Table S8.
