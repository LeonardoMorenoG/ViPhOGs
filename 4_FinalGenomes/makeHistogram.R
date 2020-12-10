library(ggplot2)

args <- commandArgs(trailingOnly = TRUE)
data <- read.table(args[1], h=F)
#data <- read.table(file.choose()) 

m <- ggplot(data, aes(x=data$V1)) + geom_histogram(aes(fill=..count..), binwidth=5)
m <- m + xlim(0,300)

jpeg(file="histogram")
m
dev.off()