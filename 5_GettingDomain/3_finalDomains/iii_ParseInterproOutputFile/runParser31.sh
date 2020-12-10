#!/bin/bash

#PBS -q batch
#PBS -N parser31
#PBS -M jl.moreno116@uniandes.edu.co
#PBS -m abe

cd $PBS_O_WORKDIR 

module load R/3.1.2

/lustre/apps/R/3.1.2/bin/Rscript interproOutputParser.R allProteins.slice31.domains.tsv allProteins.slice31.domains.parsed.tsv
