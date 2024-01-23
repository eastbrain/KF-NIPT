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
def convert_reads(args):

  bam_aln    = pysam.AlignmentFile(args.bam, "rb") 
  idxstats   = bam_aln.get_index_statistics()

  keep_contigs="(?i)^chr"
  if keep_contigs is None:
        keep_contigs = "."

  #pattern = re.compile(keep_contigs)
  for i in idxstats: 
    contig          = i.contig    
    reference_len   = bam_aln.get_reference_length(contig)
    read_count      = i.mapped
    length_coverage = read_count / reference_len
    #if pattern.match(contig):
    if not '_' in contig: 
      print(contig,"\t",read_count,"\t",reference_len,"\t",length_coverage)

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
