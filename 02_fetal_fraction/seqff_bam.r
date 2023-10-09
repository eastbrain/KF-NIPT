##################################################################################################################################################
##################################################################################################################################################
##### SeqFF.R
##### Sung Kim, Phd
##### Sequenom, Inc.
#####
##################################################################################################################################################
##### Instructions
##### Command Line
##### R CMD BATCH
##### --i input directory
##### --f input file name
##### --d output directory
##### --o output file name
##### --t data type; sam file (without header) or tabulated read counts ordered by genomic coordinates found in SupplementalTable1.csv
##### SeqFF.R


##################################################################################################################################################
##################################################################################################################################################
#####
##### seqff_bam.r (bam version) 2023/08/29
#####
##### add bam processing
#####
##### Dongin Kim, senior researcher
##### Bioinformatics / Molecular diagnosis
##### EONE Laboratories, Incheon , KOREA, KR
#####
#####             email1: gtphrase@eonelab.co.kr
#####             email2: sckacker@ajou.ac.kr
#####             email3: gtphrase@naver.com
#####
##################################################################################################################################################
#####
##### R version 4.1.2 (2021-11-01) -- "Bird Hippie"
#####
##### if (!require("BiocManager", quietly = TRUE))
#####     install.packages("BiocManager")
##### BiocManager::install("Rsamtools") 
#####
#####
##### usage: Rscript seqff_bam.r input.bam output.txt
#####
#####
##################################################################################################################################################
##################################################################################################################################################

suppressMessages(library(Rsamtools))
suppressWarnings({
####################################################################################################################################################
ff.pred <- function(gc.norm.bc.61927, B, mu, parameter.1, parameter.2){
  gc.norm.bc.61927[is.na(gc.norm.bc.61927)] <- 0
  gc.norm.bc <- gc.norm.bc.61927[grepl('chr[0-9]', names(gc.norm.bc.61927))]
  gc.norm.bc.c <- gc.norm.bc - mu
  y.hat <- matrix(c(1, gc.norm.bc.c), nrow = 1) %*% B
  y.hat.rep <- sum(y.hat, na.rm = T) / sum(gc.norm.bc)
  ff.hat <- (y.hat.rep + parameter.1) * parameter.2
  return(ff.hat)
}
####################################################################################################################################################
calculate_ff <- function(bam,output){
  load("SupplementalFile1.RData")
  bininfo = read.csv("SupplementalTable2.csv")
  colnames(bininfo)[1]="binName"
  bininfo$binorder=c(1:61927)

  bam   <- scanBam(bam)[[1]]
  rname <- bam$rname
  pos   <- bam$pos
  dat <- data.frame()
  dat <- data.frame(matrix(nrow = 0, ncol = 2))
  columns <- c("refChr","begin")
  dat <- data.frame(matrix(nrow = 0, ncol = length(columns)))
  dat <- data.frame(rname,pos)
  colnames(dat) <- columns
  dat <- dat[dat$refChr!="*" & dat$refChr!="chrM" ,]
  binindex = ifelse((dat$begin%%50000)==0,floor(dat$begin/50000)-1,floor(dat$begin/50000))
  fastbincount = table(paste(dat$refChr,binindex, sep="_"))
  
  newtemp=as.data.frame(matrix(NA, ncol=2, nrow=length(fastbincount)))
  newtemp[,1]=paste(names(fastbincount))
  newtemp[,2]=as.numeric(paste(fastbincount))
  colnames(newtemp)=c("binName","counts")

  bininfo = merge(bininfo, newtemp, by="binName",all.x=T)
  bininfo=bininfo[order(bininfo$binorder),]

  ##################################################################################################################################################
  ##### DATA PROCESSING
  autosomebinsonly <- bininfo$BinFilterFlag==1 & bininfo$FRS!="NA" &  bininfo$CHR!="chrX" & bininfo$CHR!="chrY"
  alluseablebins   <- bininfo$BinFilterFlag==1 & bininfo$FRS!="NA"
  autoscaledtemp   <- bininfo$counts[autosomebinsonly]/sum(bininfo$counts[autosomebinsonly], na.rm=T)
  allscaledtemp    <- bininfo$counts[alluseablebins]/sum(bininfo$counts[autosomebinsonly], na.rm=T)
  # additive loess correction
  mediancountpergc <- tapply(autoscaledtemp,bininfo$GC[autosomebinsonly], function(x) median(x, na.rm=T))
  ## prediction
  #print(mediancountpergc)

  loess.fitted  <- predict( loess(mediancountpergc ~ as.numeric(names(mediancountpergc))), bininfo$GC[alluseablebins])
  normalizedbincount <- allscaledtemp + ( median(autoscaledtemp, na.rm=T) - loess.fitted )

  bincounts=rep(0,61927)
  names(bincounts) = bininfo$binName
  bincounts[alluseablebins] <- na.omit((normalizedbincount/sum(normalizedbincount, na.rm=T)) * length(normalizedbincount))
  wrsc=ff.pred(bincounts,B,mu,parameter.1,parameter.2)
  enet = bincounts %*% elnetbeta+elnetintercept
  ff=c((wrsc+enet)/2, enet, wrsc)
  names(ff)=c("SeqFF","Enet","WRSC")
  #print(ff)
  #write.csv(ff, file=output,sep="\t")
  write.table(ff, output, sep = "\t",  col.names = F, quote = F)
}
####################################################################################################################################################
main <- function() {
  #args=commandArgs()
  args = commandArgs(trailingOnly=TRUE)
  if (length(args)!=2) {
    stop("#################################################
        usage: Rscript seqff_bam.r input.bam output.txt\n\n

                                      EONE Laboratories

	                                     Dongin Kim


                          email1: gtphrase@eonelab.co.kr

                          email2: sckacker@ajou.ac.kr
        #################################################
	 ", call.=FALSE)
  } else if (length(args)==2) {
    bam <- args[1]
    out <- args[2]
    calculate_ff(bam,out)
  }
}
####################################################################################################################################################
if(!interactive()) {
    main()
}
####################################################################################################################################################
})
