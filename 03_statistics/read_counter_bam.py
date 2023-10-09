#!/usr/bin/env python3
import os
import sys
import argparse
import numpy as np
import pysam
#import pysamstats
import logging
import warnings
import re

#####################################################################################################
def main():
  warnings.filterwarnings('ignore')

  parser = argparse.ArgumentParser(description='NIPT Welcoming version (gtphrase@eonelab.co.kr)')
  parser.add_argument('bam' ,type=str,help='sorted.filtered.markdup.rmdup.bam')

  args = parser.parse_args(sys.argv[1:])
  bam_file = args.bam

  convert_reads(args)

if __name__ == '__main__':
    main()
