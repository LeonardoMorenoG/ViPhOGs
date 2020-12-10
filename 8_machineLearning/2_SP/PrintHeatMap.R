#!/usr/bin/Rscript

rm(list=ls());
library(gplots);
Inputs<-commandArgs(trailingOnly=TRUE)
#Inputs=c("~/Dropbox/Work/MalCheck/", "ToHeatMap_Consensus.txt", "HeatMap_consenus.pdf", "white", "blue", "red")

##set working directory
setwd(getwd())
#setwd(Inputs[1])
#Load file in R, assumes first row is header and first column is row names.
MatrixFile<-as.matrix(read.table(file=Inputs[1], header=T, sep="\t", row.names=1))
#Mt<-log((MatrixFile*100000)+1)
#Mt2<-log(Mt)
# Opens the output file
pdf(file=Inputs[2])
# Makes the color gradient, uniformly distributed
#colfun<-colorRampPalette(c(Inputs[3], Inputs[4],Inputs[5]))
colfun<-colorRampPalette(c('white', 'blue', 'green', 'yellow', 'orange','red'))

#Matrix_norm<-sqrt(MatrixFile)

# Makes and print the heatmap, 100 colors.
heatmap.2(MatrixFile, Rowv=F, Colv=F, scale="none", col=colfun(1000), dendrogram="none", trace="none", density.info="none")
# Close the output PDF
dev.off()
