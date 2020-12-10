#/bin/sh
#
#PBS -q batch
#PBS -N fb10 
#PBS -l nodes=1:ppn=6:intel
#PBS -l mem=16gb
#PBS -l vmem=16gb

cd $PBS_O_WORKDIR

module load blast/2.2.30

blastp -query ../i_PrepareBLAST/vpb10.fasta -db ../i_PrepareBLAST/UVP -outfmt 6 -show_gis -comp_based_stats T -seg yes -num_threads 6 -out vpb10.filtering.out.tab
