# -*- coding: utf-8 -*-
"""
readCDHIToutput
Created on Mon Aug 17 18:29:37 2015
given : .clstr output file
return: representatives.out notRepresentatives.out
@author: lemoga
usage: python readCDHIToutput.py cdhitOutput representatives.out nonRepresentatives.out
"""

class Cluster:
    name = ""
    members = []
    def __init__(self, n):
        self.name = n
        self.members = []

class Member:
    gi = ""
    accession = ""
    representative = False
    def __init__(self, g, a, r):
        self.gi = g
        self.accession = a
        self.representative = r

def getKey(aMember):
    return aMember.representative
    
def readOutCDHIT(aPath):
    fr = open(aPath)
    clusters = []
    cluster = Cluster("dummy")
    for line in fr:
        if ">Cluster" in line:
            clusters.append(cluster)
            name = line.rstrip('\n')
            cluster = Cluster(name)
        else:
            line = line.split('|')
            gi = line[1]
            accession = line[3]
            if 'NC_' in accession:
                representative = True
            else:
                representative = False
            aMember = Member(gi, accession, representative)
            cluster.members.append(aMember)
    clusters.append(cluster)
    fr.close()
    return clusters
    
def writeOutputs(aList, aPath1, aPath2):
    fw = open(aPath1, "w")
    fx = open(aPath2, "w")
    for cluster in aList:
        if cluster.name != "dummy":
            mList = sorted(cluster.members, key=getKey)
            fw.write(mList[-1].gi)
            fw.write('\n')
            for m in mList[0:-1]:
                fx.write(m.gi)
                fx.write('\n')
    fw.close()
    fx.close()
    
if __name__ == "__main__":
    import sys
    print "reading the output file..."
    clst = readOutCDHIT(sys.argv[1])
    print str(len(clst)) + " clusters found"
    print "writing output files"
    writeOutputs(clst, sys.argv[2], sys.argv[3])