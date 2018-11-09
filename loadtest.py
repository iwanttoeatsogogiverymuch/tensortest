import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
import pymysql 
import pandas as pd
import numpy as np
import os
import json
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from keras.models import load_model
seed = 17
np.random.seed(seed)

train_data = "data.csv"
train_df = pd.read_csv(train_data,header=None)
traind_values = train_df.values
print(train_df.head(3))

train_x = traind_values[:,0:27].astype(int)
train_label = traind_values[:,28].astype(int)

encoder = LabelEncoder()
encoder.fit(train_label)
encoded_Y = encoder.transform(train_label)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)

loaded_model = load_model("cat_model.h5")
predicted=loaded_model.predict_proba(train_x[:1,0:27],verbose = 1,batch_size=100)
print(predicted)