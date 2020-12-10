import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import timeit

# Load Data
trainTestMatrix = np.load("trainTestMatrixFamilyAll.npy")
trainTestLables = np.load("trainTestLabelsFamilyAll.npy")

# Classification (sample as data)
sampleSplit = cross_validation.StratifiedShuffleSplit(trainTestLables, 50, 
                                                      test_size=0.5, random_state=0)
classifiers = {}
for i in range(10,101,10):
    classifiers[i] = []

fw = open("timesFamily.wall.csv","w")
fw.write("Time n_estimators\n")
    
for i in range(10,101,10):
    for trainIndex, testIndex in sampleSplit:
	start_time = timeit.default_timer()
	# code you want to evaluate
        xTrain, xTest, yTrain, yTest = [], [], [], []
        for x in trainIndex:
            xTrain.append(trainTestMatrix[x])
            yTrain.append(trainTestLables[x])
        for x in testIndex:
            xTest.append(trainTestMatrix[x])
            yTest.append(trainTestLables[x])

        clf = RandomForestClassifier(n_estimators=i, max_depth=None,
                                     min_samples_split=1, random_state=0)
        clf.fit(xTrain,yTrain)
        classifiers[i]. append((clf,clf.score(xTest,yTest),xTrain,xTest, yTrain, yTest))
	elapsed = timeit.default_timer() - start_time
	fw.write(str(elapsed) + str(i) + "\n")
fw.close()

#compuTime = pd.read_csv("timesFamily.wall.csv", sep=" ")
#pd.DataFrame.head(compuTime)
#compuTimeMean = compuTime.groupby('n_estimators').mean()
#compuTimeStd = compuTime.groupby("n_estimators").std()

classifiersScores = {}
for i in range(10,101,10):
    classifiersScores[i] = []
    for c in classifiers[i]:
        classifiersScores[i].append(c[1])

fw = open("dictClassifiersScoresFamily.txt","w")
for key in classifiersScores:
    fw.write(str(key)+"\n")
    fw.write(str(classifiersScores[key]))
fw.close()
