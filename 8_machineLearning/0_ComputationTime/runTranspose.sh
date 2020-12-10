#!/bin/bash
#
#PBS -q batch
#PBS -l nodes=1:ppn=4
#PBS -l mem=92gb 
#PBS -l vmem=92gb
#PBS -N transpose
#PBS -M jl.moreno116@uniandes.edu.co 
#PBS -m abe

cd $PBS_O_WORKDIR 

./ToTranspose.awk fooGenXCLS.csv > fooGenXCLS.transposed.csv
