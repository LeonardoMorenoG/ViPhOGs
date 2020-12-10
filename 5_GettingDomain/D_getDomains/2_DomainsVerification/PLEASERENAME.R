args <- commandArgs(trailingOnly=T)

#Reading Data
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

#"Empty data frame for save data"
#comparison <- data.frame(x=character(), onlyI=integer(), onlyD=integer(),both=integer(), neither=integer())
comparison <- data.frame()

#"Merge interpro info with each aprox and save data"
domains <- merge(x=interpro, y=BlastX0, by="ProteinAccession",all.y=T)
domains$Count.I[is.na(domains$Count.I)]<-0
comparison[1,1] <- "x0"
comparison[1,2] <- sum(domains$Count.I > 0 & domains$Count.0 == 0)
comparison[1,3] <- sum(domains$Count.I == 0 & domains$Count.0 > 0)
comparison[1,4] <- sum(domains$Count.I > 0 & domains$Count.0 > 0)
comparison[1,5] <- sum(domains$Count.I == 0 & domains$Count.0 == 0)
colnames(comparison) <- c("x","onlyI","onlyD","both","neither")

domains <- merge(x=interpro, y=BlastX4, by="ProteinAccession",all.y=T)
domains$Count.I[is.na(domains$Count.I)]<-0
comparison[2,1] <- "x4"
comparison[2,2] <- sum(domains$Count.I > 0 & domains$Count.4 == 0)
comparison[2,3] <- sum(domains$Count.I == 0 & domains$Count.4 > 0)
comparison[2,4] <- sum(domains$Count.I > 0 & domains$Count.4 > 0)
comparison[2,5] <- sum(domains$Count.I == 0 & domains$Count.4 == 0)

domains <- merge(x=interpro, y=BlastX8, by="ProteinAccession",all.y=T)
domains$Count.I[is.na(domains$Count.I)]<-0
comparison[3,1] <- "x8"
comparison[3,2] <- sum(domains$Count.I > 0 & domains$Count.8 == 0)
comparison[3,3] <- sum(domains$Count.I == 0 & domains$Count.8 > 0)
comparison[3,4] <- sum(domains$Count.I > 0 & domains$Count.8 > 0)
comparison[3,5] <- sum(domains$Count.I == 0 & domains$Count.8 == 0)

domains <- merge(x=interpro, y=BlastX16, by="ProteinAccession",all.y=T)
domains$Count.I[is.na(domains$Count.I)]<-0
comparison[4,1] <- "x8*2"
comparison[4,2] <- sum(domains$Count.I > 0 & domains$Count.16 == 0)
comparison[4,3] <- sum(domains$Count.I == 0 & domains$Count.16 > 0)
comparison[4,4] <- sum(domains$Count.I > 0 & domains$Count.16 > 0)
comparison[4,5] <- sum(domains$Count.I == 0 & domains$Count.16 == 0)

#make barplot
library(ggplot2)
library(reshape2)

comparison <- melt(comparison, id="x")
comparison <- comparison[with(comparison, order(x)),]

plot <-ggplot(comparison, aes(x=variable, y=value, fill=variable)) + geom_bar(stat="identity") + facet_grid(. ~ x)
pdf(args[6])
plot
dev.off()