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

file_pattern = '*.txt' 

merged_df  = pd.DataFrame()
merged_df1 = pd.DataFrame()
merged_df2 = pd.DataFrame()
merged_df3 = pd.DataFrame()

file_paths = glob.glob(file_pattern)

for file_path in file_paths:
    file_name = "s_" + os.path.basename(file_path).split('.')[0]
    df = pd.read_csv(file_path, names = ['chr',file_name], sep="\t")
    if merged_df.empty:
        merged_df = df
    else:
        merged_df = merged_df.merge(df, on='chr', how='outer')
merged_df1 = merged_df.set_index('chr')
merged_df2 = merged_df.set_index('chr')
merged_df3 = merged_df.set_index('chr')

for i in range(1, 23):
  #column  = merged_df1.loc['chr'+str(i)+" "]
  column  = merged_df1.loc['chr'+str(i)]
  median  = stat.median(column.to_list())
  #merged_df2.loc['chr'+str(i)+" "] = merged_df1.loc['chr'+str(i)+" "].apply(lambda x : abs(x-median))
  merged_df2.loc['chr'+str(i)] = merged_df1.loc['chr'+str(i)].apply(lambda x : abs(x-median))

for j in range(1, 23):
  column1  = merged_df1.loc['chr'+str(j)]
  column2  = merged_df2.loc['chr'+str(j)]

  median1  = stat.median(column1.to_list())
  median2  = stat.median(column2.to_list())
  merged_df3.loc['chr'+str(j)] = merged_df1.loc['chr'+str(j)].apply(lambda x : (0.6745*(x-median1))/median2)

merged_df3.to_csv('modified_zscore_2023_07_01.tsv', sep='\t', index=True)
print(merged_df3)
