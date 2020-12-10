#Interpro output parser

setwd(getwd())
args <- commandArgs(trailingOnly = TRUE)
output <- read.table(args[1], header=F, sep="\t")
print("Table readed...")
colnames(output) <- c("ProteinAccession","SequenceMD5digest","SequenceLength","Analysis","SignatureAccession","SignatureDescription","Start","Stop","Score","Status","Date")
print("Colnames added...")
#output <- subset(output, output$SignatureDescription!="")
#print("Entries without description removed...")
#output <- output[with(output, order(ProteinAccession,Start,Stop)),]
#print("Table sorted...")

parsedOutput <- data.frame(row.names=c("ProteinAccession","SequenceMD5digest","SequenceLength","Analysis","SignatureAccession","SignatureDescription","Start","Stop","Score","Status","Date"))
domain <- output[1,]
for(i in 2:dim(output)[1]){
  x <- output[i,]
  if(domain$ProteinAccession==x$ProteinAccession){
    if(domain$Stop > x$Start){
      if(x$Stop > domain$Stop){
        domain$Stop <- x$Stop
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