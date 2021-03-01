# Load libraries
import numpy as np
from numpy import argmax

import requests
from flask import Flask
from flask_caching import Cache
import os

import json
from json import JSONEncoder

import time
from threading import Timer


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_der(x):
    return sigmoid(x) * (1 - sigmoid(x))


def softmax(A):
    expA = np.exp(A)
    return expA / expA.sum(axis=1, keepdims=True)


def predict(wh, bh, wo, bo, X_test):
    zh = np.dot(X_test, wh) + bh
    ah = sigmoid(zh)
    zo = np.dot(ah, wo) + bo
    ao = softmax(zo)
    return ao


# config = {
#     "DEBUG": True,  # some Flask specific configs
#     "CACHE_TYPE": "simple",  # Flask-Caching related configs
#     "CACHE_DEFAULT_TIMEOUT": 300
# }

app = Flask(__name__)

# app.config.from_mapping(config)
# cache = Cache(app)

y_predict_array = []

input_nodes = 2
hidden_nodes = 8
output_labels = 6
wh = np.random.rand(input_nodes, hidden_nodes)
bh = np.random.randn(hidden_nodes)
wo = np.random.rand(hidden_nodes, output_labels)
bo = np.random.randn(output_labels)


@app.route('/ac_control/predict', methods=['GET'])
# @cache.cached(timeout=300)
def predict_data():
    start_time = time.time()
    number_array = predict_output()
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---predict_data %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/roof/wh', methods=['GET'])
# @cache.cached(timeout=300)
def wh_data():
    global wh

    start_time = time.time()
    number_array = wh
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---output_data %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/roof/bh', methods=['GET'])
# @cache.cached(timeout=300)
def bh_data():
    global bh

    start_time = time.time()
    number_array = bh
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---output_data %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/roof/wo', methods=['GET'])
# @cache.cached(timeout=300)
def wo_data():
    global wo

    start_time = time.time()
    number_array = wo
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---output_data %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/roof/bo', methods=['GET'])
# @cache.cached(timeout=300)
def bo_data():
    global bo

    start_time = time.time()
    number_array = bo
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---output_data %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


def get_x_train_data():
    try:
        req = requests.get("http://localhost:3001/ac_control/x_train")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_y_train_data():
    try:
        req = requests.get("http://localhost:3001/ac_control/y_train")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_x_test_data():
    try:
        req = requests.get("http://localhost:3001/ac_control/x_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_y_test_data():
    try:
        req = requests.get("http://localhost:3001/ac_control/y_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_input_data():
    try:
        req = requests.get("http://localhost:3001/ac_control/input")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_fog_wh():
    try:
        req = requests.get("http://localhost:4500/ac/wh")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_fog_bh():
    try:
        req = requests.get("http://localhost:4500/ac/bh")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_fog_wo():
    try:
        req = requests.get("http://localhost:4500/ac/wo")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_fog_bo():
    try:
        req = requests.get("http://localhost:4500/ac/bo")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_cloud_wh():
    try:
        req = requests.get("http://localhost:5500/ac/wh")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_cloud_bh():
    try:
        req = requests.get("http://localhost:5500/ac/bh")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_cloud_wo():
    try:
        req = requests.get("http://localhost:5500/ac/wo")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_cloud_bo():
    try:
        req = requests.get("http://localhost:5500/ac/bo")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_roof_accuracy():
    try:
        req = requests.get("http://localhost:3002/ac_control/accuracy")
        accuracy = float(req.text)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return accuracy


def get_fog_accuracy():
    try:
        req = requests.get("http://localhost:4500/ac/accuracy")
        accuracy = float(req.text)

    except requests.exceptions.ConnectionError:
        return 0.0
    return accuracy


def get_cloud_accuracy():
    try:
        req = requests.get("http://localhost:5500/ac/accuracy")
        accuracy = float(req.text)

    except requests.exceptions.ConnectionError:
        return 0.0
    return accuracy


def model_train():
    global y_predict_array, wh, bh, wo, bo

    y_train = get_y_train_data()
    x_train = get_x_train_data()
    x_test = get_x_test_data()
    y_test = get_y_test_data()

    if len(x_test) == len(y_test) and len(x_train) == len(y_train):

        # create a matrix for one hot encoding
        one_hot_labels = np.zeros((len(y_train), 6))
        for i in range(len(y_train)):
            one_hot_labels[i, y_train[i]] = 1

        # input_nodes = 2
        # hidden_nodes = 8
        # output_labels = 6
        # wh = np.random.rand(input_nodes, hidden_nodes)
        # bh = np.random.randn(hidden_nodes)
        # wo = np.random.rand(hidden_nodes, output_labels)
        # bo = np.random.randn(output_labels)
        lr = 10e-4

        error_cost = []

        for epoch in range(5000):
            ############# feedforward

            # Phase 1
            zh = np.dot(x_train, wh) + bh
            ah = sigmoid(zh)
            zo = np.dot(ah, wo) + bo
            ao = softmax(zo)

            ########## Back Propagation

            ########## Phase 1

            dcost_dzo = ao - one_hot_labels
            dzo_dwo = ah

            dcost_wo = np.dot(dzo_dwo.T, dcost_dzo)

            dcost_bo = dcost_dzo

            ########## Phases 2

            dzo_dah = wo
            dcost_dah = np.dot(dcost_dzo, dzo_dah.T)
            dah_dzh = sigmoid_der(zh)
            dzh_dwh = x_train
            dcost_wh = np.dot(dzh_dwh.T, dah_dzh * dcost_dah)

            dcost_bh = dcost_dah * dah_dzh

            # Update Weights ================

            wh -= lr * dcost_wh
            bh -= lr * dcost_bh.sum(axis=0)

            wo -= lr * dcost_wo
            bo -= lr * dcost_bo.sum(axis=0)

            if epoch % 200 == 0:
                loss = np.sum(-one_hot_labels * np.log(ao))
                # print('Loss function value: ', loss)
                error_cost.append(loss)

        # End of for loop (End of training phase)

        roof_accuracy = get_roof_accuracy()
        fog_accuracy = get_fog_accuracy()
        cloud_accuracy = get_cloud_accuracy()

        if fog_accuracy > roof_accuracy:

            if cloud_accuracy > fog_accuracy:
                wh = get_cloud_wh()
                bh = get_cloud_bh()
                wo = get_cloud_wo()
                bo = get_cloud_bo()
            else:
                wh = get_fog_wh()
                bh = get_fog_bh()
                wo = get_fog_wo()
                bo = get_fog_bo()

            # Make predictions
        predictions = predict(wh, bh, wo, bo, x_test)

        y_predict = []
        for i in range(len(y_test)):
            n = argmax(predictions[i])
            y_predict.append(n)
        y_predict_array = np.array(y_predict)

        print("y_pred", y_predict_array)


def predict_output():
    global y_predict_array
    # model_train()

    return y_predict_array


model_train_automated = RepeatedTimer(15, model_train)

if __name__ == '__main__':
    app.run(port=3003)
