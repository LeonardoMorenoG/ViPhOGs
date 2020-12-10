# -*- coding: utf-8 -*-
"""
readingGB
Created on Tue Aug 18 18:46:21 2015
Given: a GenBank file of genomes
reuturn: proteinsFile genomesWithoutProteinsFile
@author: lemoga
Usage: python readingGB.py input.gb proteins.out genomesWithotProteins.out
"""


if __name__ == "__main__":

    from Bio import SeqIO
    import sys
    
    fw = open(sys.argv[2], "w")
    fx = open(sys.argv[3], "w")
    
    for genome in SeqIO.parse(open(sys.argv[1]), "genbank"):
        acc = genome.id
        countCDS = 0
        for feature in genome.features:
            if feature.type == "CDS":
                #Looking for GI
                gi = ""
                try:
                    for ref in feature.qualifiers["db_xref"]:
                        if 'GI' in ref:
                            gi = ref.split(':')[1]
                            break
                except KeyError:
                    continue
                if gi == "":
                    continue
                fw.write(">" + acc + '|' + gi + '\n')
                #Looking for sequence
                seq = feature.qualifiers["translation"]
                fw.write(seq[0] + '\n')
                countCDS += 1
        if countCDS == 0:
            fx.write(acc + '\n')
    
    fw.close()
    fx.close()
