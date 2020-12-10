fr = open("/home/leonardo/Documents/Projects/VOGss/7_DBtests/iv_queries/taxonomyAnotation.csv")
accessions = {}
for line in fr:
    line = line.strip('\n').split(',')
    accession = line[0]
    taxPath = line[1:] #taxPath means taxonomy path
    accessions[accession] = taxPath
print len(accessions)


fr = open("/home/leonardo/Documents/Projects/VOGss/6_GetCOGs/E_getCOG/viii_getCOGs/genomesVsClusters.sorted.greaterThan2.tab")
genomes = []
genomesClusters = []
actualGenome = ""

for line in fr:
    line = line.strip('\n').split('\t')
    genome = line[0].split('.')[0]
    cluster = line[1]
    if actualGenome != genome:
        actualGenome = genome 
        genomes.append(genome)
        clusters = {}
        if cluster in clusters:
            clusters[cluster] = clusters[cluster] + 1
        else:
            clusters[cluster] = 1
        genomesClusters.append(clusters)
    else:
        clusters = genomesClusters[-1]
        if cluster in clusters:
            clusters[cluster] = clusters[cluster] + 1
        else:
            clusters[cluster] = 1
        genomesClusters[-1] = clusters
fr.close()

sumClusters = []
for genome in genomesClusters:
    sumClusters.append(sum(genome.values()))

fw = open("taxonomicAnnotationGenomesWithVOGs.csv",'w')
for genome in genomes:
    fw.write(genome + ',' + ','.join(accessions[genome]) + '\n')
fw.close()


genomesWithoutAnnotation = set(accessions.keys()) - set(genomes)

fw = open("taxonomicAnnotationGenomesWithoutVOGs.csv",'w')
for genome in genomesWithoutAnnotation:
    fw.write(genome + ',' + ','.join(accessions[genome]) + '\n')
fw.close()
