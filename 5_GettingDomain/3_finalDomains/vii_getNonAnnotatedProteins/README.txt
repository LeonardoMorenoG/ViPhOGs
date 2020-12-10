i) get protein names that were annotated with interpro
awk -F"\t" '{print $1}' ../v_getNonDomainsRegions/allProteins.domainsAndNonDomRegions.tsv | sort -u > proteinsAnnotatedWithInterpro.names.txt
ii) get names of all proteins
grep ">" ../../../C_diamondAligment/allProteins.sorted.fasta | sed 's/>//g' | sort -u > allProteins.sorted.names.txt
iii) Get protein names that are not annotated
comm -23 allProteins.sorted.names.txt proteinsAnnotatedWithInterpro.names.txt > proteinsNotAnnotated.names.txt
iv) Get proteins that are not annotated in FASTA format
xargs samtools faidx ~/Documents/Projects/VOGss/5_GettingDomains/C_diamondAligment/allProteins.sorted.fasta < proteinsNotAnnotated.names.txt > proteinsNotAnnotated.fasta
v) Do the same for those regions that don't get an annotation 
grep "NoDomain" ../vi_extractSequences/regionsInterproScan.fasta | sed 's/>//g' > regionsNotAnnotated.names.txt
sed 's/ NoDomain//g' regionsNotAnnotated.names.txt > regionsNotAnnotated.names.txt.mod
mv regionsNotAnnotated.names.txt.mod regionsNotAnnotated.names.txt


