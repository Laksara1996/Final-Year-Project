# Load libraries
from sklearn.metrics import accuracy_score
import numpy as np

import requests
from flask import Flask

import json
from json import JSONEncoder

import time

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


app = Flask(__name__)


@app.route('/accuracy', methods=['GET'])
def ac_status_output():
    """ Get lists based on window_opening """
    start_time = time.time()
    accuracy_value = accuracy()
    print("---accuracy %s seconds ---" % (time.time() - start_time))
    return str(accuracy_value)


def get_y_test_data():
    try:
        req = requests.get("http://localhost:3001/y_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_predict_data():
    try:
        req = requests.get("http://localhost:3003/predict")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def accuracy():
    # print("hello")
    accuracy_value = accuracy_score(get_y_test_data(), get_predict_data())
    print('Accuracy: ', accuracy_value)
    return accuracy_value


if __name__ == '__main__':
    app.run(port=3002, debug=True)
