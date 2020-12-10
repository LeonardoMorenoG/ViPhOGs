# -*- cofding: utf-8 -*-
"""
removeCoilsWhitoutAnnotation
Created on Sun Mar  6 12:58:45 2016

@author: leonardo
"""

import sys

fr = open(sys.argv[1],'r')
fw = open(sys.argv[2],'w')
for line in fr:
    aLine = line.strip('\n').split('\t')
    if int(aLine[6]) - int(aLine[5]) < 40:
        continue
    else:
        fw.write(line)
fr.close()
fw.close()
