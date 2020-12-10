
# coding: utf-8

# In[113]:

import pandas as pd


# In[114]:

def getRank(aPath):
    data = pd.read_csv(aPath, sep='\t', header=0)
    i=1
    fw = open("output.txt", "w")
    for row in data.iterrows():
        row = row[1]
        fw.write(str(i) + "\t" + row[row == row.max()].index[0] + "\n")
        i += 1
    fw.close()


# In[157]:

if __name__ == "__main__":
    import sys
    getRank(sys.argv[1])


# In[ ]:



