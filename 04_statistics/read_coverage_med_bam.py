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
import statistics as st

from numpy import median

def get_median_v2(data):
    #data = sorted(data)
 
    centerIndex = len(data)//2
    return (data[centerIndex ] + data[-centerIndex - 1])/2

#####################################################################################################
def convert_reads(args):

  bam_aln    = pysam.AlignmentFile(args.bam, "rb") 
  idxstats   = bam_aln.get_index_statistics()

  keep_contigs="(?i)^chr"
  if keep_contigs is None:
        keep_contigs = "."

  #pattern = re.compile(keep_contigs)
  cov_lst=[]
  for i in idxstats: 
    contig = i.contig    
    if not '_' in contig and contig !="chrX" and  contig !="chrY" and contig !="chrM":
      reference_len   = bam_aln.get_reference_length(contig)
      read_count      = i.mapped
      length_coverage = float(read_count) / float(reference_len)
      cov_lst.append(float(length_coverage))

  for j in idxstats:
    contig2 = j.contig
    if not '_' in contig2 and contig2 !="chrX" and  contig2 !="chrY" and contig2 !="chrM":
      reference_len2   = bam_aln.get_reference_length(contig2)
      read_count2      = j.mapped
      med_len_cov      = median(cov_lst)
      length_coverage2 = (read_count2 / reference_len2) / med_len_cov
      print(contig2,"\t",length_coverage2)

  bam_aln.close()

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
  parser.add_argument('bam' ,type=str,help='sorted.filtered.markdup.rmdup.bam')

  args = parser.parse_args(sys.argv[1:])
  bam_file = args.bam

  convert_reads(args)

if __name__ == '__main__':
    main()
