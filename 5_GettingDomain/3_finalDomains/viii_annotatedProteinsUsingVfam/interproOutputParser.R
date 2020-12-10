#Interpro output parser

setwd(getwd())
args <- commandArgs(trailingOnly = TRUE)
output <- read.table(args[1], header=F, sep="\t")
print("Table readed...")
colnames(output) <- c("ProteinAccession","Analysis","SignatureAccession","SignatureDescription","Start","Stop")
print("Colnames added...")
#output <- subset(output, output$SignatureDescription!="")
#print("Entries without description removed...")
output <- output[with(output, order(ProteinAccession,Start,Stop)),]
#print("Table sorted...")
#write.table(x=output, file=args[3], sep="\t", row.names=F, quote=F)

parsedOutput <- data.frame(row.names=c("ProteinAccession","Analysis","SignatureAccession","SignatureDescription","Start","Stop"))
domain <- output[1,]
if(domain$Stop < domain$Start){
  aux <- domain$Stop
  domain$Stop <- domain$Start
  domain$Start <- aux
}
for(i in 2:dim(output)[1]){
  print(i)
  x <- output[i,]
  if(x$Stop < x$Start){
    aux <- x$Stop
    x$Stop <- x$Start
    x$Start <- aux
  }
  if(domain$ProteinAccession==x$ProteinAccession){
    if(domain$Stop > x$Start){
      if(x$Stop > domain$Stop){
        domain$Stop <- x$Stop
	domain$SignatureDescription <- paste(domain$SignatureDescription, x$SignatureDescription, sep="-")
      }else{
        domain$SignatureDescription <- paste(domain$SignatureDescription, x$SignatureDescription, sep="-")
      }
    }else{
      parsedOutput <- rbind(parsedOutput, domain)
      domain <- x
    }
  }else{
    parsedOutput <- rbind(parsedOutput, domain)
    domain <- x
  }
}
parsedOutput <- rbind(parsedOutput, domain)
write.table(x=parsedOutput, file=args[2], sep="\t", row.names=F, quote=F)
