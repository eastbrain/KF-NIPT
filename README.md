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

01) fastq QC

            shell> python 01_fastqc_processing.py fastq
