#!/usr/bin/env python3
import os
import sys
import argparse
import numpy as np
import pysam
import logging
import warnings

import khmer

from collections import defaultdict

from Bio.Seq import Seq

#logging.basicConfig(level=logging.DEBUG)


#####################################################################################################
def parsing_argument():
  parser = argparse.ArgumentParser(
    description="NIPT Welcoming version",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
  )

  parser.add_argument(
    'title',
    metavar='str',
    type=str,
    help='Program title'
  )
  return parser.parse_args()
#####################################################################################################
def main():
  warnings.filterwarnings('ignore')

  parser = argparse.ArgumentParser(description='NIPT Welcoming version (gtphrase@eonelab.co.kr)')
  parser.add_argument('bam' ,type=str,help='sorted.bam')
  parser.add_argument('kmer',type=int,help='25, 50, 75...')

  args = parser.parse_args(sys.argv[1:])
  #logging.debug('args are: {}'.format(args))

  bam_file = args.bam
  kmer     = args.kmer

  convert_kmer(args)

if __name__ == '__main__':
    main()
