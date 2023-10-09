#!/usr/bin/env python3
import os
import sys
import argparse
import numpy as np
import pandas as pd
import pysam
import logging
import warnings


#####################################################################################################
def calculate_zscore(args):
  cnr_file  = args.cnr
  sample_nm = os.path.basename(cnr_file).split(".")[0]
  cnr = pd.read_csv(cnr_file,sep="\t")
  cnr = cnr[cnr['chromosome'] == 'chr21']

  sd = np.sqrt(1 - cnr['weight'])
  zscore =  cnr['log2'] / sd
  print(sample_nm,zscore.max())
#####################################################################################################
def main():
  warnings.filterwarnings('ignore')

  parser = argparse.ArgumentParser(description='NIPT Welcoming version (gtphrase@eonelab.co.kr)')
  parser.add_argument('cnr' ,type=str,help='cnvkit output cnr')

  args = parser.parse_args(sys.argv[1:])
  calculate_zscore(args)

if __name__ == '__main__':
    main()
