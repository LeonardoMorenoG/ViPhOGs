# -*- coding: utf-8 -*-
#!bin/python
"""
parseProdigal.py
Created on Tue Sep  8 20:29:03 2015
Given: Prodigal protein output file
Return: Parsed protein file
@author: lemoga
usage: parseProdigal.py inputFile
"""

"""
The parse is on the header of the sequence
From:
>Genome_prot # initCoord # endCoord # otherInfo
To:
>Genome|prot|initCoord_endCoord_Prodigal
"""

if __name__ == "__main__":
    import sys
    import readFASTA
    
    sequences = readFASTA.ReadFasta(sys.argv[1])
    fw = open (sys.argv[1]+".mod","w")
    for seq in sequences:
        sequence = sequences[seq].strip('*')
        seq = seq.split('#')
        prot = "prot_" + seq[0].strip(' ').split('_')[1]
        genome = seq[0].split('_')[0] 
        initCoord = seq[1].strip(' ')
        endCoord = seq[2].strip(' ')
        fw.write(genome+'|'+prot+'|'+initCoord+'_'+endCoord+'_Prodigal\n')
        fw.write(sequence + '\n')
    fw.close()