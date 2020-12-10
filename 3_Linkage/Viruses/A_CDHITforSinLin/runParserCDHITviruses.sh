#!/bin/bash
#
#PBS -q batch 
#PBS -N pCDHITv 

cd $PBS_O_WORKDIR

./Parse_CD-Hit-table.pl equalProteinsViruses.clstr > rawMatrixViruses.txt
