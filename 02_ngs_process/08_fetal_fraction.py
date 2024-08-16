#!/usr/bin/env python3
import os
import sys
import argparse
import numpy as np
import pysam
import logging
import warnings
import subprocess as subp
from collections import defaultdict
#logging.basicConfig(level=logging.DEBUG)

#####################################################################################################
def calculate_FF(args):
  bam = args.bam
  seqFF_bam_ver = "../bin/SeqFF_bam/seqff_bam.r"
  cmd = "Rscript " + seqFF_bam_ver + " " + bam + " "  + bam + ".ff.out.txt"
  os.system("ln -s ../bin/SeqFF_bam/SupplementalFile1.RData .")
  os.system("ln -s ../bin/SeqFF_bam/SupplementalTable2.csv .")
  os.system(cmd)
  os.system("rm -rf SupplementalFile1.RData")
  os.system("rm -rf SupplementalTable2.csv")
######################################################################################################
def main():
  parser   = argparse.ArgumentParser(description='NIPT Welcoming version (sckacker@ajou.ac.kr,gtphrase@eonelab.co.kr)')
  parser.add_argument('-v','--version', action='version', version='KF-NIPT 0.01')
  optional = parser._action_groups.pop()
  required = parser.add_argument_group('required arguments')
  parser._action_groups.append(optional)
  required.add_argument('-bam',dest="bam",help="bam", required=True)
  args = parser.parse_args()
  calculate_FF(args)
if __name__ == '__main__':
    main()

