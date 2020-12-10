# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 14:29:49 2016

@author: leonardo
"""

import sys 
import numpy as np
from Bio import SeqIO


#read sequences in fasta format
fr = open(sys.argv[1])
allSeqs = SeqIO.to_dict(SeqIO.parse(fr, "fasta"))
fr.close()

#Search each desired sequence
selectedSeqs = []
fr = open(sys.argv[2])
for line in fr:
    selectedSeqs.append(allSeqs[line.strip('\n')])
fr.close()

#Randomize selectedSeqs array
np.random.shuffle(selectedSeqs)
selectedSeqs=selectedSeqs[0:int(sys.argv[3])]

fw = open(sys.argv[4], 'w')
SeqIO.write(selectedSeqs, fw, "fasta")
fw.close()
