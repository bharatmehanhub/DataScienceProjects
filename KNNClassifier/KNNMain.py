#!/usr/bin/python

from sklearn.neighbors import KNeighborsClassifier
from class_vis import predictOutput
from prep_terrain_data import makeTerrainData

features_train, labels_train, features_test, labels_test = makeTerrainData(500)


clf = KNeighborsClassifier(n_neighbors=2)
clf.fit(features_train, labels_train)


# Drawing the decision boundary with the test points overlaid
predictOutput(clf, features_test, labels_test)

