#solo se guarda para recordar el error que comet'i al no guardar la longitud de la secuencia query al hacer el parsing del hmmm
#ahora hmmerOutParser.py ya lo hace y no toca ejecutar este script

import sys

fr = open(sys.argv[1])
lengths = {}
for line in fr:
    line = line.strip('\n').split('\t')
    lengths[line[0]] = line[1]
fr.close()

fr = open(sys.argv[2])
fw = open(sys.argv[3],'w')
for line in fr:
    line = line.strip('\n').split('\t')
    fw.write(line[0]+'\t'+lengths[line[0]]+'\t'+line[1]+'\t'+line[2]+'\t'+line[3]+'\t'+line[4]+'\t'+line[5]+'\n')
fr.close()
fw.close()
