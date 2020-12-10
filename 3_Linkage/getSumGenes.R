setwd('/lustre/home/ciencias/biologia/jl.moreno116/VOGs/CDHIThproteins/sinLinViruses')
data <- read.table("matrix.txt", h=F)
sumGenes <- colSums(data)
write(sumGenes, file="sumGenes.txt", sep='\t', ncolumns=dim(data)[2])
