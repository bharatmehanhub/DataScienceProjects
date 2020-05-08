#!/usr/bin/python
import random


def makeTerrainData(n_points):

    # Creating a toy data set
    random.seed(42)
    grade = [random.random() for i in range(0,n_points)]
    bumpy = [random.random() for i in range(0,n_points)]
    error = [random.random() for i in range(0,n_points)]

    y = [round(grade[i]*bumpy[i]+0.3+0.1*error[i]) for i in range(0,n_points)]

    for i in range(0, n_points):
        if grade[i]>0.8 or bumpy[i]>0.8:
            y[i] = 1.0

    # Splitting the data into train/test sets
    X = [[a, b] for a, b in zip(grade, bumpy)]
    split = int(0.80*n_points)
    X_train = X[0:split]
    X_test = X[split:]
    y_train = y[0:split]
    y_test = y[split:]

    return X_train, y_train, X_test, y_test
