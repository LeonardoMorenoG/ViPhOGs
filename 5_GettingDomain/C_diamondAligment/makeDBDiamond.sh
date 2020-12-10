#!/bin/bash
#PBS-q batch

cd $PBS_O_WORKDIR

module load diamond/0.6.13.48

diamond makedb --in allProteins.sorted.fasta -d allProteins
