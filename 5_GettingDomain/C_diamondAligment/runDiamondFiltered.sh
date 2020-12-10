#!/bin/bash
#PBS -q batch
#PBS -N dAlignmentKfil
#PBS -M jl.moreno116@uniandes.edu.co
#PBS -m abe

cd $PBS_O_WORKDIR

module load diamond/0.6.13.48

diamond blastp -d allProteins -q xak.fasta -o filMachesK00001.tbl -k 500 -e 1e-5 --seg yes --sensitive 
diamond blastp -d allProteins -q xak.fasta -o filMachesK001.tbl -k 500 -e 1e-3 --seg yes --sensitive
diamond blastp -d allProteins -q xak.fasta -o filMachesK01.tbl -k 500 -e 1e-1 --seg yes --sensitive
