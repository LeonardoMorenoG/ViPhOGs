# -*- coding: utf-8 -*-
#!bin/python
"""
parseGenemark.py
Created on Tue Sep  8 20:51:00 2015
Given: GenMark protein output file
Return: Parsed protein file
@author: lemoga
usage: parseGenemark.py inputFile
"""

"""
The parse is on the header of the sequence
From:
>prot|GeneMark.hmm|size|sense|initCoord|endCoord >Genome otherInfo(Complete genome name)
To:
>Genome|prot|initCoord_endCoord_Prodigal
"""

def makeFasta(aPath):
    fr = open(aPath)
    line = fr.readline()
    while line[0] != '>':
        line = fr.readline()
    fw = open(aPath + ".FASTA", "w")
    fw.write(line)
    for line in fr:
        fw.write(line)
    fw.close()
    fr.close()

if __name__ == "__main__":
    import sys
    import readFASTA
    
    makeFasta(sys.argv[1])
    sequences = readFASTA.ReadFasta(sys.argv[1]+".FASTA")
    fw = open (sys.argv[1]+".mod","w")
    for seq in sequences:
        if '>' in seq[0]:
            sequence = sequences[seq]
            seq = seq.split('|')
            prot = seq[0].strip('>').replace("gene","prot")
            initCoord = seq[4]
            seq = seq[5].split('\t')
            endCoord = seq[0]
            genome = seq[1].split(' ')[0].strip('>')
            
            fw.write('>'+genome+'|'+prot+'|'+initCoord+'_'+endCoord+'_GeneMark\n')
            fw.write(sequence + '\n')
    fw.close()
