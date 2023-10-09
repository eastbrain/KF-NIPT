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
    #if "_" not in contig and "chrM" != contig and "chrX" !=contig and "chrY" !=contig:
    if "_" not in contig:
      reference_len   = bam_aln.get_reference_length(contig)
      read_count      = i.mapped
      length_coverage = read_count / reference_len
      reads           = bam_aln.fetch(contig,1,reference_len)
      total_bases = 0
      gc_bases    = 0
      for read in reads:
         seq = read.query_sequence.lower()
         total_bases += len(seq)
         gc_bases += len([x for x in seq if x == 'c' or x == 'g'])
      #gc_percent = '{0:.2f}%'.format(float(gc_bases)/total_bases * 100)
      gc_percent = '{0:.6f}'.format(float(gc_bases)/total_bases)
      print(contig+"\t"+str(gc_percent))
  bam_aln.close()

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
####################################################################################################
def main():
  warnings.filterwarnings('ignore')

  parser = argparse.ArgumentParser(description='NIPT Welcoming version (gtphrase@eonelab.co.kr, sckacker@ajou.ac.kr)')
  parser.add_argument('bam' ,type=str,help='sample.bam')

  args = parser.parse_args(sys.argv[1:])
  bam_file = args.bam

  convert_reads(args)

if __name__ == '__main__':
    main()
