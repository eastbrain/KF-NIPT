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
def run_repair(args):
  repair = "../bin/BBMap/39.06/bbmap/repair.sh"
  r1_out = args.fastq_R1 + "_1_repair.fq.gz"
  r2_out = args.fastq_R2 + "_2_repair.fq.gz"
  cmd = repair + " -Xmx16g  in=" + args.fastq_R1 + " in2=" + args.fastq_R2 + " -out=" + r1_out + " -out2=" + r2_out
  os.system(cmd)
#####################################################################################################
def main():
  parser   = argparse.ArgumentParser(description='NIPT Welcoming version (sckacker@ajou.ac.kr,gtphrase@eonelab.co.kr)')
  parser.add_argument('-v','--version', action='version', version='KF-NIPT 0.01')
  optional = parser._action_groups.pop()
  required = parser.add_argument_group('required arguments')
  parser._action_groups.append(optional)
  required.add_argument('-r1',dest="fastq_R1",help="sample_R1.fastq(.gz)", required=True)
  required.add_argument('-r2',dest="fastq_R2",help="sample_R2.fastq(.gz)", required=True)
  args = parser.parse_args()
  run_repair(args)
if __name__ == '__main__':
    main()

