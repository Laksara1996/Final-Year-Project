# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

import requests
from flask import Flask
from flask_caching import Cache

import json
from json import JSONEncoder

import time


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "simple",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)

app.config.from_mapping(config)
cache = Cache(app)


@app.route('/breaking/elbow_number', methods=['GET'])
@cache.cached(timeout=300)
def predict_data():
    start_time = time.time()
    elbow_number = elbow_method()
    print("---predict_data %s seconds ---" % (time.time() - start_time))
    return str(elbow_number)


def get_input_data():
    try:
        req = requests.get("http://localhost:3001/breaking/input")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def elbow_method():
    data = get_input_data()
    print(data)

    df = pd.DataFrame(data)
    print(df)
    mms = StandardScaler()
    mms.fit(df)
    normalized_data = mms.transform(df)

    Sum_of_squared_distances = []
    K = range(1, 10)

    # Use Elbow method to identify the best k which minimizes the Within-Cluster-Sum-of-Squared(inertia)
    for k in K:
        kmeans_model = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10, random_state=0)
        kmeans_model.fit(normalized_data)
        Sum_of_squared_distances.append(kmeans_model.inertia_)

    # checking for min of K value
    print(np.min(Sum_of_squared_distances))

    # checking for min of K value
    arr = Sum_of_squared_distances
    diff = []
    r = range(0, 8)
    for i in r:
        n = arr[i] - arr[i + 1]
        diff.append(n)

    q = range(0, 8)
    for i in q:
        lbow = diff[i + 1] * 3
        if diff[i] < lbow:
            number_of_clusters = i + 1
            # print(number_of_clusters)
            break

    # Plotting for change in K value
    # plt.plot(K, Sum_of_squared_distances, 'bx-')
    # plt.title('Elbow Method')
    # plt.xlabel('Number of clusters')
    # plt.ylabel('Sum_of_squared_distances')
    # plt.show()

    return number_of_clusters


if __name__ == '__main__':
    app.run(port=3101, debug=True)
