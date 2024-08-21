## KF-NIPT
#### KF-NIPT: K-mer and fetal fraction-based estimation of chromosomal anomaly from NIPT data 
![image](https://github.com/eastbrain/KF-NIPT/assets/140467225/90a73a89-a3b5-4141-96dc-804b3ab08099)

![image](https://github.com/eastbrain/KF-NIPT/assets/140467225/ce591dcd-1f5b-4631-9ddc-f13181f1043d)

![image](https://github.com/eastbrain/KF-NIPT/assets/140467225/eb0632bf-139a-4542-9f12-445504da1ded)

![image](https://github.com/eastbrain/KF-NIPT/assets/140467225/40bb70b7-d88a-45d7-9e9e-3288a323b572)


# Demo

##  01) demo1 - single-end fastq
https://github.com/user-attachments/assets/f4f09428-1db7-475e-898a-acd0575dfccc

       shell> cd 00_demo/
       shell> ln -s ../ref .
       shell> cp -rf ../02_ngs_process/00_wgs_processing.py  ./
       shell> cp -rf ../04_statistics/kmer_coverage_med_bam.py ./
       shell> ln -s raw/demo_S1_R1_001.fastq.gz .
       shell> ./00_wgs_processing.py  -r1 demo_S1_R1_001.fastq.gz
       shell> python  kmer_coverage_med_bam.py demo.bwa.out.sam.F4.q20.sorted.bam.rmdup.bam.gc_corrected.bam
       shell> mkdir ff kmer
       shell> cp -rf  demo.k25.txt  kmer/
       shell> cp -rf  demo.bwa.out.sam.F4.q20.sorted.bam.rmdup.bam.gc_corrected.bam.ff.out.txt  ff/
      
## 02) demo2 - paired-end fastq
https://github.com/user-attachments/assets/5b57a879-c0c4-4abc-80c9-c74c43b37dd6
     
       shell> cd 00_demo/
       shell> ln -s ../ref .
       shell> cp -rf ../02_ngs_process/00_wgs_processing.py  ./
       shell> cp -rf ../04_statistics/kmer_coverage_med_bam.py ./
       shell> ln -s raw/demo_S1_R1_001.fastq.gz .
       shell> ln -s raw/demo_S1_R2_001.fastq.gz .
       shell> ./00_wgs_processing.py  -r1 demo_S1_R1_001.fastq.gz -r2 demo_S1_R2_001.fastq.gz
       shell> mkdir ff kmer
       shell> cp -rf  demo.k25.txt  kmer/
       shell> cp -rf  demo.bwa.out.sam.F4.q20.sorted.bam.rmdup.bam.gc_corrected.bam.ff.out.txt  ff/


The directories containing fetal fraction analysis results and the calculated KF-SCORE (K-mer and Fetal fraction-based Score), along with the relevant analysis python code, are available at the following address. You can use these to perform the analysis on the demo data as shown in the figure below.

https://github.com/eastbrain/KF-NIPT/tree/main/00_demo/T21
![image](https://github.com/eastbrain/KF-NIPT/assets/140467225/386e7a0f-5f3e-42ec-9704-158e2c501497)

https://github.com/eastbrain/KF-NIPT/tree/main/00_demo/T18
![image](https://github.com/eastbrain/KF-NIPT/assets/140467225/24a6e0cd-0bce-43d4-b6f0-0a1986188779)

https://github.com/eastbrain/KF-NIPT/tree/main/00_demo/T13
![image](https://github.com/eastbrain/KF-NIPT/assets/140467225/e4d200d2-bb38-4764-924c-815187af0ed3)


#### System requirements

            OS: Ubuntu 22.04.1
            Linux kernel: 5.15.0-76-generic
            python: version 3.7.6
            R: version 3.5.1
            
#### Installation

#### install 1
https://github.com/user-attachments/assets/7e04d807-066a-43d8-b815-f65de3cda67a
#### install 2
https://github.com/user-attachments/assets/8129765d-a4fc-4ade-a131-534cedc0fe8d
#### install 3
https://github.com/user-attachments/assets/23205b6d-9bdf-4f3a-9dd4-156361e24b5b
 
#### 01) setting environment for operating

    Linux Environment
    
        shell> wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
        shell> bash Anaconda3-2020.02-Linux-x86_64.sh
        shell> bash
        shell> conda config --add channels defaults
        shell> conda config --add channels bioconda
        shell> conda config --add channels conda-forge
        shell> pip install pysam==0.15.3
        shell> pip install py2bit==0.3.0
        shell> pip install deeptoolsintervals==0.1.9
        shell> pip install matplotlib==3.3.0
        shell> pip install plotly==4.9
        shell> pip install retrying==1.3.4
        shell> pip install pyBigWig==0.2.1
        shell> pip install khmer==2.1.1

        shell> wget https://github.com/deeptools/deepTools/archive/refs/tags/3.5.2.tar.gz
        shell> tar xvf 3.5.2.tar.gz
        shell> cd deepTools-3.5.2/
        shell> python setup.py build
        shell> python setup.py install
        shell> correctGCBias --version 
        shell> computeGCBias --version
        shell> cd ../
    
        shell> git clone https://github.com/eastbrain/KF-NIPT.git       
        shell> chmod 755 KF-NIPT/02_ngs_process/*.py
        shell> chmod 755 KF-NIPT/bin/FastQC/v0.12.1/bin/fastqc
        shell> cd KF-NIPT/bin/BBMap/39.06/bbmap
        shell> tar xvf BBMap_39.06.tar.gz
        shell> mv bbmap/* ./
        shell> chmod 755 *.sh
        shell> cd ../../../../

        shell> cd bin/java/openjdk-18.0.2
        shell> wget https://download.java.net/java/GA/jdk18.0.2/f6ad4b4450fd4d298113270ec84f30ee/9/GPL/openjdk-18.0.2_linux-x64_bin.tar.gz
       
        shell> tar xvf openjdk-18.0.2_linux-x64_bin.tar.gz
        shell> mv jdk-18.0.2/* ./
        shell> ./bin/java 
        shell> cd ../../../
        shell> chmod 755 bin/samtools/1.17/bin/samtools
        shell> bin/samtools/1.17/bin/samtools
        shell> chmod 755 bin/sickle/v1.33/bin/sickle
        shell> bin/sickle/v1.33/bin/sickle

        shell> chmod 755 bin/bwa/0.7.17/bin/bwa
        shell> cd ref
        shell> wget https://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/hg19.2bit
        shell> wget https://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/hg19.fa.gz
        shell> ../bin/bwa/0.7.17/bin/bwa index hg19.fa.gz
                 
     R Environment

        Linnx shell> conda install R=3.5.1
        R shell> conda install R=3.5.1
        R shell> if (!require("BiocManager", quietly = TRUE))
        install.packages("BiocManager")
        R> BiocManager::install("Rsamtools")



#### NGS processing

#### 0.0) automated mode
   
           shell> python 00_wgs_processing.py fastq -h

                 usage: 00_wgs_processing.py [-h] fastq

                 NIPT Welcoming version (sckacker@ajou.ac.kr,gtphrase@eonelab.co.kr)

                 positional arguments:
                   fastq       fastq, fastq.gz

                 optional arguments:
                    -h, --help  show this help message and exit
    
#### 0.1) fastq QC

            shell> python 01_fastqc_processing.py fastq
                   usage: 01_fastqc_processing.py [-h] fastq
                   01_fastqc_processing.py: error: the following arguments are required: fastq

#### 0.2) quality trim

            shell> python 02_sickle_quality_trim.py
                   usage: 02_sickle_quality_trim.py [-h] fastq
                   02_sickle_quality_trim.py: error: the following arguments are required: fastq

#### 0.3) genome alignment mapping

            shell> python 03_bwa_genome_mapping.py
                   usage:  03_bwa_genome_mapping.py [-h] trimmed.fastq
                   03_bwa_genome_mapping.py: error: the following arguments are required: trimmed.fastq   

#### 0.4) 1 - convert samtools to bam 
          2 - sort bam
          3 - mapping quality filter

            shell> python 04_samtools_sort_filter.py
                   usage: 04_samtools_sort_filter.py [-h] sam
                   04_samtools_sort_filter.py: error: the following arguments are required: sam

#### 0.5) remove duplication

            shell> python 05_picard_remove_duplicates.py
                   usage: 05_picard_remove_duplicates.py [-h] bam
                   05_picard_remove_duplicates.py: error: the following arguments are required: bam 

#### 0.6) gc correction

            shell> python 06_gc_correction.py
                   06_gc_correction.py [-h] bam
                   06_gc_correction.py: error: the following arguments are required: bam        




#### Calculate fetal fraction

#### 0.1) python mode

            shell> python 07_fetal_fraction.py
                   usage: 07_fetal_fraction.py [-h] bam
                   07_fetal_fraction.py: error: the following arguments are required: bam  

#### 0.2) R mode

            shell> Rscript seqff_bam.r input.bam output.txt     




#### Calculation coverage based on mapping read count per chromosomes

#### 0.1) for mapping reads per chromosomes

             shell> python read_counter_bam.py
                    usage: read_counter_bam.py [-h] bam
                    read_counter_bam.py: error: the following arguments are required: bam

#### 0.2) for mapping reads coverage by median per chromosomes

            shell> python read_coverage_med_bam.py
                   usage: read_coverage_med_bam.py [-h] bam
                   read_coverage_med_bam.py: error: the following arguments are required: bam                   





#### Calculation coverage based on detected K-mer count in mapping read per chromosomes

#### 0.1) count detected K-mer in mapping read per chromosomes

            shell> python read_counter_bam.py
                   usage: kmer_counter.py [-h] bam kmer(25,50,70...)
                   kmer_counter.py: error: the following arguments are required: bam, kmer

#### 0.2) count detected count in mapping read per chromosomes (strand specific )

            shell> python kmer_counter_strand.py
                   usage: kmer_counter_strand.py [-h] bam kmer(25,50,70...)
                   kmer_counter_strand.py: error: the following arguments are required: bam, kmer   

#### 0.3) Calculation coverage based on detected K-mer in mapping read per chromosomes

            shell> usage: python  kmer_coverage.py
                   usage: usage: kmer_coverage.py [-h] bam kmer
                   kmer_coverage.py: error: the following arguments are required: bam, kmer

#### 0.4) Calculation coverage based on detected K-mer in mapping read per chromosomes (strand specific )

            shell> python python kmer_coverage_strand.py
                   usage: kmer_coverage_strand.py [-h] bam kmer
                   kmer_coverage_strand.py: error: the following arguments are required: bam, kmer

#### 0.5) Calculation coverage by median based on detected K-mer in mapping read per chromosomes

            shell> python kmer_coverage_med_bam.py
                   usage: kmer_coverage_med_bam.py [-h] bam kmer
                   kmer_coverage_med_bam.py: error: the following arguments are required: bam, kmer




#### Calculation KF-score (K-mer and fetal fraction-based estimation) of chromosomal anomaly from NIPT data 

#### 0.1) Calculation KF-score based on detected K-mer in mapping read per chromosomes with fetal fraction

            shell> python calculate_kf_score_matrix.py
                   usage: calculate_kf_score_matrix.py [-h]  K-mer_directory fetal-fraction_directory matrix.out.txt 
                   Calculate_kf_score_matrix.py: error: the following arguments are required: kmer_dir, ff_dir, output         


#### 0.2) Detection chromosomal abnormalities

            shell> python detection_chromosome_abnormalities_T21.py
                   usage:detection_chromosome_abnormalities_T21.py [-h]  matrix.out.txt
                   detection_chromosome_abnormalities_T21.py: error: the following arguments are required: matrix

          
                   
