#!/bin/bash
#
#PBS -q batch 
#PBS -N CDHIT
#PBS -l mem=40gb
#PBS -l vmem=40gb

cd $PBS_O_WORKDIR

module load cd-hit/4.6.1

cd-hit-est -i repeatedPhages.fasta -o equalPhages -d 0 -n 8 -G 1 -c 0.95 -p 1 
