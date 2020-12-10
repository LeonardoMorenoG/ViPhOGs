#!/bin/bash

#PBS -l nodes=node-3.local
#PBS -N parser1
#PBS -M jl.moreno116@uniandes.edu.co
#PBS -m abe

cd $PBS_O_WORKDIR 

module load R/3.1.2

/lustre/apps/R/3.1.2/bin/Rscript interproOutputParser.R allProteins.slice1.domains.tsv allProteins.slice1.domains.parsed.tsv
