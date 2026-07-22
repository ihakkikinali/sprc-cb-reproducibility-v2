"""Reproduce pooled failure-screening metrics reported in the main manuscript."""
import argparse
import pandas as pd
from sklearn.metrics import average_precision_score, roc_auc_score

TARGETS = ["failure70", "failure80", "severe50"]
SCORES = [
    ("SPRC-CB", "sprc_cb_score"),
    ("SPRC++-R", "sprc_pp_r_score"),
    ("SAM confidence", "sam_confidence_risk"),
    ("Mask IoU disagreement", "mask_iou_disagreement"),
    ("Linear SPRC", "linear_sprc_score"),
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="results/polyp_main/sprc_cb_scored_results.csv")
    args = ap.parse_args()
    df = pd.read_csv(args.input)
    print(f"Loaded {len(df)} scored images")
    for target in TARGETS:
        y = df[target].astype(int).to_numpy()
        print(f"\n{target}: failures={int(y.sum())}/{len(y)}")
        print(f"{'Method':<24} {'AUPRC':>8} {'AUROC':>8}")
        print("-"*42)
        for label, col in SCORES:
            s = df[col].astype(float).to_numpy()
            print(f"{label:<24} {average_precision_score(y,s):>8.3f} {roc_auc_score(y,s):>8.3f}")

if __name__ == "__main__":
    main()
