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
    if((aLine[3] == "Coils" or aLine[3]=="Gene3D") and aLine[5]=='-'):
        if int(aLine[7]) - int(aLine[6]) < 30:
            continue
        else:
            fw.write(line)
    else:
        fw.write(line)
fr.close()
fw.close()
