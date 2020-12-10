#!/bin/bash

#PBS -q batch
#PBS -N parser40
#PBS -M jl.moreno116@uniandes.edu.co
#PBS -m abe

cd $PBS_O_WORKDIR 

module load R/3.1.2

/lustre/apps/R/3.1.2/bin/Rscript interproOutputParser.R allProteins.slice40.domains.tsv allProteins.slice40.domains.parsed.tsv