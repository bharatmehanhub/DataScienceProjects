#!/usr/bin/python

import pandas as pd

df = pd.read_csv('emails.csv')


df2 = df.head(5000)

df2.to_csv('enron_test_data.csv')