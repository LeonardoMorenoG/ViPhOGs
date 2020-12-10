# -*- coding: utf-8 -*-
"""
splitGenBeank
Created on Tue Aug 18 18:46:21 2015
Given: a GenBank file of genomes & GIs of interest
reuturn: a genBank file for each genome of interest
@author: lemoga
Usage: python splitGenBank.py input.gb genomesOfInterest.txt
"""


if __name__ == "__main__":

    from Bio import SeqIO
    import sys
    
    fr = open(sys.argv[2])
    genomesOfInterest = []
    for line in fr:
        genomesOfInterest.append(line.strip('\n'))
    fr.close()
    

    for genome in SeqIO.parse(open(sys.argv[1]), "genbank"):
        gi = genome.annotations["gi"]
        print gi  + " checked"
        if gi in genomesOfInterest:
            fileName = gi+".fasta"
            fw = open(fileName,"w")
            SeqIO.write(genome, fw, "fasta")
            fw.close()
