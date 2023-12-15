# KF-NIPT
A more accurate analysis tool utilized WGS data of cfDNA based on combined k-mer, modified z-score, and fetal fraction for the detection of fetal aneuploidy

System requirements

            OS: Ubuntu 22.04.1
            Linux kernel: 5.15.0-76-generic
            python: version 3.7.6
            R: version 3.5.1
            
Installation

01) setting environment for operating

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
    

NGS processing

0.0) automated mode
   
           shell> python 00_wgs_processing.py fastq -h

                 usage: 00_wgs_processing.py [-h] fastq

                 NIPT Welcoming version (sckacker@ajou.ac.kr,gtphrase@eonelab.co.kr)

                 positional arguments:
                   fastq       fastq, fastq.gz

                 optional arguments:
                    -h, --help  show this help message and exit
    
0.1) fastq QC

            shell> python 01_fastqc_processing.py fastq
                   usage: 01_fastqc_processing.py [-h] fastq
                   01_fastqc_processing.py: error: the following arguments are required: fastq

0.2) quality trim

            shell> python 02_sickle_quality_trim.py
                   usage: 02_sickle_quality_trim.py [-h] fastq
                   02_sickle_quality_trim.py: error: the following arguments are required: fastq

0.3) genome alignment mapping

            shell> python 03_bwa_genome_mapping.py
                   usage:  03_bwa_genome_mapping.py [-h] trimmed.fastq
                   03_bwa_genome_mapping.py: error: the following arguments are required: trimmed.fastq   

0.4) 1 - convert samtools to bam 
     2 - sort bam
     3 - mapping quality filter

            shell> python 04_samtools_sort_filter.py
                   usage: 04_samtools_sort_filter.py [-h] sam
                   04_samtools_sort_filter.py: error: the following arguments are required: sam

0.5) remove duplication

            shell> python 05_picard_remove_duplicates.py
                   usage: 05_picard_remove_duplicates.py [-h] bam
                   05_picard_remove_duplicates.py: error: the following arguments are required: bam 

0.6) gc correction

            shell> python 06_gc_correction.py
                   06_gc_correction.py [-h] bam
                   06_gc_correction.py: error: the following arguments are required: bam        


Calculate fetal fraction

0.1) python mode

            shell> python 07_fetal_fraction.py
                   usage: 07_fetal_fraction.py [-h] bam
                   07_fetal_fraction.py: error: the following arguments are required: bam  

0.2) R mode

            shell> Rscript seqff_bam.r input.bam output.txt             
