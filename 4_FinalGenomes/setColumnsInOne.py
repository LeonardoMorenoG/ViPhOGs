# -*- coding: utf-8 -*-
"""
setColumnsInone
Created on Wed Nov  4 06:54:59 2015
Given: a file of culumns
Returns: a file with all columns in one
@author: leonardo
"""

if __name__ == "__main__":
    import sys
    
    fr = open(sys.argv[1])
    fw = open(sys.argv[2],'w')
    for line in fr:
        line = line.strip('\n').split('\t')
        for x in line:
            fw.write(x+'\n')
    fr.close()
    fw.close()