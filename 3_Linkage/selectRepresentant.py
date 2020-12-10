# -*- coding: utf-8 -*-
"""
selectRepresentant
Created on Tue Oct 27 16:46:57 2015
Given: a file of clusters (with a a cluster per file's line)
Return: a file of representative clusters
@author: leonardo
"""

def readClusters(aPath):
    fr = open(aPath)
    clusters = []
    for line in fr:
        line = line.strip('\n').split('\t')
        clusters.append(Set(line))
    fr.close()
    return clusters
    
def makeNumGenes(numGenesPath, nameGenomesPaht):
    fr = open(numGenesPath)
    sumGenes = np.loadtxt(fr,delimiter='\t')
    fr.close()
    
    fr = open(nameGenomesPaht)
    nameGenomes = fr.readline().strip('\n').split('\t')
    if(nameGenomes[-1] == '\t'):
        nameGenomes.pop(-1)
    fr.close()
    #print(nameGenomes)
    
    numGenes = {}
    i = 0
    for x in nameGenomes:
        numGenes[x] = sumGenes[i]
        i += 1
        
    return numGenes
    
if __name__ == "__main__":
    from sets import Set
    import sys
    import numpy as np
    
    clusters = readClusters(sys.argv[1])
    numGenes = makeNumGenes(sys.argv[2], sys.argv[3])
    
    fw = open("output.representatives", 'w')
    for cluster in clusters:
        greater = ["",0]
        for x in cluster:
            try:
                if numGenes[x] > greater[1]:
                    greater[0] = x
                    greater[1] = numGenes[x]
            except:
                continue
        fw.write(greater[0] + '\n')
        greater = ["",0]
    fw.close()