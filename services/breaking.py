# import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier


dataset = pd.read_csv("ssdata.csv")
# dataset = pd.read_csv("text.csv")
print(dataset)
df = dataset.iloc[:, [1, 8, 9]]
print(df)

array = df.values
X = array[:, [0, 1, 2]]
print("X")
print(X)

mms = StandardScaler()
mms.fit(df)
normalized_data = mms.transform(df)

###########################################
Sum_of_squared_distances = []
K = range(1, 10)

# Use Elbow method to identify the best k which minimizes the Within-Cluster-Sum-of-Squared(inertia)
for k in K:
    kmeans_model = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans_model.fit(normalized_data)
    Sum_of_squared_distances.append(kmeans_model.inertia_)

# checking for min of K value
print(np.min(Sum_of_squared_distances))
# Plotting for change in K value
plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Sum_of_squared_distances')
plt.show()

########################################
# Doing the clustering
kmeans = KMeans(n_clusters=3, random_state=0)  # from Elbow method we identified n_clusters=3

kmeans = kmeans.fit(normalized_data)

df['labels'] = kmeans.labels_
print("df")
print(df)
Y = df['labels'].values.tolist()

print("Y")
print(Y)


# create the model for the nerural netwok
def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(500, activation='relu', input_dim=3))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(3, activation='softmax'))

    # compile model
    # optimizer='adam' learning rate
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


# create the estimator using keras classifier
estimator = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=20, verbose=0)
# split train and test
print(type(estimator))
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=0)
print("x_train")
print(len(X_train))
# print("x_test")
# print(X_test)
print("y_train")
print(len(Y_train))
# print("y_test")
# print(Y_test)

# fit the estimator
estimator.fit(X_train, Y_train)

# predict test values
print(estimator.predict(X_test))
# find accuracy

predictions = estimator.predict(X_test)
print(predictions)

print('Accuracy: ', accuracy_score(Y_test, predictions))

print('confusion_matrix: ')
print(confusion_matrix(Y_test, predictions))

print('classification_report: ')
print(classification_report(Y_test, predictions))
