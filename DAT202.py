import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_blobs
from sklearn.cluster import MeanShift, KMeans, Birch
import matplotlib.pyplot as plt



# Import
dfInit = pd.read_csv("best sellin books total I.csv")
dfPrep = pd.read_csv("best sellin books total P.csv")

demoLabels = ['race', 'age', 'engnat', 'gender', 'hand', 'source', 'country']

'''
print(dfInit.dtypes.index)
print(dfInit.info(verbose=True))
print(dfInit.nunique())
'''

print(dfPrep.dtypes.index)
print(dfPrep.info(verbose=True))
print(dfPrep.nunique())

print(dfPrep[(dfPrep['form'] == "Imitation Leather")])

print(dfPrep[(dfPrep['form'] == "Spiral-bound")].to_string())

print(dfPrep[(dfPrep['Rating'] == 4.1)].to_string())

print(dfPrep)
print(dfPrep['Author'].value_counts())
print(dfPrep['Genre'].value_counts())
print(dfPrep['form'].value_counts())
print(dfPrep['Rating'].value_counts())
print(dfPrep['Print Length'].value_counts().to_string())
print(dfPrep[(dfPrep['Print Length'] == -1)])

print(dfPrep['Rating'].agg(["min", "mean", "max"]))
print(dfPrep['reviews count'].agg(["min", "mean", "max"]))
print(dfPrep['Print Length'].agg(["min", "mean", "max"]))
print(dfPrep['price'].agg(["min", "mean", "max"]))
dfPrep['AD'] = dfPrep['List Year'] - dfPrep['Publishing date']
print(dfPrep['AD'].agg(["min", "mean", "max"]))
print(dfPrep[(dfPrep['AD'] == -1)])

