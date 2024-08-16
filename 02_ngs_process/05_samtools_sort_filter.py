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
def run_samtools(args):
  sam = args.sam
  samtools = "../bin/samtools/1.17/bin/samtools" 
  cmd1 = samtools + " view -@ 100 -bF 4 -q 20 " + sam +  " | " + samtools + " sort -o " + sam + ".F4.q20.sorted.bam"
  os.system(cmd1)
  cmd2 = samtools + " index -@ 100 " + sam + ".F4.q20.sorted.bam"
  os.system(cmd2)
######################################################################################################
def main():
  parser   = argparse.ArgumentParser(description='NIPT Welcoming version (sckacker@ajou.ac.kr,gtphrase@eonelab.co.kr)')
  parser.add_argument('-v','--version', action='version', version='KF-NIPT 0.01')
  optional = parser._action_groups.pop()
  required = parser.add_argument_group('required arguments')
  parser._action_groups.append(optional)
  required.add_argument('-sam',dest="sam",help="sam", required=True)
  args = parser.parse_args()
  run_samtools(args)
if __name__ == '__main__':
    main()

