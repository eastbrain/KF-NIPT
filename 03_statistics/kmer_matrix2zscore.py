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


merged_df.to_csv('zscore_2023_07_01.tsv', sep='\t', index=True)
print(merged_df)
