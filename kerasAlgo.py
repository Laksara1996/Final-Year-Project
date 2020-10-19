# Load libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import os,sys
from scipy import stats
import pandas as pd
import numpy as np

import pandas
from tensorflow.keras.models import Sequential 
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline

# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

# load the dataset
dataset = pd.read_csv('dataset.csv')
# considering columns (Passenger Count, Air conditioning status, Window Opening)
array = dataset.iloc[:, [8, 10, 11]].values
print(array)

X = array[:,[0,2]]
Y = array[:,1]

# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(Y)

# print('Accuracy: %.2f' % (accuracy*100))

def baseline_model():
	# create model
	model = Sequential()
	model.add(Dense(32, input_dim=2, activation='tanh'))
	model.add(Dense(3, activation='softmax'))
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model


estimator = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=5, verbose=0)
#split train and test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=0)
estimator.fit(X_train, Y_train)

# #get probabilities
# predictions = estimator.predict_proba(X_test)
# print(predictions)

#print class predictions
print(estimator.predict(X_test))
# print(Y_test)
print('Accuracy: ',accuracy_score(Y_test, estimator.predict(X_test)))
# kfold = KFold(n_splits=10, shuffle=True)
# results = cross_val_score(estimator, X, dummy_y, cv=kfold)
# print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))


# load the dataset
dataset = pd.read_csv('fileID1_ProcessedTripData.csv')
# considering columns (Passenger Count, Air conditioning status, Window Opening)
array = dataset.iloc[:, [8, 10, 11]].values
print(array)

X = array[:,[0,2]]
Y = array[:,1]

print(estimator.predict(X))
df = pd.DataFrame(estimator.predict(X), columns = ['output'])
print(df['output'].values.tolist())

print(Y)