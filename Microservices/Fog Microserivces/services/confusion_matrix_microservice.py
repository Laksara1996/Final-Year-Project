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


@app.route('/speed/confusion_matrix', methods=['GET'])
def speed_confuion():
    start_time = time.time()
    speed_confusion_matrix_function()
    print("--- %s seconds ---" % (time.time() - start_time))
    return "confusion matrix"
    # return str(confusion_matrix_value)


def get_ac_control_y_test_data():
    try:
        req = requests.get("http://localhost:4001/ac_control/y_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_ac_control_predict_data():
    try:
        req = requests.get("http://localhost:4003/ac_control/predict")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_speed_y_test_data():
    try:
        req = requests.get("http://localhost:4001/speed/y_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_speed_predict_data():
    try:
        req = requests.get("http://localhost:4201/speed/predict")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def ac_control_confusion_matrix_function():
    print('confusion_matrix: ')
    y_test = get_ac_control_y_test_data()
    predict_data = get_ac_control_predict_data()

    print("y_test len", len(y_test))
    print("predict len", len(predict_data))

    confusion_matrix_value = confusion_matrix(y_test[:len(predict_data)], predict_data)
    print(confusion_matrix_value)
    # return confusion_matrix_value


def speed_confusion_matrix_function():
    print('confusion_matrix: ')

    y_test = get_speed_y_test_data()
    predict_data = get_speed_predict_data()

    print("y_test len", len(y_test))
    print("predict len", len(predict_data))

    confusion_matrix_value = confusion_matrix(y_test[:len(predict_data)], predict_data)
    print(confusion_matrix_value)
    # return confusion_matrix_value


if __name__ == '__main__':
    app.run(port=4004, host='0.0.0.0', debug=True)
