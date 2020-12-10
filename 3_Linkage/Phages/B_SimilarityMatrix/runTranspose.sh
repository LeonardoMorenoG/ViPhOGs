#/bin/sh
#
#PBS -q batch
#PBS -N makeBLASTDB

cd $PBS_O_WORKDIR

module load R/3.1.2

Rscript transpose.R
