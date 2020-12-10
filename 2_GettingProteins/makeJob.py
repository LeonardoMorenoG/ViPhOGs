import os
import sys

files = os.listdir(sys.argv[2])

fw = open(sys.argv[1],"w")
for x in files:
    x2 = x.split('.')[0]
    fw.write("python getDomains.py " + x + " > " + x + ".domains\n")
    fw.write("printf " + x2 + "'\\n'\n")
fw.close()
