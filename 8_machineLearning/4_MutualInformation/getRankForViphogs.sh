python getMaxIndex.py outfileMI.csv Order
python getMaxIndex.py outfileMI.family.csv Family
python getMaxIndex.py outfileMI.genus2.csv Genus
python getMaxIndex.py outfileMI.type.csv Type

paste *.max.csv > miAllRanks.csv

python getRank.py miAllRanks.csv
