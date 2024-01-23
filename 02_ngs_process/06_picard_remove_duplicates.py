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
def run_rmdup(args):
  bam = args.bam
  java = "../bin/java/openjdk-18.0.2/bin/java"
  picard = "../bin/picard/2.27.5/picard.jar" 
  cmd = java + " -Xmx30g -jar " + picard + " MarkDuplicates -I " + bam + " -O " + bam + ".rmdup.bam -M " + bam +".rmdup.metrics.txt -REMOVE_DUPLICATES true  -CREATE_INDEX true -VALIDATION_STRINGENCY STRICT" 
  os.system(cmd)
######################################################################################################
def main():
  parser   = argparse.ArgumentParser(description='NIPT Welcoming version (sckacker@ajou.ac.kr,gtphrase@eonelab.co.kr)')
  parser.add_argument('-v','--version', action='version', version='KF-NIPT 0.01')
  optional = parser._action_groups.pop()
  required = parser.add_argument_group('required arguments')
  parser._action_groups.append(optional)
  required.add_argument('-bam',dest="bam",help="bam", required=True)
  args = parser.parse_args()
  run_rmdup(args)
if __name__ == '__main__':
    main()

