# -*- coding: utf-8 -*-
"""
getRegionsWithoutAnnotation.py
Created on Mon Feb 29 14:26:41 2016

@author: leonardo
"""

def addLine(fw, acc, length, analysis, signatureAcc, signatureDesc, start, stop):
    line = acc+'\t'+str(length)+'\t'+analysis+'\t'+signatureAcc+'\t'+signatureDesc+'\t'+str(start)+'\t'+str(stop)+'\n' 
    fw.write(line)

if __name__ == "__main__":
    import sys
    
    fr = open(sys.argv[1], "r")
    fr.readline()#omits the header of the file
    
    fw = open(sys.argv[2], "w")
    
    actual = "" #ActualProtein
    startNewRegion = 0 
    length = 0
    #i = 1
    for line in fr:
        #print line
        line  = line.strip("\n").split("\t")        
        if actual != line[0]:
            if length - startNewRegion > 39:
                addLine(fw, acc, length, "", "", "NoDomain",startNewRegion, length)
            startNewRegion = 0    
        acc = line[0]
        actual = acc 
        length = int(line[1])
        db = line[2]
        signAcc = line[3]
        desc = line[4]
        start = int(line[5])
        stop = int(line[6])
        stopNewRegion = start-1
        if stopNewRegion - startNewRegion > 39:
            addLine(fw, acc, length, "", "", "NoDomain",startNewRegion, stopNewRegion)
        addLine(fw, acc, length, db, signAcc, desc,start, stop)
        startNewRegion = stop + 1 
        #i +=1 
    
    fr.close()
    fw.close()
