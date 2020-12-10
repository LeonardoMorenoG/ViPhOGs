#!/bin/bash
#
#PBS -q batch 
#PBS -N pCDHITp 

cd $PBS_O_WORKDIR

./Parse_CD-Hit-table.pl equalProteinsPhages.clstr > rawMatrixPhages.txt
