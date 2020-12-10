#!/bin/bash
#
#$ -cwd
#$ -N SEEDssPh

../RASTtk/bin/svr_call_pegs < 14210833.fasta > 14210833.protein.fasta 2>14210833.out.tbl
../RASTtk/bin/svr_call_pegs < 14210825.fasta > 14210825.protein.fasta 2>14210825.out.tbl
../RASTtk/bin/svr_call_pegs < 14210826.fasta > 14210826.protein.fasta 2>14210826.out.tbl
../RASTtk/bin/svr_call_pegs < 14210831.fasta > 14210831.protein.fasta 2>14210831.out.tbl
../RASTtk/bin/svr_call_pegs < 14210827.fasta > 14210827.protein.fasta 2>14210827.out.tbl
