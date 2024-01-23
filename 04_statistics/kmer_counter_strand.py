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
def convert_kmer(args):

  tablesize = int(1e8)

  bins_per_chr = dict()
  for chr in range(1, 25):
     bins_per_chr[str(chr)] = None

  logging.info('Importing data ...')
  #logging.info('Starting kmer count') 

  kmer_counts = defaultdict(int)

  bam_file = args.bam
  k        = args.kmer

  reads_file  = pysam.AlignmentFile(bam_file, "rb") 
  kmer_counts = defaultdict(int)

  chromosomes = reads_file.references

  for chr in chromosomes:
     # k-mer matrix 생성
     htable = khmer.Counttable(k, tablesize, 4) 

     chr_name = chr
     if chr_name[:3].lower() == 'chr':
         chr_name = chr_name[3:]
     if chr_name not in bins_per_chr and chr_name != 'X' and chr_name != 'Y':
         continue

     if chr_name == 'X': chr_name = '23'
     if chr_name == 'Y': chr_name = '24' 

     kmer_counts = defaultdict(int)
     for read in reads_file.fetch(chr):
        seq = read.query_sequence
        is_reverse = read.is_reverse
        if is_reverse:
         seq = Seq(seq).reverse_complement()
        if seq != None:
          for i in range(len(seq) - k + 1):
             kmer = seq[i:i+int(k)]
             kmer_counts[kmer] += 1

     counts = 0
     for kmer, count in kmer_counts.items():
       counts += int(count)
     bins_per_chr[chr_name] = counts
  
  for chr in chromosomes:
     chr_name = chr
     if chr_name[:3].lower() == 'chr':
         chr_name = chr_name[3:]
     if chr_name not in bins_per_chr and chr_name != 'X' and chr_name != 'Y':
         continue

     if chr_name == 'X': chr_name = '23'
     if chr_name == 'Y': chr_name = '24'
     print(chr,"\t",bins_per_chr[chr_name])

  reads_file.close()


# 아규먼트 파싱 메소드 
#####################################################################################################
def parsing_argument():
  parser = argparse.ArgumentParser(
    description="NIPT Sensuous",
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

  parser = argparse.ArgumentParser(description='NIPT Sensuous (gtphrase@eonelab.co.kr)')
  parser.add_argument('bam' ,type=str,help='sorted.bam')
  parser.add_argument('kmer',type=int,help='25, 50, 75...')

  args = parser.parse_args(sys.argv[1:])
  #logging.debug('args are: {}'.format(args))

  bam_file = args.bam
  kmer     = args.kmer

  convert_kmer(args)

if __name__ == '__main__':
    main()
