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
def run_gccorrect(args):
  bam = args.bam
  computeGCBias = "~/anaconda3/bin/computeGCBias"
  correctGCBias = "~/anaconda3/bin/correctGCBias"
  cmd1 = computeGCBias + " -p 100 -l 101 -b " + bam  + " --effectiveGenomeSize 2864785220 -g ./ref/hg19.2bit --GCbiasFrequenciesFile " + bam + ".freq.txt"
  cmd2 = correctGCBias + " -p 100 -b " + bam + " --effectiveGenomeSize 2864785220 -g ./ref/hg19.2bit --GCbiasFrequenciesFile " + bam + ".freq.txt" + " -o " + bam + ".gc_corrected.bam"
  os.system(cmd1)
  os.system(cmd2)
######################################################################################################
def main():
  parser   = argparse.ArgumentParser(description='NIPT Welcoming version (sckacker@ajou.ac.kr,gtphrase@eonelab.co.kr)')
  parser.add_argument('-v','--version', action='version', version='KF-NIPT 0.01')
  optional = parser._action_groups.pop()
  required = parser.add_argument_group('required arguments')
  parser._action_groups.append(optional)
  required.add_argument('-bam',dest="bam",help="bam", required=True)
  args = parser.parse_args()
  run_gccorrect(args)
if __name__ == '__main__':
    main()

