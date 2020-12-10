#!/bin/bash

#PBS -q batch
#PBS -N parser42
#PBS -M jl.moreno116@uniandes.edu.co
#PBS -m abe

cd $PBS_O_WORKDIR 

module load R/3.1.2

/lustre/apps/R/3.1.2/bin/Rscript interproOutputParser.R allProteins.slice42.domains.tsv allProteins.slice42.domains.parsed.tsv
