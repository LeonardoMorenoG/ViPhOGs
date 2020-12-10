# -*- coding: utf-8 -*-
"""
genomesPlusProteins.py
Created on Thu Mar 31 08:37:47 2016
Given: aGenbakFile Proteins.fasta
Return: a genbank with those proteins as features (only those proteins)
@author: leonardo
"""

if __name__ == "__main__":
    import sys
    from Bio import SeqIO
    from Bio.SeqFeature import SeqFeature, FeatureLocation
    #save geneBank as a dictionary
    fr = open(sys.argv[1], 'r')
    genomesDict = SeqIO.to_dict(SeqIO.parse(fr, "genbank"))
    fr.close()
    
    fr = open(sys.argv[2],'r')
    proteinsList = list(SeqIO.parse(fr, 'fasta'))
    proteinsDict = {} #dictionary of proteins saved by genome
    for protein in proteinsList:
        genome = protein.id.split('|')[0]
        if genome in proteinsDict:
            genomesProts = proteinsDict[genome]
            genomesProts.append(protein)
            proteinsDict[genome] = genomesProts
        else:
            genomesProts = [protein]
            proteinsDict[genome] = genomesProts
    
    finalGenomes = []
    for genome in proteinsDict:
        genomeGB = genomesDict[genome]
        source = genomeGB.features[0]
        genomeGB.features = []
        genomeGB.features.append(source)
        for protein in proteinsDict[genome]:
            aType = "CDS"
            L = FeatureLocation(0,1)
            ID = protein.id
            q = {}
            q["protein_id"] = protein.id
            #q["translation"] = protein.seq
            aFeature = SeqFeature(location=L, id=ID, type=aType, qualifiers=q)
            genomeGB.features.append(aFeature)
        finalGenomes.append(genomeGB)
    fw = open(sys.argv[3], 'w')
    SeqIO.write(finalGenomes, fw, "genbank")
