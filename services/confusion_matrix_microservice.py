# Load libraries
import numpy as np

from sklearn.metrics import confusion_matrix

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


@app.route('/ac_control/confusion_matrix', methods=['GET'])
def ac_status_confuion():
    start_time = time.time()
    ac_control_confusion_matrix_function()
    print("--- %s seconds ---" % (time.time() - start_time))
    return "confusion matrix"
    # return str(confusion_matrix_value)


@app.route('/breaking/confusion_matrix', methods=['GET'])
def breaking_confuion():
    start_time = time.time()
    breaking_confusion_matrix_function()
    print("--- %s seconds ---" % (time.time() - start_time))
    return "confusion matrix"
    # return str(confusion_matrix_value)


def get_ac_control_y_test_data():
    try:
        req = requests.get("http://localhost:3001/ac_control/y_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_ac_control_predict_data():
    try:
        req = requests.get("http://localhost:3003/ac_control/predict")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_breaking_y_test_data():
    try:
        req = requests.get("http://localhost:3001/breaking/y_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_breaking_predict_data():
    try:
        req = requests.get("http://localhost:3102/breaking/predict")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def ac_control_confusion_matrix_function():
    print('confusion_matrix: ')
    confusion_matrix_value = confusion_matrix(get_ac_control_y_test_data(), get_ac_control_predict_data())
    print(confusion_matrix_value)
    # return confusion_matrix_value


def breaking_confusion_matrix_function():
    print('confusion_matrix: ')
    confusion_matrix_value = confusion_matrix(get_breaking_y_test_data(), get_breaking_predict_data())
    print(confusion_matrix_value)
    # return confusion_matrix_value


if __name__ == '__main__':
    app.run(port=3004, debug=True)
