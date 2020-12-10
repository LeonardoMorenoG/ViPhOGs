
# coding: utf-8

# In[56]:

import pandas as pd
import numpy as np


# In[100]:

def getMaxIndex(aFile, category):
    data = pd.read_csv(aFile, sep="\t", index_col=0, header=0)
    data = data.transpose()
    maxData = pd.DataFrame(data.max(axis=1), columns=[category])
    aFile += ".max.csv"
    maxData.to_csv(aFile, sep="\t", header=True, index=False)


# In[106]:

if __name__ == "__main__":
    import sys
    getMaxIndex(sys.argv[1], sys.argv[2])


# In[ ]:



