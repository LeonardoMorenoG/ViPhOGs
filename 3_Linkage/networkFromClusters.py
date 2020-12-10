# -*- coding: utf-8 -*-
"""
networkFromCluster
Created on Tue Nov  3 11:20:31 2015
Given: a file of cluster (a cluster per line)
Returns: a cytoscape input file
@author: leonardo
"""

def clusters2Net(aPath):
    fr = open(aPath)
    fw = open("output.network",'w')
    for line in fr:
        line = line.strip('\t\n').split('\t')
        for i in range(0,len(line)-1):
            fw.write(line[i]+'\t1\t'+line[i+1]+'\n')
        fw.write(line[-1]+'\t1\t'+line[0]+'\n')
    fw.close()    
    
if __name__ == "__main__":
    import sys
    
    clusters2Net(sys.argv[1])
    