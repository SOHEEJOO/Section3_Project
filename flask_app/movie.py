import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets
from embedding_as_service_client import EmbeddingClient
from sklearn.model_selection import train_test_split
import pickle
import joblib

client = EmbeddingClient(host='13.125.113.215', port=8989)

data = pd.read_csv('movies_metadata.csv', sep=',')
data = data.dropna()
data = data.drop(['id'], axis=1)
print(data)

model=LinearRegression()

target ='revenue'

y = data[target]
x = data.drop(columns=target)

model.fit(x,y)

joblib.dump(model, "model.pkl")

