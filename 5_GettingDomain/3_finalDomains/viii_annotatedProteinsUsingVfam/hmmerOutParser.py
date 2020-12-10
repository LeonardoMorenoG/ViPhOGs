# -*- coding: utf-8 -*-
"""

Created on Mon Mar  7 10:32:21 2016

@author: leonardo
"""

import Bio.SearchIO.HmmerIO as hIO
import sys 

fr = open(sys.argv[1])

x = hIO.hmmer3_text.Hmmer3TextParser(fr)

fw = open(sys.argv[2], 'w')
for element in x:
    p = str(element).split('\n')[1].split('(')[1].split(')')[0] #Cant get query length in a simple way
    lengthQuery = p
    for a in element.hsps:
        fw.write(a.query.id + '\t')
        fw.write(lengthQuery + '\t')
        fw.write("vFam"+ '\t')
        fw.write(a.hit.id+ '\t')
        fw.write(a.hit.id + '_' + str(a.hit_start) + '_' + str(a.hit_end) + '\t')
        fw.write(str(a.query_start) + '\t')
        fw.write(str(a.query_end) + '\n')
fw.close()
fr.close()        