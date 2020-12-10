#/bin/sh
#
#PBS -q batch
#PBS -N transposeMatrix

cd $PBS_O_WORKDIR

module load R/3.1.2

Rscript transpose.R
