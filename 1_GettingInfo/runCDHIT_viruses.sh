#!/bin/bash
#
#PBS -q batch
#PBS -l nodes=1:ppn=2 mem=16gb
#PBS -N CDHITvir
#PBS -M jl.moreno116@uniandes.edu.co
#PBS -m abe

cd $PBS_O_WORKDIR

module load cd-hit/4.6.1

cd-hit-est -i sequence1.fasta -o equalViruses1 -d 0 -n 8 -G 1 -c 0.95 -p 1 -M 16000 -T 0
cd-hit-est -i sequence2.fasta -o equalViruses2 -d 0 -n 8 -G 1 -c 0.95 -p 1 -M 16000 -T 0
cd-hit-est -i sequence3.fasta -o equalViruses3 -d 0 -n 8 -G 1 -c 0.95 -p 1 -M 16000 -T 0
cd-hit-est -i sequence4.fasta -o equalViruses4 -d 0 -n 8 -G 1 -c 0.95 -p 1 -M 16000 -T 0
cd-hit-est -i sequence5.fasta -o equalViruses5 -d 0 -n 8 -G 1 -c 0.95 -p 1 -M 16000 -T 0
cd-hit-est -i sequence6.fasta -o equalViruses6 -d 0 -n 8 -G 1 -c 0.95 -p 1 -M 16000 -T 0
cd-hit-est -i sequence7.fasta -o equalViruses7 -d 0 -n 8 -G 1 -c 0.95 -p 1 -M 16000 -T 0
cd-hit-est -i sequence8.fasta -o equalViruses8 -d 0 -n 8 -G 1 -c 0.95 -p 1 -M 16000 -T 0
cd-hit-est -i sequence9.fasta -o equalViruses9 -d 0 -n 8 -G 1 -c 0.95 -p 1 -M 16000 -T 0
cd-hit-est -i sequence10.fasta -o equalViruses10 -d 0 -n 8 -G 1 -c 0.95 -p 1 -M 16000 -T 0
cd-hit-est -i sequence11.fasta -o equalViruses11 -d 0 -n 8 -G 1 -c 0.95 -p 1 -M 16000 -T 0
cd-hit-est -i sequence12.fasta -o equalViruses12 -d 0 -n 8 -G 1 -c 0.95 -p 1 -M 16000 -T 0
cd-hit-est -i sequence13.fasta -o equalViruses13 -d 0 -n 8 -G 1 -c 0.95 -p 1 -M 16000 -T 0
cd-hit-est -i sequence14.fasta -o equalViruses14 -d 0 -n 8 -G 1 -c 0.95 -p 1 -M 16000 -T 0
