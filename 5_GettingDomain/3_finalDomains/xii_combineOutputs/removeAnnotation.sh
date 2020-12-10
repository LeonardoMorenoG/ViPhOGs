import sys

fr = open(sys.argv[1])
fw = open(sys.argv[2], 'w')

for line in fr:
    if " " in line:
        line = line.split(" ")[0]
        fw.write(line+'\n')
    else:
        fw.write(line)

fw.close()
fr.close()
