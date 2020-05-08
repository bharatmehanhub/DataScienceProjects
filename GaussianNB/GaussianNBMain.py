#!/usr/bin/python

from sklearn.naive_bayes import GaussianNB
from prep_terrain_data import makeTerrainData
from class_vis import predictOutput

features_train, labels_train, features_test, labels_test = makeTerrainData(5000)

clf = GaussianNB()
clf.fit(features_train, labels_train)

### draw the decision boundary with the text points overlaid
predictOutput(clf, features_test, labels_test)




