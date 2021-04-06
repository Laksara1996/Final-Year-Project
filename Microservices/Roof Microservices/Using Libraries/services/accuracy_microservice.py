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


@app.route('/ac_control/accuracy', methods=['GET'])
def ac_status_accuracy():
    start_time = time.time()
    accuracy_value = ac_control_accuracy()
    print("---ac accuracy %s seconds ---" % (time.time() - start_time))
    return str(accuracy_value)


@app.route('/breaking/accuracy', methods=['GET'])
def breaking_accuracy():
    start_time = time.time()
    accuracy_value = breaking_accuracy()
    print("---break accuracy %s seconds ---" % (time.time() - start_time))
    return str(accuracy_value)


@app.route('/speed/accuracy', methods=['GET'])
def speed_accuracy():
    start_time = time.time()
    accuracy_value = speed_accuracy()
    print("---speed accuracy %s seconds ---" % (time.time() - start_time))
    return str(accuracy_value)


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
        req = requests.get("http://localhost:3103/breaking/predict")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_speed_y_test_data():
    try:
        req = requests.get("http://localhost:3001/speed/y_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_speed_predict_data():
    try:
        req = requests.get("http://localhost:3201/speed/predict")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def ac_control_accuracy():
    # print("hello")
    accuracy_value = accuracy_score(get_ac_control_y_test_data(), get_ac_control_predict_data())
    print('Accuracy: ', accuracy_value)
    return accuracy_value


def breaking_accuracy():
    # print("hello")
    accuracy_value = accuracy_score(get_breaking_y_test_data(), get_breaking_predict_data())
    print('Accuracy: ', accuracy_value)
    return accuracy_value


def speed_accuracy():
    # print("hello")
    accuracy_value = accuracy_score(get_speed_y_test_data(), get_speed_predict_data())
    print('Accuracy: ', accuracy_value)
    return accuracy_value


if __name__ == '__main__':
    app.run(port=3002, debug=True)