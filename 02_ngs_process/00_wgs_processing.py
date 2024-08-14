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

fastqc    = "../02_ngs_process/01_fastqc_processing.py"
sickle    = "../02_ngs_process/02_sickle_quality_trim.py"
repair    = "../02_ngs_process/03_repair_fastq.py"
bwa       = "../02_ngs_process/04_bwa_genome_mapping.py"
samtools  = "../02_ngs_process/05_samtools_sort_filter.py"
picard    = "../02_ngs_process/06_picard_remove_duplicates.py"
deeptools = "../02_ngs_process/07_gc_correction.py"
seqff_bam = "../02_ngs_process/08_fetal_fraction.py"

#####################################################################################################
def run_main(args):
  cmd = ""
  sampleid = args.fastq_R1.split("_")[0]
  if args.fastq_R2 is not None:#paired-end
    #fastq QC
    cmd = fastqc + " -r1 " + args.fastq_R1 + " -r2 " + args.fastq_R2
    os.system(cmd)

    #fastq Quality fiter, Length filter
    cmd = sickle + " -r1 " + args.fastq_R1 + " -r2 " + args.fastq_R2
    os.system(cmd)

    #repairing fastq
    cmd = repair + " -r1 " + args.fastq_R1 + "_1_trimmed.fastq" + " -r2 " + args.fastq_R2 + "_2_trimmed.fastq"
    os.system(cmd)

    #genome alignment
    #sampleid = args.fastq_R1.split("_")[0]
    cmd = bwa + " -r1 " + args.fastq_R1 + "_1_trimmed.fastq" + "_1_repair.fq.gz" + " -r2 " + args.fastq_R2 + "_2_trimmed.fastq" + "_2_repair.fq.gz " + " -index ../ref/ucsc.hg19.fasta -sample " + sampleid 
    os.system(cmd)

    #convert sam to bam, filter bam, sort bam
    cmd = samtools + " -sam " + sampleid + ".bwa.out.sam"
    os.system(cmd)

    #remove duplication
    cmd = picard + " -bam " + sampleid + ".bwa.out.sam" + ".F4.q20.sorted.bam "
    os.system(cmd) 

    #gc correction
    cmd = deeptools + " -bam " + sampleid + ".bwa.out.sam" + ".F4.q20.sorted.bam" + ".rmdup.bam"
    os.system(cmd)

    #fetal fraction
    cmd = seqff_bam + " -bam " + sampleid + ".bwa.out.sam" + ".F4.q20.sorted.bam" + ".rmdup.bam" + ".gc_corrected.bam" 
    os.system(cmd)

  else:#single-end
    #cmd =  args.fastq_R1
    #fastq QC
    cmd = fastqc + " -r1 " + args.fastq_R1 
    os.system(cmd)

    #fastq Quality fiter, Length filter
    cmd = sickle + " -r1 " + args.fastq_R1
    os.system(cmd)

    #genome alignment
    #sampleid = args.fastq_R1.split("_")[0]
    cmd = bwa + " -r1 " + args.fastq_R1 + "_1_trimmed.fastq" + "_1_repair.fq.gz" + " -index ../ref/ucsc.hg19.fasta -sample " + sampleid 
    os.system(cmd)

    #convert sam to bam, filter bam, sort bam
    cmd = samtools + " -sam " + sampleid + ".bwa.out.sam"
    os.system(cmd)

    #remove duplication
    cmd = picard + " -bam " + sampleid + ".bwa.out.sam" + ".F4.q20.sorted.bam "
    os.system(cmd)

    #gc correction
    cmd = deeptools + " -bam " + sampleid + ".bwa.out.sam" + ".F4.q20.sorted.bam" + ".rmdup.bam"
    os.system(cmd)

    #fetal fraction
    cmd = seqff_bam + " -bam " + sampleid + ".bwa.out.sam" + ".F4.q20.sorted.bam" + ".rmdup.bam" + ".gc_corrected.bam"
    os.system(cmd)

  #os.system(cmd)
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
  run_main(args)

if __name__ == '__main__':
    main()

