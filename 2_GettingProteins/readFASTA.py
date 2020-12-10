# -*- coding: utf-8 -*-
"""
ReadFasta.py
Created on Tue Sep  8 19:58:57 2015
Given: FASTA file
Returns: A dictionary with all sequences in the FASTA file
@author: lemoga
"""

def ReadFasta(aPath):    
    """
    Transforms a fasta file into a dictionary of Ids -> sequences.
    
    Parameters:
    aPath : string
        path (or name) of the FASTA file.
    
    Returns:
    -----------
    fastaDict : list
        Dictionary with the sequences
    """
    fr = open(aPath)
    dictOfsequences = {}
    seqID = ''
    seq = ''
    flag = 0
    for line in fr:
        if '>' in line:
            if flag != 0:
                dictOfsequences[seqID] = seq
                seq = ''
            seqID=line.replace('\n','')
            flag += 1
        else:
            seq += line.replace('\n','')
    dictOfsequences[seqID] = seq
    fr.close()
    return dictOfsequences

if __name__ == "__main__":
    import sys
    sequences = ReadFasta(sys.argv[1])
    for seq in sequences:
        print seq
        print sequences[seq]