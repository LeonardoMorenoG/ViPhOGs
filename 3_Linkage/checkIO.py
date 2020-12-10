# -*- coding: utf-8 -*-
"""
checkIO
Created on Mon Oct 19 10:57:04 2015
given: a matrix of numbers
returns: a matrix of I(ones) and 0(zeros)
@author: lemoga
"""


if __name__ == "__main__":
    import sys
    
    fr = open(sys.argv[1])
    fw = open(sys.argv[2], "w")
    for line in fr:
        line = line.strip('\n').split('\t')
        newLine = []
        for item in line:
            value = int(item)
            if value > 0:
                newLine.append("1")
            else:
                newLine.append(item)
        fw.write('\t'.join(newLine) + '\n')
    fr.close()
    fw.close()



