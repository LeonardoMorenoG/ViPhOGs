# file transformation | sort | unique -c
awk -F"|" '{print $1}' finalPhagesProteins.txt | sort | uniq -c
