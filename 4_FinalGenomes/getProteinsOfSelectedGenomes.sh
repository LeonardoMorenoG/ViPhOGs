#i)Search proteins that belongs to selected genomes
#grep -f patternFile FiletoSearcho > outFile
grep -f finalGenomesPhages.csv phageAndPredictedProteins.fasta > desiredProteins.txt
#Remove ">" from names
sed 's/>//g' desiredProteins.txt > desiredProteins.txt.mod
mv desiredProteins.txt.mod desiredProteins.txt
#Get those proteins
xargs samtools faidx phageAndPredictedProteins.fasta < desiredProteins.txt > desiredProteins.fasta
#Get proteins size
python ../getSequencesSize.py desiredProteins.fasta > desiredProteins.size
#Gives the sequences ordered by decrescent size
sort -k2 -n -r desiredProteins.size | awk -F"\t" '{print $1}' > desiredProteins.txt
xargs samtools faidx phageAndPredictedProteins.fasta < desiredProteins.txt > desiredProteins.fasta
