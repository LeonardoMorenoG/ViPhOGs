# -*- coding: utf-8 -*-
"""
readingGBorganism
Created on Tue Aug 18 18:46:21 2015
Given: a GenBank file of genomes
reuturn: taxonomy and gi for each gi
@author: lemoga
Usage: python readingGB.py input.gb proteins.out genomesWithotProteins.out
"""


if __name__ == "__main__":

    from Bio import SeqIO
    import sys

    for genome in SeqIO.parse(open(sys.argv[1]), "genbank"):
        print str(genome.annotations["taxonomy"]) + " " + genome.annotations["gi"]