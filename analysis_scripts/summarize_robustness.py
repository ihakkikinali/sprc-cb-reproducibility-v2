"""Print compact manuscript-facing robustness summaries from included artifacts."""
from pathlib import Path
import pandas as pd
B=Path('results/robustness')

box=pd.read_csv(B/'polyp_box_noise_summary.csv')
sel=box[(box['set']=='pooled_heldout') & (box['target']=='failure') & (box['method'].isin(['SPRC-CB','SAM IoU min'])) & (box['noise'].isin([0.1,0.2]))]
print('Box-localisation noise (pooled held-out, Dice < 0.70)')
print(sel[['noise','method','n','pos','auprc','auroc','diff_vs_sam_auprc','diff_ci_low','diff_ci_high','diff_p']].to_string(index=False))

cross=pd.read_csv(B/'polyp_cross_backbone_summary.csv')
sel=cross[(cross['set']=='pooled_heldout') & (cross['target']=='failure') & (cross['model']=='MedSAM') & (cross['method'].isin(['SPRC-CB','SAM IoU min']))]
print('\nMedSAM cross-model check (pooled held-out, Dice < 0.70)')
print(sel[['method','n','pos','auprc','auroc','diff_vs_sam_auprc','diff_ci_low','diff_ci_high','diff_p']].to_string(index=False))

det=pd.read_csv(B/'polyp_detector_prompt_summary.csv')
sel=det[(det['prompt_source']=='detector') & (det['target']=='failure70') & (det['score'].isin(['SPRC-CB','Confidence']))]
print('\nDetector-derived prompts (Dice < 0.70)')
print(sel[['score','n','failures','failure_rate','AUPRC','AUROC','mean_dice','mean_base_box_iou_gt']].to_string(index=False))
