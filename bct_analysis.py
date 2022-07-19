"""Analysis of clusters"""

import pandas as pd
from scipy.stats import chi2_contingency

MIN_CLUSTER_SIZE = 100
TOP_SIX = False

def chisq_cid(df, c, c2="cluster_id"):
    groupsizes = df.groupby([c, c2]).size()
    # if a cluster has no values in a group it will be NaN instead of 0
    ctsum = groupsizes.unstack(c).fillna(0)
    chi2_res = chi2_contingency(ctsum)
    p = chi2_res[1]
    diff = ctsum - chi2_res[-1]
    return p, diff

cat_cols = cat_cols = [
    "gender",
    "uniwords",
    "climate",
    "stage",
    "bct",
    "family",
    "north",
    "east",
    "stage_transition",
    "tropical",
    "farming",
    "palm_oil_production",
    "agriculture",
    "hunting",
    "fishing",
    "livestock",
    "unknown",
    "gathering",
    "nomadic",
    "mercantilism",
]

df = pd.read_excel('speaker.xlsx')
big_cluster_labels = df['cluster_id'].value_counts()[df['cluster_id'].value_counts() >= MIN_CLUSTER_SIZE].index
if TOP_SIX:
    big_cluster_labels = df['cluster_id'].value_counts()[:6].index
big_cl = df[df['cluster_id'].isin(big_cluster_labels)]

results = {}
for c in cat_cols:
    print(f"column: {c}")
    p, diff = chisq_cid(big_cl, c)
    print(f"p-value = {p}")
    results[c] = diff

for k, v in results.items():
    print(f"column: {k}")
    print(f"diff:\n{v}")
    v.to_csv(k + '_diff.csv')
