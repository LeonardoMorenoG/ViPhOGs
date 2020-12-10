# -*- coding: utf-8 -*-
"""
checkLessThan20
Created on Sun Mar  6 08:24:34 2016

@author: leonardo
"""

import sys 

fr = open(sys.argv[1], 'r')
for line in fr:
    line = line.strip('\n').split('\t')
    x = int(line[6])
    y = int(line[7])
    if y - x <= 20:
        print line

