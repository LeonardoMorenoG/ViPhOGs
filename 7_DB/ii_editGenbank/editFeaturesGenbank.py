# -*- coding: utf-8 -*-
"""
editFeaturesGenbank
Created on Wed Mar  9 03:54:29 2016
Given: aGenbank proteinsFasta
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
            if '@' in protein.id:
                ID = protein.id
                L = ID.split('@')[-1].split(':')
                L = FeatureLocation(int(L[0]),int(L[1]))
                aType="Region"
                q = {}
                q["region_id"] = ID 
                q["protein_id"] = ID.split('@')[0]
                aFeature = SeqFeature(location=L, type=aType, qualifiers=q)
                genomeGB.features.append(aFeature)
            else:
                ID = protein.id
                L = FeatureLocation(0,1)
                aType = "CDS"
                q["region_id"] = ID 
                q["protein_id"] = ID.split('@')[0]
                aFeature = SeqFeature(id=ID, type=aType)
        finalGenomes.append(genomeGB)
    fw = open(sys.argv[3], 'w')
    SeqIO.write(finalGenomes, fw, "genbank")