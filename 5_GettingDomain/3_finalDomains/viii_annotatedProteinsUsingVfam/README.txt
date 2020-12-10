i) compress and index the hmm database flatfile with hmmpress
hmmpress vFam-A_2014HighPerformance.hmm
ii) search the HMM database
hmmscan vFam-A_2014HighPerformance.hmm ../vii_getNonAnnotatedProteins/proteinsNotAnnotated.fasta > proteinsNotAnnotated.vFamAnnotation.out.txt

iii)Do the same for regions not annotated

iv) parse hmmer output file to tsv like interproscan
python hmmerOutParser.py proteinsNotAnnotated.vFamAnnotation.out.txt proteinsNotAnnotated.vFamAnnotation.out.tsv
python hmmerOutParser.py regionsNotAnnotated.vFamAnnotation.out.txt regionsNotAnnotated.vFamAnnotation.out.tsv

v)parse interproScan for join merged annotation
qsub runParserProteins.sh
qsub runParserRegions.sh

vi)Remove domains smaller than 30
#befor run removeRegionsSmallerThan30.py headers were removed
python removeRegionsSmallerThan40.py proteinsNotAnnotated.vFamAnnotation.out.parsed.tsv proteinsAnnotated.vFamAnnotation.final.tsv
python removeRegionsSmallerThan40.py regionsNotAnnotated.vFamAnnotation.out.parsed.tsv regionsNotAnnotated.vFamAnnotation.final.tsv 
