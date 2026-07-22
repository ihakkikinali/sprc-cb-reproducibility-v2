"""Print the OFAT sensitivity summary and paired-bootstrap comparisons."""
from pathlib import Path
import pandas as pd
BASE=Path('results/sensitivity')
summary=pd.read_csv(BASE/'sensitivity_summary.csv')
boot=pd.read_csv(BASE/'sensitivity_bootstrap.csv')
print('OFAT sensitivity — Dice < 0.70')
print(summary[summary.target=='failure70'][['config','axis','value','n','failures','SPRC_CB_AUPRC','Conf_AUPRC','delta_vs_conf']].to_string(index=False))
print('\nPaired bootstrap: alternative minus default — Dice < 0.70')
print(boot[boot.target=='failure70'][['config','axis','value','alt_minus_default_mean','ci_lo','ci_hi','p']].to_string(index=False))
