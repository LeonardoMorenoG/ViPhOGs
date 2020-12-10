setwd('/lustre/home/ciencias/biologia/jl.moreno116/VOGs/CDHIThproteins/sinLinPhages2')
data <- read.table("matrix.txt", h=F, sep='\t')
xxx <- t(data)
write.table(xxx, file="try.txt",sep='\t', row.names=F, col.names=F)
