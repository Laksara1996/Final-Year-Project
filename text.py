# import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
from sklearn.preprocessing import scale
import os
import seaborn as sns
from sklearn.preprocessing import StandardScaler
#importing the cdist package
from scipy.spatial.distance import cdist
import math

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import os,sys
from scipy import stats

#importing the dataset with pandas
dataset = pd.read_csv("dataset.csv")
# dataset = pd.read_csv("text.csv")
df = dataset.iloc[:, [8, 10, 11]]

print(df)

mms = StandardScaler()
mms.fit(df)
normalized_data = mms.transform(df)
print(normalized_data)

############################################
Sum_of_squared_distances = []
K = range(1,10)

# Use Elbow method to identify the best k which minimizes the Within-Cluster-Sum-of-Squared(inertia)
for k in K: 
    kmeans_model = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans_model.fit(normalized_data)
    Sum_of_squared_distances.append(kmeans_model.inertia_)

# checking for min of K value
print(np.min(Sum_of_squared_distances))
#Plotting for change in K value
plt.plot(K,Sum_of_squared_distances,'bx-')
plt.title('Elbow Method') 
plt.xlabel('Number of clusters') 
plt.ylabel('Sum_of_squared_distances') 
plt.show()

########################################
# Doing the clustering 
kmeans = KMeans(n_clusters = 5, random_state=0)#from Elbow method we identified n_clusters=3

kmeans = kmeans.fit(normalized_data)

df['labels'] = kmeans.labels_
print(df)

print(df['labels'].values.tolist())

array = df.values
X = array[:,0:3]
y = array[:,3]
#split the data set
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=0)

# Make predictions on validation dataset
model = LogisticRegression(solver='liblinear', multi_class='ovr')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)
# Evaluate predictions
print('Accuracy: ',accuracy_score(Y_validation, predictions))

# print('confusion_matrix: ')
# print(confusion_matrix(Y_validation, predictions))

print('classification_report: ')
print(classification_report(Y_validation, predictions))
