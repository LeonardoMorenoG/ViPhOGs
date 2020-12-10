#!/bin/bash
#
#PBS -q batch
#PBS -l nodes=1:ppn=4
#PBS -l mem=92gb 
#PBS -l vmem=92gb
#PBS -N SPFamily
#PBS -M jl.moreno116@uniandes.edu.co 
#PBS -m abe

cd $PBS_O_WORKDIR 

../SensitivityPrecision.pl fooGenXCLS.Family.csv fooTaxTagXGen.Family.transposed.csv > out_SP.family.txt
