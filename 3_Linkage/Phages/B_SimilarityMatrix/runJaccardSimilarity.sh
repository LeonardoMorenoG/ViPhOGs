#!/bin/csh
#
#PBS -q batch  
#PBS -l nodes=6:ppn=6
#PBS -l pmem=8gb
#PBS -N JaccardTest

cd $PBS_O_WORKDIR

/opt/openmpi/1.8.5/bin/mpirun mpiJaccard 2071 130009
