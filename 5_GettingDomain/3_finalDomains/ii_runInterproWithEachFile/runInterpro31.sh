#!/bin/bash
#PBS -q batch
#PBS -N interpro031
#PBS -M jl.moreno116@uniandes.edu.co
#PBS -m abe

cd $PBS_O_WORKDIR 

module load python/2.7.9

interproscan-5.16-55.0/interproscan.sh -i allProteins.slice31.fasta -f tsv -o allProteins.slice31.domains.tsv
