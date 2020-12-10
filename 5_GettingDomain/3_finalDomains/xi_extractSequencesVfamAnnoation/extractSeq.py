# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
    
def extract(aSequence, listCoordinates):
    regions = []
    i = 1
    for xy in listCoordinates:
        newId = "r"+str(i)
        region = aSequence.seq[xy[0]:xy[1]]
        regions.append(region)
    return regions
        
        

if __name__ == "__main__":
    import sys
    from Bio import SeqIO
    from Bio.SeqRecord import SeqRecord
    from Bio.Alphabet import IUPAC
    from Bio.Seq import Seq
    
    #READ FILE OF SEQUENCES IN FASTA FORMAT
    fr = open(sys.argv[1], "r")
    sequences = list(SeqIO.parse(fr, "fasta"))
    fr.close()
    
    #PARSE THAT FILE INTO A DICTIONARY FOR AN EASY SEARCH
    dictSequences = {}
    for seq in sequences:
        dictSequences[seq.id] = seq
        
    #READ DE FILE OF REGIONS TO EXTRACT
    regionsAndProteins = []    
    fr = open(sys.argv[2])
    name = "ipS_"
    for line in fr:
        line = line.strip('\n').split('\t')
        if line[0] in dictSequences:
            x1 = int(line[5])
            x2 = int(line[6])
            annotation = line[4]
            code = line[0] + '@' + str(x1) + ":" + str(x2)
            region = SeqRecord(dictSequences[line[0]].seq[x1:x2], id=code, description=annotation)
            regionsAndProteins.append(region)
        else:
            print line
    fr.close()
    
    fw = open(sys.argv[3], 'w')
    SeqIO.write(regionsAndProteins, fw, "fasta")
    fw.close()
