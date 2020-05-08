#!/usr/bin/python

from sklearn.tree import DecisionTreeClassifier
from class_vis import predictOutput
from prep_terrain_data import makeTerrainData

features_train, labels_train, features_test, labels_test = makeTerrainData(1000)

clf = DecisionTreeClassifier(min_samples_split=5, criterion='entropy')
clf.fit(features_train, labels_train)

# Drawing the decision boundary with the test points overlaid
predictOutput(clf, features_test, labels_test)