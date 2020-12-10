#!/usr/bin/python
#Taken from https://bioexpressblog.wordpress.com/2014/04/15/calculate-length-of-all-sequences-in-an-multi-fasta-file/
"""
getSequencesSize.py
Given: multiFastaFile
Returns: size of each seq in multiFasta
@author GummyBear April 15, 2014
Usage: python getSequencesSize.py multiFasta > output
"""
from Bio import SeqIO
import sys
cmdargs = str(sys.argv)
for seq_record in SeqIO.parse(str(sys.argv[1]), "fasta"):
 output_line = '%s\t%i' % \
(seq_record.id, len(seq_record))
 print(output_line)
