# -*- coding: utf-8 -*-
#!bin/python 
"""
parseRASTtk
Created on Tue Sep  8 20:05:06 2015
Given: RASTtk (Glimmer) protein output file
Return: Parsed protein file
@author: lemoga
usage: parseRASTtk.py inputFile
"""

"""
The parse is on the header of the sequence
From:
>prot Genome_intCoord_endCoord
To:
>Genome|prote|initCoord_endCoord_RASTtk
"""

if __name__ == "__main__":
    import sys
    import readFASTA
    
    sequences = readFASTA.ReadFasta(sys.argv[1])
    fw = open (sys.argv[1]+".mod","w")
    for seq in sequences:
        sequence = sequences[seq]
        seq = seq.split(' ')
        prot = seq[0].strip('>')
        seq = seq[1].split('_')
        genome = seq[0]
        initCoord = seq[1]
        endCoord = seq[2]
        fw.write('>'+genome+'|'+prot+'|'+initCoord+'_'+endCoord+'_RASTtk\n')
        fw.write(sequence + '\n')
    fw.close()