#/bin/sh
#
#PBS -q batch
#PBS -N egb 
#PBS -l mem=16gb
#PBS -l vmem=16gb

cd $PBS_O_WORKDIR

module load anaconda/python2

python editFeaturesGenbank.py nonRedundantViralGenomes.gb ../../D_getDomains/3_allInterproDomains/xii_combineOutputs/UniverseOfViralProteins.fasta 
