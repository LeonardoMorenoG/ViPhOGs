#!/bin/sh
#
#PBS -q batch  
#PBS -N sinLinVir 

cd $PBS_O_WORKDIR

module load python/2.7.9

python singleLinkage2.py similarityMatrix.txt.mod sumGenes.txt nameGenes.txt
