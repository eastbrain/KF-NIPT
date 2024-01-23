import pandas as pd
import glob
import os
import seaborn as sns
import numpy as np
import statistics as stat

from scipy.stats import zscore
from astropy.stats import median_absolute_deviation
from statistics import mean 
from statistics import stdev

file_pattern = '*.txt'  # 실제 파일 경로 패턴으로 수정해야 합니다.

merged_df = pd.DataFrame()

file_paths = glob.glob(file_pattern)

for file_path in file_paths:
    file_name = "s_" + os.path.basename(file_path).split('.')[0]
    df = pd.read_csv(file_path, names = ['chr',file_name], sep="\t")
    if merged_df.empty:
        merged_df = df
    else:
        merged_df = merged_df.merge(df, on='chr', how='outer')
merged_df = merged_df.set_index('chr')

for i in range(1, 23):
  column  = merged_df.loc['chr'+str(i)+" "]
  average = stat.mean(column.to_list())
  stdev   = stat.stdev(column.to_list())
  merged_df.loc['chr'+str(i)+" "] = merged_df.loc['chr'+str(i)+" "].apply(lambda x : (x-average)/stdev)

merged_df.to_csv('zscore_2023_06_26.tsv', sep='\t', index=True)
print(merged_df)
