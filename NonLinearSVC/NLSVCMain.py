#!/usr/bin/python

from sklearn.svm import SVC
from class_vis import predictOutput
from prep_terrain_data import makeTerrainData

features_train, labels_train, features_test, labels_test = makeTerrainData(5000)

clf = SVC(C=1000, gamma=1000, kernel='rbf')
clf.fit(features_train, labels_train)

# Drawing the decision boundary with the test points overlaid
predictOutput(clf, features_test, labels_test)