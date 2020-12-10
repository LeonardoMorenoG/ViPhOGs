"""
ImportantVariables.py
Leonardo Moreno G.
BCEM
Given: SPmatrixOutput RFselectedVariables
Retrieve:
Usage: python ImportantViPhOGs.py specificityPrecissionType.txt NEWimportantVOGsType.txt taxonomicAnnotationGenomesWithVOGs.csv
"""
import sys
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist
"""
import plotly
import plotly.graph_objs as go
plotly.offline.init_notebook_mode() # run at the start of every notebook
"""

#Read SP output
spMatrix = pd.read_csv(sys.argv[1], sep="\t",header=0, index_col=0) #egg specificityPrecissionType.txt
spMatrix = spMatrix.div(spMatrix.max()).fillna(0)
#pd.DataFrame.head(spMatrix)
#pd.DataFrame.to_csv(spMatrix, "specificityPrecissionType.txt", sep="\t")


#Read RF important Variables
fr = open(sys.argv[2], 'r')#egg. NEWimportantVOGsType.txt
VIPs = []
for line in fr:
    line = "CLS"+str(int(line.strip('\n'))+1)
    VIPs.append(line)
fr.close()
print len(VIPs)


#Coincident viPhogs, get the intersection of both groups of variables
importantVOGs = []
for cls in spMatrix.index:
    if cls in VIPs:
        importantVOGs.append(cls)
#d = set(VIPs)&set(spMatrix.index)
print len(importantVOGs)
importantVOGs = np.array(importantVOGs)


fr = open(sys.argv[3])#egg.taxonomicAnnotationGenomesWithVOGs.csv
print fr.readline()
accessions = {}
for line in fr:
    line = line.strip('\n').split(',')
    accession = line[0]
    taxPath = line[1:] #taxPath means taxonomy path
    accessions[accession] = taxPath
print len(accessions)


# # Plot concordandt viPhogs 

spMatrixImportant = spMatrix.loc[importantVOGs]
spMatrixImportant.to_csv("NEWconcordantViphogs.csv", sep="\t")
#spMatrixImportant = pd.read_csv("NEWconcordantViphogs.Genus.csv", sep="\t", index_col=0)
#pd.DataFrame.head(spMatrixImportant)
spMatrixImportant.shape
"""
colorscale = [[0, 'rgb(253,253,253)'],[0.1, "rgb(6,64,255)"],[0.325, "rgb(6,139,255)"],[0.55,"rgb(255,222,0)"],
              [0.775,"rgb(255,119,0)"],[1, 'rgb(255,0,0)']]  
data = [go.Heatmap(z=spMatrixImportant.values.tolist(),
                       #x=spMatrixImportant.columns.values,y=spMatrixImportant.index, 
                   colorscale=colorscale)]

layout = go.Layout(title='Specificity And Precision Type', width=1000,height=1000,autosize=False#,
                    #yaxis=dict(autotick=False,ticks='',nticks=len(spMatrixImportant.index),
                    #          tickfont=dict(family='Old Standard TT, serif',size=8,)
                    #      ),
                    #xaxis=dict(autotick=True, ticks="", nticks=len(spMatrixImportant.columns))
                    #showticklabels=True,
                    #dtick=700.0/len(spMatrix.index),
                    #
                  )
fig = go.Figure(data=data, layout=layout)
plotly.offline.iplot(fig)


# In[35]:

genomes = spMatrixImportant.columns.values
taxLabels = {"subspecies":0,"species":1,"subgenus":2,"genus":3,"subfamily":4,"family":5,"order":6,"type":7}
labels = []
for genome in genomes:
    label = accessions[genome][taxLabels["type"]]+"|"+accessions[genome][taxLabels["order"]]+"|"+accessions[genome][taxLabels["family"]]+"|"+accessions[genome][taxLabels["genus"]]
    labels.append(label)
np.savetxt("NEWlabelsGenus.txt", np.array(labels),delimiter='\n', fmt='%s')


# In[36]:

spMatrixImportant2 = spMatrixImportant
spMatrixImportant2.columns = labels
spMatrixImportant2.to_csv("NEWconcordantViphogs.Genus.csv", sep="\t")
"""
