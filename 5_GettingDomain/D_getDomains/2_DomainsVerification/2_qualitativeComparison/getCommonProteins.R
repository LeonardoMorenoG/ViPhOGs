#1. Get proteins with domains in both methods 

args <- commandArgs(trailingOnly=T)

#Reading Data
interpro <- read.table(args[1],h=T,sep="\t")
colnames(interpro) <- c("ProteinAccession","Count.I")
BlastX0 <- read.table(args[2],h=F)
colnames(BlastX0) <- c("Count.0","ProteinAccession")

#Merge interpro info with each aprox and save data
domains <- merge(x=interpro, y=BlastX0, by="ProteinAccession",all.y=T)
domains$Count.I[is.na(domains$Count.I)]<-0
commons <- subset(domains, domains$Count.I > 0 & domains$Count.0 > 0)

#2. Get those common proteins and their domains from interpro domains file
#Read Data
interpro <- read.table(args[3], h=T, sep="\t")
#merge tables
interpro <- merge(x=interpro, y=commons, by="ProteinAccession")
#Select columns of interest 
columns <- c("ProteinAccession", "SignatureAccession", "Start", "Stop")
interproDomains <- interpro[columns]
numInterproDomains <- dim(interproDomains)[1]
numInterproDomains

#3. Get those common proteins and their domains from diamondAlignment aprox domains file
#Read data
diamond <- read.table(args[4], h=F, sep=" ")
colnames(diamond) <- c("ProteinAccession", "Start", "Stop")
#Merge tables
diamond <- merge(x=diamond, y=commons, by="ProteinAccession")
#Select columns of interest
columns <- c("ProteinAccession", "Start", "Stop")
diamondDomains <- diamond[columns]
numDiamondDomains <- dim(diamondDomains)[1]
numDiamondDomains

#4. Compare domains
#Merge data
allCombinations <- merge(x=diamondDomains, y=interproDomains, by="ProteinAccession")

#remove combinations that has not contained domains
domains <- subset(allCombinations, !(Stop.x < Start.y | Stop.y < Start.x) )

#Interpro domains contained in diamond domains
iCd <- subset(domains, Start.y >= Start.x & Stop.y <= Stop.x)
columns <- c("ProteinAccession", "SignatureAccession", "Start.y", "Stop.y")
numiCd <- dim(unique(iCd[columns]))[1]
columns <- c("ProteinAccession", "Start.x", "Stop.x")
numDiamondContainerDomains <- dim(unique(iCd[columns]))[1]
numiCd
numDiamondContainerDomains

#Diamond domains contained in interpro domains
dCi <- subset(domains, Start.x >= Start.y & Stop.x <= Stop.y)
columns <- c("ProteinAccession", "Start.x", "Stop.x")
numdCi <- dim(unique(dCi[columns]))[1]
columns <- c("ProteinAccession", "SignatureAccession", "Start.y", "Stop.y")
numInterproContainerdomains <- dim(unique(dCi[columns]))[1]
numdCi
numInterproContainerdomains

#Domains Size comparison 
interproDomains$length <- interproDomains$Stop - interproDomains$Start
x <- data.frame(interproDomains$length)
x$db <- "interpro"
colnames(x) <- c("length", "db")
mean(x$length)

diamondDomains$length <- diamondDomains$Stop - diamondDomains$Start
y <- data.frame(diamondDomains$length)
y$db <- "diamond"
colnames(y) <- c("length", "db")
mean(y$length)

sizes <- data.frame(colnames(c("length", "db")))
sizes <- rbind(x,y)

library(ggplot2)
library(scales)
pdf("outputCharts.pdf")
par(mfrow=c(3,1))
ggplot(sizes, aes(x=db, y=length)) + geom_violin()
ggplot(sizes, aes(x=db, y=log(length))) + geom_violin()
ggplot(sizes, aes(log(length), colour=db)) + geom_density(bindwith=1.0) + scale_x_continuous(breaks = pretty_breaks(n = 10))
dev.off()