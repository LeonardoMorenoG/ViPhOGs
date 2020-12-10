Split allProteins in five file just for parallelize python.

split -l 110000 allProteins.size.sorted.txt 
#Make jobs for get protein files 
python ../makeJobQueries.py splitAllProtein.sh ../B_splitForGoParallel
chmod +x splitAllProtein.sh
./splitAllProtein.sh 
mv xa* ../B_split... (mv all pertinent files to the respective folder)
