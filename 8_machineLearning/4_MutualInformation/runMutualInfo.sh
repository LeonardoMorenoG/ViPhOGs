#/bin/bash

#PBS -N M.I.Genus
#PBS -l nodes=1:ppn=4
#PBS -l mem=48gb
#PBS -l vmem=48gb
#PBS -M jl.moreno116@uniandes.edu.co
#PBS -m abe
#PBS -l walltime=96:00:00


cd $PBS_O_WORKDIR

#./MutualInformation-Unweighted_info.pl familyViPhogsMatrix.csv familyTaxonomyMatrix.csv > outfileMI.family.csv
#./MutualInformation-Unweighted_info.pl genusViPhogsMatrix.csv genusTaxonomyMatrix.csv > outfileMI.genus2.csv
#./MutualInformation-Unweighted_info.pl orderViphogsMatrix.csv orderTaxonomyMatrix.csv > outfileMI.csvi
./MutualInformation-Unweighted_info.pl typeViPhogsMatrix.csv typeTaxonomyMatrix.csv > outfileMI.type.csv
