#!/bin/bash
#
#PBS -q batch 
#PBS -N CDHITPhage

cd $PBS_O_WORKDIR

module load cd-hit/4.6.1

cd-hit -i phageAndPredictedProteins.fasta -o equalProteinsPhages -d 0 -n 5 -c 0.99 -p 1
