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

file_pattern = '*.txt'  #

merged_df = pd.DataFrame()

file_paths = glob.glob(file_pattern)

merged_df.to_csv('zscore_2023_06_26.tsv', sep='\t', index=True)
print(merged_df)
