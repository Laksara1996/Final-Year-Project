
# Load libraries
import pandas as pd
import numpy as np
from pandas import read_csv
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.metrics import accuracy_score

# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# load the dataset
dataset = pd.read_csv('dataset.csv')
# considering columns (Passenger Count, Air conditioning status, Window Opening)
array = dataset.iloc[:, [8, 10, 11]].values
print(array)

X = array[:,[0,2]]
Y = array[:,1]

# create the model for the nerural netwok
def baseline_model():
	# create model
	model = Sequential()
	model.add(Dense(32, input_dim=2, activation='relu'))
	model.add(Dense(12,  activation='relu'))
	model.add(Dense(4, activation='softmax'))
	# compile model
	model.compile(loss='categorical_crossentropy' , optimizer='adam', metrics=['accuracy'])
	return model

# create the estimator using keras classifier
estimator = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=5, verbose=0)
#split train and test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=0)
# fit the estimator
estimator.fit(X_train, Y_train)
# predict test values
print(estimator.predict(X_test))
# find accuracy
print('Accuracy: ',accuracy_score(Y_test, estimator.predict(X_test)))

###########################################################################################


# load the dataset
dataset = pd.read_csv('dataset.csv')
# considering columns (Passenger Count, Air conditioning status, Window Opening)
array = dataset.iloc[:, [8, 10, 11]].values

X = array[:,[0,2]]
Y = array[:,1]

# print the out put values from specific data set
print(estimator.predict(X))

df = pd.DataFrame(estimator.predict(X), columns = ['output'])
print(df['output'].values.tolist())

