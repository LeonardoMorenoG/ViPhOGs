#/bin/sh
#
#PBS -q short
#PBS -N makeBLASTDB
#PBS -l nodes=1
#PBS -l mem=8gb
#PBS -l vmem=8gb

cd $PBS_O_WORKDIR

module load blast/2.2.30

makeblastdb -in ~/D_getDomains/3_allInterproDomains/xii_combineOutputs/UniverseOfViralProteins.fasta -dbtype 'prot' -out UVP
#UVP means universe of viral proteins
