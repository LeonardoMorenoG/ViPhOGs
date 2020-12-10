# -*- coding: utf-8 -*-
"""
singleLinkage.py
Created on Tue Oct 20 16:24:24 2015
Given: a simmilarity matrix
Return: single linkage desired
@author: lemoga
"""
def getDisMatrix(aPath):
    """
    transform similarity to distance matrix
    Parameters
    ----------
    aPath: a path file    
    Returns
    -------
    disMatrix: a distance matrix
    """
    matrix = np.loadtxt(open(aPath,"rb"),delimiter='\t')
    onesMatrix = np.copy(matrix)
    for row in onesMatrix:
        row.fill(1)
    disMatrix = np.subtract(onesMatrix,matrix)
    return disMatrix

def getSmallGenomes(sumGenes, nameGenomes):
    noInSG = []
    sgSumGenes = []
    sgNameGenomes = []
    noInMBG = []
    mbgSumGenes = []
    mbgNameGenomes = []
    i = 0
    for x in sumGenes:
        if x < 20 :
            sgSumGenes.append(x)
            sgNameGenomes.append(nameGenomes[i])
        else:
            noInSG.append(i)
        if x >= 18:
            mbgSumGenes.append(x)
            mbgNameGenomes.append(nameGenomes[i])
        else:
            noInMBG.append(i)
        i+=1
    return [[noInSG,sgSumGenes,sgNameGenomes],[noInMBG, mbgSumGenes, mbgNameGenomes]]
    
def splitDistMatix(disMatrix, noInSG, noInMBG):
    bigGenomes = np.delete(disMatrix,noInMBG,0)
    bigGenomes = np.delete(bigGenomes,noInMBG,1)
    smallGenomes = np.delete(disMatrix,noInSG,0)
    smallGenomes = np.delete(smallGenomes,noInSG,1)
    return [smallGenomes, bigGenomes]
    
def makeLinkage(distMatrixes,sgNames,bgNames):
    linkageBig = linkage(squareform(distMatrixes[1],'yes',True),"complete")
    flatClustersBig = fcluster(linkageBig,0.1,"distance")
    clustersBig = {}
    i = 0
    for x in flatClustersBig:
        if x in clustersBig:
            value = clustersBig[x]
            value.append(bgNames[i])
            clustersBig[x] = value
        else:
            clustersBig[x] = [bgNames[i]]
        i += 1
        
    linkageSmall = linkage(squareform(distMatrixes[0],'yes',True),"complete")
    flatClustersSmall = fcluster(linkageSmall,0.0,"distance")
    clustersSmall = {}
    i = 0
    for x in flatClustersSmall:
        if x in clustersSmall:
            value = clustersSmall[x]
            value.append(sgNames[i])
            clustersSmall[x] = value
        else:
            clustersSmall[x] = [sgNames[i]]
        i += 1
    return [clustersSmall, clustersBig]
    
        
if __name__ == "__main__":
    import sys
    import numpy as np
    from scipy.spatial.distance import squareform
    from scipy.cluster.hierarchy import linkage, fcluster
    
    disMatrix = getDisMatrix(sys.argv[1])
    
    fr = open(sys.argv[2])
    sumGenes = np.loadtxt(fr,delimiter='\t')#cjamge for tab
    fr.close()
    
    fr = open(sys.argv[3])
    "delete the last tab in the file befor run it"
    nameGenomes = fr.readline().strip('\n').split('\t')
    if(nameGenomes[-1] == '\t'):
        nameGenomes.pop(-1)
    fr.close()
    
    selector = getSmallGenomes(sumGenes,nameGenomes)
    distMatrixes = splitDistMatix(disMatrix, selector[0][0], selector[1][0])
    
    clusters = makeLinkage(distMatrixes,selector[0][2],selector[1][2])
    
    fw = open("output.txt", "w")
    for key in clusters[0]:
        if len(clusters[0][key]) == 1:
            continue
        else:
            for x in clusters[0][key]:
                fw.write( x+ '\t')
            fw.write('\n')
            
    for key in clusters[1]:
        if len(clusters[1][key]) == 1:
            continue
        else:
            for x in clusters[1][key]:
                fw.write( x+ '\t')
            fw.write('\n')
    
