# -*- coding: utf-8 -*-
"""
makeUniqueClusters.py
Created on Tue Oct 20 10:09:49 2015
The list of clusters that the program receive could have clusters with 
common elements. This program merge two clusters with common elements
and returns a list of unique clusters (cluters that do not share any element)
Given: a list of clusters
Return: a list of unique clusters
@author: lemoga
"""

def readClusters(aPath):
    fr = open(aPath)
    clusters = []
    for line in fr:
        line = line.strip('\n').split('\t')
        clusters.append(Set(line))
    fr.close()
    return clusters
    
def mergeSets(actual, merge, clusters):
    newSet= clusters[actual]
    for x in merge:
        newSet = newSet | clusters[x]
    clusters[actual] = newSet
    return clusters

def rmSets(merge,clusters):
    newClusters = []
    i=0
    for aSet in clusters:
        if i in merge:
            i += 1
            continue
        newClusters.append(aSet)
        i +=1
    return newClusters
        
def mergeForUnify(clusters):
    i = 1
    j = 0
    merge = []
    while i < len(clusters):
        for i in range(i,len(clusters)):
            if len(clusters[j] & clusters[i]) > 0:
                merge.append(i)
        clusters = mergeSets(j,merge, clusters)
        clusters = rmSets(merge, clusters)
        i += 1
        j += 1
    return clusters
        

if __name__ == "__main__":
    import sys
    from sets import Set
    
    clusters = readClusters(sys.argv[1])#clustersFile
    clusters = mergeForUnify(clusters)
    fw = open(sys.argv[2],"w")
    for aSet in clusters:
        for element in aSet:
            fw.write(element + '\t')
        fw.write('\n')
    fw.close()