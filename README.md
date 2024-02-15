## KF-NIPT
#### KF-NIPT: K-mer and fetal fraction-based estimation of chromosomal anomaly from NIPT data 
![image](https://github.com/eastbrain/KF-NIPT/assets/140467225/90a73a89-a3b5-4141-96dc-804b3ab08099)

![image](https://github.com/eastbrain/KF-NIPT/assets/140467225/ce591dcd-1f5b-4631-9ddc-f13181f1043d)

![image](https://github.com/eastbrain/KF-NIPT/assets/140467225/eb0632bf-139a-4542-9f12-445504da1ded)

![image](https://github.com/eastbrain/KF-NIPT/assets/140467225/9f7414c0-aec3-4f13-9f7f-ca52d3f9014b)

#### System requirements

            OS: Ubuntu 22.04.1
            Linux kernel: 5.15.0-76-generic
            python: version 3.7.6
            R: version 3.5.1
            
#### Installation

#### 01) setting environment for operating

    Linux Environment
    
            shell> wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
            shell> bash Anaconda3-2023.09-0-Linux-x86_64.sh
            shell> conda update conda
            shell> conda config --add channels defaults
            shell> conda config --add channels bioconda
            shell> conda config --add channels conda-forge

    Python Environment
    
            shell> conda install python==3.7.6
            shell> pip install astropy==4.0
            shell> pip install biopython==1.81
            shell> pip install glob2==0.7
            shell> pip install khmer==2.1.1
            shell> pip install numpy==1.21.6
            shell> pip install pandas==1.0.1
            shell> pip install pysam==0.21.0
            shell> pip install pytest-astropy==0.8.0
            shell> pip install pytest-astropy-header==0.1.2
            shell> pip install scipy==1.4.1 
            shell> pip install seaborn==0.10.0
            shell> sudo apt-get install python3-pil.imagetk
                 
     R Environment

            Linnx shell> conda install R=3.5.1
            R shell> conda install R=3.5.1
            R shell> if (!require("BiocManager", quietly = TRUE))
               install.packages("BiocManager")
            R> BiocManager::install("Rsamtools")

    Bioinformatics Tools For NGS processing

           shell> conda install -c bioconda fastqc
           shell> conda install -c bioconda sickle
           shell> conda install -c bioconda bwa
           shell> conda install -c bioconda samtools
           shell> conda install -c bioconda picard
           shell> conda install -c bioconda deeptools
    


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

0.4) 1 - convert samtools to bam 
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

          
                   
