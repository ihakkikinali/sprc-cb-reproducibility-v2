"""Per-site paired-bootstrap AUPRC confidence intervals for the four polyp benchmarks."""
import argparse
import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score

STAGE_TO_SITE = {
    "stage1_id": "Kvasir-SEG",
    "stage2_cross_site": "CVC-ClinicDB",
    "stage3_external_polyp": "CVC-ColonDB",
    "stage4_hard_external_polyp": "ETIS-Larib",
}

def bootstrap_paired(y, a, b, n_boot=5000, seed=42):
    rng=np.random.default_rng(seed); n=len(y)
    ap_a=average_precision_score(y,a); ap_b=average_precision_score(y,b); delta=ap_a-ap_b
    aa=[]; bb=[]; dd=[]
    for _ in range(n_boot):
        idx=rng.integers(0,n,size=n); yy=y[idx]
        if yy.sum()==0 or yy.sum()==len(yy): continue
        va=average_precision_score(yy,a[idx]); vb=average_precision_score(yy,b[idx])
        aa.append(va); bb.append(vb); dd.append(va-vb)
    aa=np.asarray(aa); bb=np.asarray(bb); dd=np.asarray(dd)
    p=min(2*((dd<=0).mean() if delta>=0 else (dd>=0).mean()),1.0)
    return dict(sprc=ap_a,sprc_lo=np.percentile(aa,2.5),sprc_hi=np.percentile(aa,97.5),
                conf=ap_b,conf_lo=np.percentile(bb,2.5),conf_hi=np.percentile(bb,97.5),
                delta=delta,delta_lo=np.percentile(dd,2.5),delta_hi=np.percentile(dd,97.5),p=p)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input',default='results/polyp_main/sprc_cb_scored_results.csv'); ap.add_argument('--out',default='per_site_ci_output.csv'); ap.add_argument('--n-boot',type=int,default=5000); args=ap.parse_args()
    df=pd.read_csv(args.input); df['site']=df['stage'].map(STAGE_TO_SITE); rows=[]
    for site in STAGE_TO_SITE.values():
        sub=df[df.site==site]; y=sub.failure70.astype(int).to_numpy(); a=sub.sprc_cb_score.to_numpy(); b=sub.sam_confidence_risk.to_numpy(); r=bootstrap_paired(y,a,b,args.n_boot)
        print(f"{site}: n={len(sub)}, failures={int(y.sum())}, SPRC={r['sprc']:.3f} [{r['sprc_lo']:.3f},{r['sprc_hi']:.3f}], Conf={r['conf']:.3f} [{r['conf_lo']:.3f},{r['conf_hi']:.3f}], delta={r['delta']:+.3f} [{r['delta_lo']:+.3f},{r['delta_hi']:+.3f}], p={r['p']:.3f}")
        rows.append(dict(site=site,n=len(sub),failures=int(y.sum()),**r))
    pd.DataFrame(rows).to_csv(args.out,index=False)
    print(f"Saved {args.out}")
if __name__=='__main__': main()
