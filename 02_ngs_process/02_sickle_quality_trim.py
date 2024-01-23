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
def run_sickle(args):
  sickle="../bin/sickle/v1.33/bin/sickle"
  r1_out = args.fastq_R1 + "_1_trimmed.fastq"
  single = "single.fastq"
  cmd = ""
  if args.fastq_R2 is not None:
    r2_out = args.fastq_R2 + "_2_trimmed.fastq"
    cmd = sickle + " pe -t sanger -q 20 -f " + args.fastq_R1 + " -r " + args.fastq_R2 + " -o " + r1_out + " -p " + r2_out + " -s " + single  
  else:
    cmd = sickle + " se -t sanger -q 20 -f " + args.fastq_R1 + " -o " + r1_out 
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
  run_sickle(args)
if __name__ == '__main__':
    main()

