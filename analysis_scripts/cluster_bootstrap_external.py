"""Case/image-level paired bootstrap for the cross-modality scope analysis."""
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score

FILES = {
    'BraTS2021': {'SAM ViT-B':'brats_scored_SAM_ViT_B.csv','MedSAM':'brats_scored_MedSAM.csv'},
    'LiTS17': {'SAM ViT-B':'lits_scored_SAM_ViT_B.csv','MedSAM':'lits_scored_MedSAM.csv'},
    'ISIC2018': {'SAM ViT-B':'isic_scored_SAM_ViT_B.csv','MedSAM':'isic_scored_MedSAM.csv'},
    'PROMISE12': {'SAM ViT-B':'promise_scored_SAM_ViT_B.csv','MedSAM':'promise_scored_MedSAM.csv'},
    'BUSI': {'SAM ViT-B':'busi_scored_SAM_ViT_B.csv','MedSAM':'busi_scored_MedSAM.csv'},
}

def boot(df,target,n_boot=5000,seed=42):
    y=df[target].astype(int).to_numpy(); a=df.sprc_cb_score.to_numpy(); b=df.sam_confidence_risk.to_numpy(); c=df.case_id.astype(str).to_numpy()
    ap_a=average_precision_score(y,a); ap_b=average_precision_score(y,b); delta=ap_a-ap_b
    uniq=np.unique(c); idxmap={u:np.where(c==u)[0] for u in uniq}; rng=np.random.default_rng(seed); diffs=[]
    for _ in range(n_boot):
        sampled=rng.choice(uniq,size=len(uniq),replace=True); idx=np.concatenate([idxmap[u] for u in sampled]); yy=y[idx]
        if yy.sum()==0 or yy.sum()==len(yy): continue
        diffs.append(average_precision_score(yy,a[idx])-average_precision_score(yy,b[idx]))
    diffs=np.asarray(diffs); lo,hi=np.percentile(diffs,[2.5,97.5]); p=min(2*((diffs<=0).mean() if delta>=0 else (diffs>=0).mean()),1.0)
    return ap_a,ap_b,delta,lo,hi,p

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--results-dir',default='results/external'); ap.add_argument('--target',default='failure70',choices=['failure70','failure80','severe50']); ap.add_argument('--n-boot',type=int,default=5000); ap.add_argument('--out',default='cluster_bootstrap_output.csv'); args=ap.parse_args()
    rows=[]
    for ds,cfg in FILES.items():
        for model,fname in cfg.items():
            d=pd.read_csv(Path(args.results_dir)/fname); d=d[d.split=='test'].copy(); nf=int(d[args.target].sum())
            if nf==0 or nf==len(d):
                r=dict(dataset=ds,backbone=model,n=len(d),cases=d.case_id.nunique(),failures=nf,sprc=np.nan,conf=np.nan,delta=np.nan,ci_lo=np.nan,ci_hi=np.nan,p=np.nan)
            else:
                a,b,delta,lo,hi,p=boot(d,args.target,args.n_boot)
                r=dict(dataset=ds,backbone=model,n=len(d),cases=d.case_id.nunique(),failures=nf,sprc=a,conf=b,delta=delta,ci_lo=lo,ci_hi=hi,p=p)
            rows.append(r)
            print(f"{ds:10s} {model:9s} fail={nf:3d}/{len(d)} SPRC={r['sprc'] if pd.notna(r['sprc']) else float('nan'):.3f} Conf={r['conf'] if pd.notna(r['conf']) else float('nan'):.3f} delta={r['delta'] if pd.notna(r['delta']) else float('nan'):+.3f} [{r['ci_lo'] if pd.notna(r['ci_lo']) else float('nan'):+.3f},{r['ci_hi'] if pd.notna(r['ci_hi']) else float('nan'):+.3f}] p={r['p'] if pd.notna(r['p']) else float('nan'):.3f}")
    pd.DataFrame(rows).to_csv(args.out,index=False); print(f"Saved {args.out}")
if __name__=='__main__': main()
