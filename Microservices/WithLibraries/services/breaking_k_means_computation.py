# Load libraries
import pandas as pd
import numpy as np

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


@app.route('/breaking/kmeans_output', methods=['GET'])
@cache.cached(timeout=300)
def predict_data():
    start_time = time.time()
    number_array = kmeans_method()
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---kmeans output %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


def get_input_data():
    try:
        req = requests.get("http://localhost:3001/breaking/input")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_elbow_number():
    try:
        req = requests.get("http://localhost:3101/breaking/elbow_number")
        elbow_number = int(req.text)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return elbow_number


def kmeans_method():
    data = get_input_data()
    elbow_number = get_elbow_number()

    df = pd.DataFrame(data)

    mms = StandardScaler()
    mms.fit(df)
    normalized_data = mms.transform(df)

    kmeans = KMeans(n_clusters=elbow_number, random_state=0)  # from Elbow method we identified n_clusters=3

    kmeans = kmeans.fit(normalized_data)

    df['labels'] = kmeans.labels_

    Y = df['labels'].values.tolist()

    return Y


if __name__ == '__main__':
    app.run(port=3102, debug=True)
