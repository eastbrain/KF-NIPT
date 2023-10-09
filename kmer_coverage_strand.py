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
from numpy import median

from Bio.Seq import Seq

#logging.basicConfig(level=logging.DEBUG)

#####################################################################################################
def convert_kmer(args):

  tablesize = int(1e8)

  bins_per_chr  = dict()
  bins_per_chr2 = dict()
  for chr in range(1, 25):
     bins_per_chr[str(chr)]  = None
     bins_per_chr2[str(chr)] = None

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
     htable   = khmer.Counttable(k, tablesize, 4) 
     chr_len  = reads_file.get_reference_length(chr)
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
     bins_per_chr[chr_name]  = str(counts) + "\t" + str(chr_len)
     bins_per_chr2[chr_name] = str(counts) + "\t" + str(chr_len)
  
  cov_lst=[]
  for chr in chromosomes:
     chr_name = chr
     if chr_name[:3].lower() == 'chr':
         chr_name = chr_name[3:]
     if chr_name not in bins_per_chr and chr_name != 'X' and chr_name != 'Y':
         continue

     if chr_name == 'X': chr_name = '23'
     if chr_name == 'Y': chr_name = '24'
     if chr_name !='23' and chr_name !='24':
        chr_kmer_count  = bins_per_chr[chr_name].split("\t")[0]
        chr_len         = bins_per_chr[chr_name].split("\t")[1]
        length_coverage = float(chr_kmer_count) / float(chr_len) 
        cov_lst.append(float(length_coverage))
        #print(chr,"\t",chr_kmer_count)

  for chr2 in chromosomes:
     chr_name2 = chr2
     if chr_name2[:3].lower() == 'chr':
         chr_name2 = chr_name2[3:]
     if chr_name2 not in bins_per_chr and chr_name2 != 'X' and chr_name2 != 'Y':
         continue

     if chr_name2 == 'X': chr_name2 = '23'
     if chr_name2 == 'Y': chr_name2 = '24'
     if chr_name2 !='23' and chr_name2 !='24':
        chr_kmer_count2  = bins_per_chr2[chr_name2].split("\t")[0]
        chr_len2         = bins_per_chr2[chr_name2].split("\t")[1]
        med_len_cov      = median(cov_lst)
        length_coverage2 = (float(chr_kmer_count2) / float(chr_len2)) / med_len_cov
        #print(chr_name2,"\t",length_coverage2)
        print("chr" + chr_name2 + "\t" + str(length_coverage2))

  reads_file.close()


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
