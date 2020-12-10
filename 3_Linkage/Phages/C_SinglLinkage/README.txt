###
# makes a complete linkage from a simmilarity matrix
# similarityMatrix.txt -> From Jaccard distance
# sumGenes.txt	       -> TSV file with the number of genes per genome (TSV=Tab Separated Values) (one line file, each column a genome)
# nameGenes.txt        -> Actually the name must be nameGenomes. TSB file with genomes names
# output.txt           -> output file
### 
python ../../singleLinkage2.py ../B_SimilarityMatrix/similarityMatrix.txt sumGenes.txt nameGenes.txt output.txt
###
# Choose a representant for each cluster
# Files names are the same as above
###
python ../../selectRepresentant.py output.txt sumGenes.txt nameGenes.txt
###
# creates a network from the complete linkage
# Files names are the same as above
# Can visualize the network using cytoscape
###
python ../../networkFromClusters.py output.txt
###
# If you are interested in know wich genomes are exactly equal, use this script.
# 2070 make reference to the number of genomes.
###
python ../../identifyEquals.py Phages/B_SimilarityMatrix/similarityMatrix.txt  2070 Phages/C_SinglLinkage/nameGenes.txt > Phages/C_SinglLinkage/output.equals 
