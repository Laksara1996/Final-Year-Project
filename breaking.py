# Load libraries

import pandas as pd
import numpy as np
from pandas import read_csv
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
import datetime
from keras.layers import Dropout
a = datetime.datetime.now()
# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# load the dataset
dataset = pd.read_csv('datasetold.csv')
# considering columns (Passenger Count, Air conditioning status, Window Opening)
array = dataset.iloc[:, [1, 8, 9, 17]].values
print(array)

X = array[:,[0,1,2]]
Y = array[:,3]

# create the model for the nerural netwok
def baseline_model():
	# create model
	model = Sequential()
	model.add(Dense(500, activation='relu', input_dim=3))
	model.add(Dense(100, activation='relu'))
	model.add(Dense(50, activation='relu'))
	model.add(Dense(6, activation='softmax'))

	# compile model
	# optimizer='adam' learning rate
	model.compile(loss='categorical_crossentropy' , optimizer='adam', metrics=['accuracy'])
	return model

# create the estimator using keras classifier
estimator = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=20, verbose=0)
#split train and test
print(type(estimator))
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=0)
b = datetime.datetime.now()
print(b-a)
# fit the estimator
estimator.fit(X_train, Y_train)
c = datetime.datetime.now()
print(c-a)
# predict test values
print(estimator.predict(X_test))
# find accuracy

predictions = estimator.predict(X_test)
print(predictions)

print('Accuracy: ',accuracy_score(Y_test,predictions))
d = datetime.datetime.now()
print(d-a)
print('confusion_matrix: ')
print(confusion_matrix(Y_test, predictions))
e = datetime.datetime.now()
print(e-a)

print('classification_report: ')
print(classification_report(Y_test, predictions))
f = datetime.datetime.now()
print(f-a)


##############################################################################################


# load the dataset
dataset = pd.read_csv('datasetold.csv')
# considering columns (Passenger Count, Air conditioning status, Window Opening)
array = dataset.iloc[:, [1, 8, 9,17]].values
print(array)

X = array[:,[0,1,2]]
Y = array[:,3]

# print the out put values from specific data set
print(estimator.predict(X))
# print(estimator.predict([[5,2],[1,0],[4,2]]))
# df = pd.DataFrame(estimator.predict(X), columns = ['output'])
# print(df['output'].values.tolist())

d = datetime.datetime.now()
print(d-a)