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
def run_fastqc(args):
  fastqc="../bin/FastQC/v0.12.1/bin/fastqc"
  fqs=""
  for arg in vars(args):
    fq = getattr(args, arg)
    if fq is not None:
      fqs += fq + " "
  cmd = fastqc + " " + fqs + " -o ./ "
  os.system(cmd)
#####################################################################################################
def main():

  parser   = argparse.ArgumentParser(description='NIPT Welcoming version (sckacker@ajou.ac.kr,gtphrase@eonelab.co.kr)')
  parser.add_argument('-v','--version', action='version', version='KF-NIPT 0.01')
  optional = parser._action_groups.pop()
  required = parser.add_argument_group('required arguments')
  parser._action_groups.append(optional)
  required.add_argument('-r1',dest="fastq_R1",help="sample_R1.fastq(.gz)", required=True)
  optional.add_argument('-r2',dest="fastq_R2",help="sample_R2.fastq(.gz)")
  args = parser.parse_args()
  run_fastqc(args)

if __name__ == '__main__':
    main()

