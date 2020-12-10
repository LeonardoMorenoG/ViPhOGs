# -*- coding: utf-8 -*-
"""
identify equals
Created on Tue Nov  3 12:55:02 2015
given: a similarity Matrix
return: genome names 
@author: leonardo
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
    

if __name__ == "__main__":
    import numpy as np
    from scipy.spatial.distance import squareform

    import sys
    
    matrix = getDisMatrix(sys.argv[1])
    #get the triangular matrix
    tMatrix = squareform(matrix,'yes',True)
    
    fr = open(sys.argv[3])
    nameGenomes = fr.readline().strip('\n').split('\t')
    if(nameGenomes[-1] == '\t'):
        nameGenomes.pop(-1)
    fr.close()
    
    i = 0
    j = 1
    for x in tMatrix:
        if x == 0:
            print (nameGenomes[i],nameGenomes[j])
        if j == int(sys.argv[2]):
            i += 1
            j = 1+i     
            continue
        j += 1
