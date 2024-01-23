bedtools makewindows -g hg19.chrom.sizes  -w 100000 |  bedtools coverage -g hg19.chrom.sizes  -b SRR5975172.F4.q20.sorted.bam.markdup.rmdup.bam  -a -  -nonamecheck

genome_nuc_comp = !bedtools makewindows -g reference/hg38.chrom.sizes -w 100000 | bedtools nuc -fi reference/hg38.fa -bed -

