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

seed = 17
np.random.seed(seed)

train_data = "data.csv"
train_df = pd.read_csv(train_data,header=None)
traind_values = train_df.values
print(train_df.head(3))

train_x = traind_values[:,0:28].astype(int)
train_label = traind_values[:,28].astype(int)

encoder = LabelEncoder()
encoder.fit(train_label)
encoded_Y = encoder.transform(train_label)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)

def base_model():
    model = Sequential()
    model.add(Dense(40,input_dim=28,activation='relu'))
    model.add(Dense(32,activation='relu'))
    model.add(Dense(24,activation='relu'))
    model.add(Dense(17,activation='relu'))
    model.add(Dense(15,activation='relu'))
    model.add(Dense(14,activation='relu'))
    model.add(Dense(13,activation='relu'))
    model.add(Dense(10,activation='relu'))
    model.add(Dense(9,activation='relu'))
    model.add(Dense(3,activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

estimater = KerasClassifier(build_fn=base_model,epochs=70,batch_size=18,verbose=0)
estimater.fit(train_x,dummy_y)

kfold = KFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(estimater,train_x, dummy_y, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))  
# Option 1: Save Weights + Architecture
estimater.model.save('cat_model2.h5')
with open('model_architecture.json', 'w') as f:
    f.write(estimater.model.to_json())
