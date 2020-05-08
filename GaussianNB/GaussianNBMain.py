#!/usr/bin/python

"""
Note: Naive Bayes is great for text--it’s faster and generally gives better performance than an SVM.
"""

from sklearn.naive_bayes import GaussianNB
from prep_terrain_data import makeTerrainData
from class_vis import predictOutput

features_train, labels_train, features_test, labels_test = makeTerrainData(5000)

clf = GaussianNB()
clf.fit(features_train, labels_train)

# Drawing the decision boundary with the test points overlaid
predictOutput(clf, features_test, labels_test)




