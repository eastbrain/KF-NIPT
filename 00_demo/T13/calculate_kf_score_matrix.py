import os
import sys
import glob
import numpy as np
import numpy as np
import pandas as pd
import seaborn as sns
import statistics as stat

import argparse
import warnings

from statistics import mean
from statistics import stdev
from scipy.stats import zscore
from astropy.stats import median_absolute_deviation

#####################################################################################################
file_pattern = '*.txt'
ff_dic = {}
def memPut_ff(ff_dir):
   file_paths = glob.glob(ff_dir+"/"+file_pattern)
   for file_path in file_paths:
      sample_id = file_path.split('/')[1].split('.')[0]
      f = open(file_path, 'r')
      lines = f.readlines()
      for line in lines:
       line  = line.strip()
       tools = line.split('\t')[0]
       if tools == 'SeqFF':
         ff = line.split('\t')[1]
         ff_dic[sample_id] = ff
      f.close()
#####################################################################################################
def calculate_kf_score(args):
  kmer_dir   = args.kmer_dir
  ff_dir     = args.ff_dir
  matrix_out = args.matrix
  memPut_ff(ff_dir)

  merged_df  = pd.DataFrame()
  merged_df1 = pd.DataFrame()
  merged_df2 = pd.DataFrame()
  merged_df3 = pd.DataFrame()

  file_paths = glob.glob(kmer_dir+"/"+file_pattern)

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
    column    = merged_df1.loc['chr'+str(i)]
    median    = stat.median(column.to_list())
    merged_df2.loc['chr'+str(i)] = merged_df1.loc['chr'+str(i)].apply(lambda x : abs(x-median))

  for j in range(1, 23):
    column1  = merged_df1.loc['chr'+str(j)]
    column2  = merged_df2.loc['chr'+str(j)]
    for col in column2.keys():
      sample_id2 = col.split('_')[1]
      sample_ff2 = ff_dic[sample_id2]
      kmz_score = column2[col]
      #print(kmz_score,sample_ff2)
      kf_score  = float(kmz_score) * float(sample_ff2)
      #print(sample_id2,sample_ff2,'chr'+str(j),kmz_score,kf_score)
      column2.loc['chr'+str(j)] = kf_score

    median1  = stat.median(column1.to_list())
    median2  = stat.median(column2.to_list())
    merged_df3.loc['chr'+str(j)] = merged_df1.loc['chr'+str(j)].apply(lambda x : (0.6745*(x-median1))/median2)

  merged_df3.to_csv(matrix_out, sep='\t', index=True)
  
#####################################################################################################
def main():
  warnings.filterwarnings('ignore')

  parser = argparse.ArgumentParser(description='NIPT Welcoming version (sckacker@ajou.ac.kr, gtphrase@eonelab.co.kr)')
  parser.add_argument('kmer_dir' ,type=str,help='K-mer_directory')
  parser.add_argument('ff_dir',type=str,help='fetal-fraction_directory')
  parser.add_argument('matrix',type=str,help='matrix.out.txt')

  args = parser.parse_args(sys.argv[1:])

  calculate_kf_score(args)

if __name__ == '__main__':
    main()
