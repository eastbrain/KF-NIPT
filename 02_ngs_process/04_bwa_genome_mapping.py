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
def run_bwa(args):
  bwa = "../bin/bwa/0.7.17/bin/bwa"
  sam = args.sample + ".bwa.out.sam"
  cmd = ""
  if args.fastq_R2 is not None:
    cmd = bwa + " mem -t 1 -R " + "\"@RG\\tID:"+args.sample+"\\tSM:"+args.sample+"\\tPL:ILLUMINA\"" + " " + args.db + " " + args.fastq_R1 + " " + args.fastq_R2 + " > " + sam
  else:
    cmd = bwa + " mem -t 1 -R " + "\"@RG\\tID:"+args.sample+"\\tSM:"+args.sample+"\\tPL:ILLUMINA\"" + " " + args.db + " " + args.fastq_R1 + " > " + sam
  os.system(cmd)
######################################################################################################
def main():
  parser   = argparse.ArgumentParser(description='NIPT Welcoming version (sckacker@ajou.ac.kr,gtphrase@eonelab.co.kr)')
  parser.add_argument('-v','--version', action='version', version='KF-NIPT 0.01')
  optional = parser._action_groups.pop()
  required = parser.add_argument_group('required arguments')
  parser._action_groups.append(optional)
  required.add_argument('-r1',dest="fastq_R1",help="sample_R1.fastq(.gz)", required=True)
  optional.add_argument('-r2',dest="fastq_R2",help="sample_R2.fastq(.gz)")
  required.add_argument('-index',dest="db",help="bwa index db(human genome)", required=True)
  required.add_argument('-sample',dest="sample",help="sample name", required=True)
  args = parser.parse_args()
  run_bwa(args)
if __name__ == '__main__':
    main()

