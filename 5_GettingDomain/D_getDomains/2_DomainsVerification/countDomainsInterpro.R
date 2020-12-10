#count interpro domains per protein

args <- commandArgs(trailingOnly=T)

domains <- read.table(args[1],h=T,sep="\t")
count <- data.frame(table(domains$ProteinAccession))
write.table(x=count, file=args[2], sep="\t", row.names=F, quote=F)