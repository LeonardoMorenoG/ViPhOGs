#VisualizeDomainsCountComparison

args <- commandArgs(trailingOnly=T)

interpro <- read.table(args[1],h=T,sep="\t")
colnames(interpro) <- c("ProteinAccession","Count.I")
BlastX0 <- read.table(args[2],h=F)
colnames(BlastX0) <- c("Count.0","ProteinAccession")
BlastX4 <- read.table(args[3],h=F)
colnames(BlastX4) <- c("Count.4","ProteinAccession")
BlastX8 <- read.table(args[4],h=F)
colnames(BlastX8) <- c("Count.8","ProteinAccession")
BlastX16 <- read.table(args[5],h=F)
colnames(BlastX16) <- c("Count.16","ProteinAccession")

library(ggplot2)
library(reshape2)
domains <- merge(x=interpro, y=BlastX0, by="ProteinAccession",all.y=T)
domains[is.na(domains)] <- 0
domains <- melt(domains, id="ProteinAccession")
p <- ggplot(domains, aes(x=ProteinAccession, y=value, fill=variable)) 
p <- p + geom_bar(position = "fill",stat='identity')
p <- p + theme(axis.text.x = element_blank())
phist <- ggplot(domains, aes(value, ..density.., colour=variable)) + geom_freqpoly(binwidth=1)

domains <- merge(x=interpro, y=BlastX4, by="ProteinAccession", all.y=T)
domains[is.na(domains)] <- 0
domains <- melt(domains, id="ProteinAccession")
q <- ggplot(domains, aes(x=ProteinAccession, y=value, fill=variable)) 
q <- q + geom_bar(position = "fill",stat='identity')
q <- q + theme(axis.text.x = element_blank())
qhist <- ggplot(domains, aes(value, ..density.., colour=variable)) + geom_freqpoly(binwidth=1)

domains <- merge(x=interpro, y=BlastX8, by="ProteinAccession", all.y=T)
domains[is.na(domains)] <- 0
domains <- melt(domains, id="ProteinAccession")
r <- ggplot(domains, aes(x=ProteinAccession, y=value, fill=variable)) 
r <- r + geom_bar(position = "fill",stat='identity')
r <- r + theme(axis.text.x = element_blank())
rhist <- ggplot(domains, aes(value, ..density.., colour=variable)) + geom_freqpoly(binwidth=1)

domains <- merge(x=interpro, y=BlastX16, by="ProteinAccession", all.y=T)
domains[is.na(domains)] <- 0
domains <- melt(domains, id="ProteinAccession")
s <- ggplot(domains, aes(x=ProteinAccession, y=value, fill=variable)) 
s <- s + geom_bar(position = "fill",stat='identity')
s <- s + theme(axis.text.x = element_blank())
shist <- ggplot(domains, aes(value, ..density.., colour=variable)) + geom_freqpoly(binwidth=1)

pdf(args[6])
par(mfrow=c(8,1))
p
phist
q
qhist
r
rhist
s
shist
dev.off()