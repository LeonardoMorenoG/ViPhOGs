#!/bin/bash
#PBS -q batch
#PBS -N dAlignmentK
#PBS -M jl.moreno116@uniandes.edu.co
#PBS -m abe

cd $PBS_O_WORKDIR

module load diamond/0.6.13.48

diamond blastp -d allProteins -q xak.fasta -o machesK00001.tbl -k 500 -e 1e-5 --seg no --sensitive 
diamond blastp -d allProteins -q xak.fasta -o machesK001.tbl -k 500 -e 1e-3 --seg no --sensitive
diamond blastp -d allProteins -q xak.fasta -o machesK01.tbl -k 500 -e 1e-1 --seg no --sensitive
