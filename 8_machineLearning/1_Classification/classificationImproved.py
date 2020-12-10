
# coding: utf-8

# In[1]:
import sys

import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

#import plotly.plotly as py
#py.sign_in('lemoga', 'j891204l')
#import plotly
#import plotly.graph_objs as go
#plotly.offline.init_notebook_mode() # run at the start of every notebook


# In[2]:

def getData(npyMatrix, npyLabels):
    matrix = pd.DataFrame(np.load(npyMatrix))#"Order/trainTestMatrixOrderAll.npy"
    matrix.columns = ["CLS"+str(i) for i in range(1,matrix.shape[1]+1)]
    matrix["Labels"] = np.load(npyLabels)#"Order/trainTestLabelsOrderAll.npy"
    return matrix


# In[3]:

def attributeEvaluatorFilter(attributeEvaluatorOutput, classificationMatrix):
    attributeEvaluatorOutput.append("Labels")
    return classificationMatrix[attributeEvaluatorOutput]


# In[4]:

def getMedian(matrix):
    numLabels = matrix["Labels"].unique()
    if len(numLabels)%2 == 0:
        counts = matrix["Labels"].value_counts().tolist()
        return (count[(len(numLabels)/2)-1]+counts[len(numLabels)/2])/2
    else:
        return matrix["Labels"].value_counts().tolist()[((len(numLabels)+1)/2)-1]


# In[5]:

def bootstrap_resample(X, n=None):
    """ Bootstrap resample an array_like
    Parameters
    ----------
    X : array_like
      data to resample
    n : int, optional
      length of resampled array, equal to len(X) if n==None
    Results
    -------
    returns X_resamples
    """
    if n == None:
        n = len(X)

    resample_i = np.floor(np.random.rand(n)*len(X)).astype(int)
    X_resample = X[resample_i]
    return X_resample


# In[6]:

def sampler(matrix):
    median = getMedian(matrix)
    #median = matrix["Labels"].value_counts().min()
    lenSample = median/2
    trainIndex = np.array([])
    testIndex = np.array([])
    for label in matrix["Labels"].unique():
        indexLabel = matrix[matrix["Labels"]==label].index.values
        np.random.shuffle(indexLabel)
        if indexLabel.shape[0]>= median:
            trainIndex = np.concatenate((trainIndex,indexLabel[:lenSample]))
            testIndex = np.concatenate((testIndex,indexLabel[lenSample*(-1):]))
        else:
            trainIndex = np.concatenate((trainIndex,bootstrap_resample(indexLabel[:(indexLabel.shape[0]/2)+1],lenSample)))
            testIndex = np.concatenate((testIndex,bootstrap_resample(indexLabel[indexLabel.shape[0]/2:])))
    return trainIndex,testIndex


# In[7]:

def classification(matrix, samples, labelsDict):
    allClassiffiers = []

    for sample in samples:
        trainIndex = sample[0]
        testIndex = sample[1]

        xTrain = matrix.iloc[trainIndex]
        yTrain = xTrain["Labels"]
        xTrain = xTrain.ix[:,xTrain.columns!="Labels"]

        xTest = matrix.iloc[testIndex]
        yTest = xTest["Labels"]
        xTest = xTest.ix[:,xTest.columns!="Labels"]

        clf = RandomForestClassifier(n_estimators=60, max_depth=None, min_samples_split=1, random_state=0)
        clf.fit(xTrain,yTrain)
        yPredict = clf.predict(xTest)
        cm = confusion_matrix(yTest, yPredict, labels=labelsDict.values())
        cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        allClassiffiers.append([clf, clf.score(xTest, yTest),cm_normalized])

    return allClassiffiers


# In[8]:

def getMeanImportance(allClassiffiers):
    importance = pd.DataFrame()

    for i in range(len(allClassiffiers)):
        clf = allClassiffiers[i][0]
        varImportance = clf.feature_importances_
        importance[i] = varImportance
        #std = np.std([tree.feature_importances_ for tree in clf.estimators_], axis=0)
        #indices = np.argsort(varImportance)[::-1][0:830] #num viphogs importantes orden

    mean = importance.mean(axis=1)
    std = importance.std(axis=1)
    order = list(np.argsort(mean)[::-1])

    meanSorted = []
    stdSorted = []
    for viphog in order:
        meanSorted.append(mean[viphog])
        stdSorted.append(std[viphog])

    return order, meanSorted, stdSorted


# In[9]:

def is_outlier(points, thresh=3.5):
    """
    Taken from
    http://stackoverflow.com/questions/22354094/pythonic-way-of-detecting-outliers-in-one-dimensional-observation-data#22357811
    26/03/2017
    Returns a boolean array with True if points are outliers and False
    otherwise.

    Parameters:
    -----------
        points : An numobservations by numdimensions array of observations
        thresh : The modified z-score to use as a threshold. Observations with
            a modified z-score (based on the median absolute deviation) greater
            than this value will be classified as outliers.

    Returns:
    --------
        mask : A numobservations-length boolean array.

    References:
    ----------
        Boris Iglewicz and David Hoaglin (1993), "Volume 16: How to Detect and
        Handle Outliers", The ASQC Basic References in Quality Control:
        Statistical Techniques, Edward F. Mykytka, Ph.D., Editor.
    """
    if len(points.shape) == 1:
        points = points[:,None]
    median = np.median(points, axis=0)
    diff = np.sum((points - median)**2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)

    modified_z_score = 0.6745 * diff / med_abs_deviation

    return modified_z_score > thresh


# In[10]:

matrix = getData(sys.argv[1],sys.argv[2])#"Order/trainTestMatrixOrderAll.npy","Order/trainTestLabelsOrderAll.npy"


# In[11]:

spOutput = list(pd.read_csv(sys.argv[3], sep="\t",header=0, index_col=0).index.values)#"../2_SP/Order/specificityPrecissionOrder.txt"

with open(sys.argv[4]) as miFile:#"../../12_MutualInformation/4_ViPhOGselection/importantViphogsMIOrder.csv"
    miOutput = ["CLS"+line.strip('\n') for line in miFile]

spmi = list(set(spOutput + miOutput))
reducedMatrix = attributeEvaluatorFilter(spmi, matrix)
#pd.DataFrame.head(reducedMatrix)


# In[13]:

samples = []
for i in range(1000):
    trainIndex, testIndex = sampler(reducedMatrix)
    samples.append((trainIndex,testIndex))


# In[14]:

labelsDict = np.load(sys.argv[5]).item()#"Order/trainTestLabelsDictOrderAll.npy"


# In[15]:

allClassiffiers = classification(reducedMatrix, samples, labelsDict)


# In[16]:

importanceOrder, meanImportance, stdImportance = getMeanImportance(allClassiffiers)
order = []
for i in importanceOrder:
    order.append(reducedMatrix.columns.values[i])


# In[17]:

#trace1 = go.Scattergl(y=meanImportance, x=[i for i in range(len(importanceOrder))],
#                      error_y=dict(type='data', array=stdImportance),mode="markers")

#trace1 = go.Scattergl(y=[c[1]for c in allClassiffiers], x=[i for i in range(len(allClassiffiers))],
#                      mode="markers")
#layout = go.Layout(title="ViPhogs Importance")#width=1400,#autozise=False)
#fig = go.Figure(data=[trace1], layout=layout)
#plotly.offline.iplot(fig)


# In[19]:

i=0
for x in is_outlier(np.array(meanImportance)):
    if x:
        i+=1
    else:
        break


fw = open(sys.argv[6])#"importantViphogs.Order.csv"
for viphog in order[:i]:
    fw.write(viphog+'\n')

# In[65]:

#subColumns = order
#numViPhogs = []
#meanScore = []
#stdScore = []
#while len(subColumns) > 2:
#    decreasingMatrix = reducedMatrix[subColumns+["Labels"]]
#    allSelectionClassifiers = classification(decreasingMatrix, samples[:100], labelsDict)
#    numViPhogs.append(len(subColumns))
#    scores = [c[1] for c in allSelectionClassifiers]
#    meanScore.append(np.mean(np.array(scores)))
#    stdScore.append(np.std(np.array(scores)))
#    subColumns = subColumns[:(len(subColumns)/5)*4]


# In[66]:

#trace1 = go.Scattergl(y=meanScore[::-1], x=numViPhogs[::-1],#x=[i for i in range(len(meanScore))],
#                      error_y=dict(type='data', array=stdScore[::-1], visible=True, color='black', thickness=0.5),
#                      name="100", mode="markers", marker = dict(size = 5))

#layout = go.Layout(title="Classification Score Vs Num. of ViPhOGs", xaxis=dict(type='log'))#width=1400,#autozise=False)
#fig = go.Figure(data=[trace1], layout=layout)
#plotly.offline.iplot(fig)


# In[72]:

#i=0
#for x in is_outlier(np.array(meanScore[::-1])):
#    if x:
#        i+=1
#    else:
#        break


# In[26]:

#cm_normalized = sum([c[2] for c in allClassiffiers])/len(allClassiffiers)


# In[31]:
"""
myGreys = [
        [0,"rgb(255,255,255)"],
        [0.0588235294,"rgb(240,240,240)"],
        [0.1176470588,"rgb(225,225,225)"],
        [0.1764705882,"rgb(210,210,210)"],
        [0.2352941176,"rgb(195,195,195)"],
        [0.2941176471,"rgb(180,180,180)"],
        [0.3529411765,"rgb(165,165,165)"],
        [0.4117647059,"rgb(150,150,150)"],
        [0.4705882353,"rgb(135,135,135)"],
        [0.5294117647,"rgb(120,120,120)"],
        [0.5882352941,"rgb(105,105,105)"],
        [0.6470588235,"rgb(90,90,90)"],
        [0.7058823529,"rgb(75,75,75)"],
        [0.7647058824,"rgb(60,60,60)"],
        [0.8235294118,"rgb(45,45,45)"],
        [0.8823529412,"rgb(30,30,30)"],
        [0.9411764706,"rgb(15,15,15)"],
        [1,"rgb(0,0,0)"]
    ]

data = [go.Heatmap(z=cm_normalized,x=labelsDict.keys(),y=labelsDict.keys(),colorscale=myGreys)]
layout = go.Layout(
    title='Confussion Matrix', width=1000, height=1000, autosize=False,#
    xaxis=dict(autotick=False,ticks='',nticks=len(labelsDict.keys()),
                              tickfont=dict(family='Old Standard TT, serif',size=8,color='black')),
    yaxis=dict(autotick=False,ticks='',nticks=len(labelsDict.keys()),
                              tickfont=dict(family='Old Standard TT, serif',size=8,color='black')),)
fig = go.Figure(data=data, layout=layout)
plotly.offline.iplot(fig)


# In[ ]:
"""
