#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:27:15 2020

@author: filippo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D


#%% DATA LOADING

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

train_lab = train['label']
train.drop(columns =['label'], inplace = True)

#%% VISUALIZATION EXAMPLES

plt.figure()
sb.countplot(train_lab)
plt.title('n° of images per class')


plt.figure()
plt.imshow(train.iloc[0].to_numpy().reshape(28,28))
plt.title('first sample')

#%% NORMALIZATION

train = train / 255
test = test / 255

#%% DATA PREPARATION

X_train, X_test, y_train, y_test = train_test_split(train, train_lab, test_size = 0.2, random_state = 12)


X_train = X_train.values.reshape(-1,28,28,1)
y_train = tf.keras.utils.to_categorical(y_train)

X_test = X_test.values.reshape(-1,28,28,1)
y_test = tf.keras.utils.to_categorical(y_test)

#%% NET CREATION

model = Sequential()

model.add(Conv2D(32, kernel_size = (3,3), input_shape = (28,28,1)))
model.add(MaxPool2D())

model.add(Conv2D(64, kernel_size = (3,3)))
model.add(MaxPool2D())

model.add(Flatten())

model.add(Dense(128, activation  = 'relu'))
model.add(Dense(10, activation = 'softmax'))

model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

#%% TRAINING

history = model.fit(X_train, y_train,
          batch_size=128,
          epochs=20,
          validation_data = (X_test,y_test))

#%% ACC & LOSS PLOTS

print('History keys: ',str(history.history.keys()))

plt.figure()
plt.plot(np.arange(len(history.history['loss'])), history.history['loss'])
plt.title('Loss Through Epochs')


plt.figure()
plt.plot(np.arange(len(history.history['loss'])), history.history['accuracy'])
plt.title('Acc Train')

plt.figure()
plt.plot(np.arange(len(history.history['loss'])), history.history['val_accuracy'])
plt.title('Acc Test')

#%% PREDICTIONS

test = test.values.reshape(-1,28,28,1)

y_test = model.predict(test)
y_test = np.argmax(y_test, axis = 1)

#%% RESULTS VISUALIZATION

for i in range(0,10):
    plt.figure()
    plt.imshow(test[i][:,:,0])
    plt.title(str(y_test[i]))
    
    
#%% SUBMISSION

results = pd.Series(y_test, name = 'Label')
IDs = pd.Series(range(1,28001), name = 'ImageId')

submission = pd.concat([IDs, results], axis = 1)

submission.to_csv('submission.csv', index = False)