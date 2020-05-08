#!/usr/bin/python

# They work well with small and medium datasets and not with large datasets.
# They work well with datasets carrying less noise. Noise is well handled by Naive Bayes in most of the cases.

from sklearn.svm import SVC
from class_vis import predictOutput
from prep_terrain_data import makeTerrainData

features_train, labels_train, features_test, labels_test = makeTerrainData(5000)

clf = SVC(kernel='linear')
clf.fit(features_train, labels_train)

predictOutput(clf, features_test, labels_test)