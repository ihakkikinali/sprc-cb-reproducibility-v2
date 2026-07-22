# Data Manifests

Attribution and access information for every dataset used in the experiments.
No dataset files are included in this repository — the URLs below point to
the original public sources.

## Polyp benchmarks (main experiments)

| Dataset | Access URL | Reference |
|---|---|---|
| Kvasir-SEG (~1000 images) | https://datasets.simula.no/kvasir-seg/ | Jha et al., MMM 2020 |
| CVC-ClinicDB (612 images) | https://polyp.grand-challenge.org/CVCClinicDB/ | Bernal et al., CMIG 2015 |
| CVC-ColonDB (300 images) | https://polyp.grand-challenge.org/CVCColonDB/ | Tajbakhsh et al., TMI 2015 |
| ETIS-Larib (196 images) | https://polyp.grand-challenge.org/ETISLarib/ | Silva et al., IJCARS 2014 |

The main experiments sample 150 images per site (seed 42), yielding the 600-image
pooled cohort. Image identifiers used are recorded implicitly in the
`image_path` column of `results/polyp_main/sprc_cb_scored_results.csv`.

## External modalities (scope analysis)

| Dataset | Access URL | Reference |
|---|---|---|
| BraTS2021 (brain tumour MRI) | https://www.kaggle.com/datasets/dschettler8845/brats-2021-task1 | Bakas et al., Sci. Data 2017 |
| LiTS17 (liver tumour CT) | https://competitions.codalab.org/competitions/17094 | Bilic et al., MedIA 2023 |
| ISIC2018 Task 1 (dermoscopy) | https://challenge.isic-archive.com/data/#2018 | Codella et al., ISBI 2018 |
| PROMISE12 (prostate MRI) | https://promise12.grand-challenge.org/ | Litjens et al., MedIA 2014 |
| BUSI (breast ultrasound) | https://scholar.cu.edu.eg/?q=afahmy/pages/dataset | Al-Dhabyani et al., Data Brief 2020 |

For each external dataset, 200 images (100 calibration, 100 held-out test)
are drawn at seed 42. Per-dataset preprocessing, case-identifier handling,
and split construction are documented in Supplementary Material S2 of the
submitted revision; the scored files retain the split/resampling identifiers
used by the analysis scripts.

## Segmentation backbones

- **SAM ViT-B** — https://github.com/facebookresearch/segment-anything
  (checkpoint: `sam_vit_b_01ec64.pth`, ~375 MB)
- **MedSAM** — https://github.com/bowang-lab/MedSAM
  (checkpoint: `medsam_vit_b.pth`, ~375 MB)

Both are covered by the licences of their originating projects.

## Detector for the non-oracle prompt experiment

The YOLOv8s polyp detector used in the detector-derived prompt experiment
(Supplementary Material S1, Section S1.5) is trained only on Kvasir-SEG source-domain
images. Training / inference configuration and per-image bounding-box
predictions are recorded in `../results/robustness/polyp_detector_prompt_*`.
