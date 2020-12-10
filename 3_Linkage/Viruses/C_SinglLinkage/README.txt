python ../../singleLinkage2.py ../B_SimilarityMatrix/similarityMatrix.txt sumGenes.txt nameGenes.txt output.txt
python ../../selectRepresentant.py output.txt sumGenes.txt nameGenes.txt
python ../../networkFromClusters.py output.txt 
