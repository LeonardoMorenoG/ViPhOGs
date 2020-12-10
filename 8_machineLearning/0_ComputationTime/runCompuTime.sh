#!/bin/bash
#
#PBS -q batch
#PBS -l nodes=1:ppn=4
#PBS -l mem=92gb 
#PBS -l vmem=92gb
#PBS -N timeFamilyFam2
#PBS -M jl.moreno116@uniandes.edu.co 
#PBS -m abe

module load anaconda/python2
cd $PBS_O_WORKDIR 

python compuTime.py
