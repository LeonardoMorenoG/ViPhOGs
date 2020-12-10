DIAMOND

#Concatenate finalPhagesProteins.fasta and finalViralProteins.fasta in one file (allProteins.fasta)
#Make diamond database
diamond makedb --in allProteins.fasta -d allProteins

#Run the program with blastp
diamond blastp -d nonRedundantVirusProteins138465 -q ./clusteredProteins138465.faa -o maches.tbl -t ./temp -k 100 -e 1e-5 --seg yes --sensitive
