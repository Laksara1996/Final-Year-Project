# Load libraries
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier

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


class NeuralNetwork:

    def __init__(self):
        # seeding for random number generation
        np.random.seed(1)

        # converting weights to a 2 by 1 matrix with values from -1 to 1 and mean of 0
        self.synaptic_weights = 2 * np.random.random((2, 1)) - 1

    @staticmethod
    def sigmoid(x):
        # applying the sigmoid function
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def sigmoid_derivative(x):
        # computing derivative to the Sigmoid function
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        # training the model to make accurate predictions while adjusting weights continually
        for iteration in range(training_iterations):
            # siphon the training data via  the neuron
            output = self.think(training_inputs)

            # computing error rate for back-propagation
            error = training_outputs - output

            # performing weight adjustments
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))

            self.synaptic_weights += adjustments

    def think(self, inputs):
        # passing the inputs via the neuron to get output
        # converting values to floats
        inputs = inputs.astype(float)
        # print(np.dot(inputs, self.synaptic_weights))
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output


config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "simple",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)

app.config.from_mapping(config)
cache = Cache(app)


y_predict_array = []


@app.route('/ac_control/predict', methods=['GET'])
# @cache.cached(timeout=300)
def predict_data():
    start_time = time.time()
    number_array = predict()
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---predict_data %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/ac_control/output', methods=['GET'])
# @cache.cached(timeout=300)
def output_data():
    start_time = time.time()
    number_array = output()
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


def model_train():
    global y_predict_array
    # initializing the neuron class
    neural_network = NeuralNetwork()

    arrX = np.array(get_x_train_data())
    training_inputs = arrX / 10.

    arrY = np.array([get_y_train_data()]).T
    training_outputs = arrY / 10.

    # training taking place
    neural_network.train(training_inputs, training_outputs, 20000)

    y_predict_array = get_y_test_data().copy()

    x_test_data = get_x_test_data()

    for i in range(0, len(y_predict_array)):

        output_neural = neural_network.think(np.array(x_test_data[i]))

        if output_neural > 0.4 and output_neural != 0.5:
            output_neural = 5
        elif 0.4 > output_neural > 0.3:
            output_neural = 4
        elif 0.3 > output_neural > 0.2:
            output_neural = 3
        elif 0.2 > output_neural > 0.1:
            output_neural = 2
        elif 0.1 > output_neural > 0.05:
            output_neural = 1
        elif output_neural < 0.05 and output_neural == 0.5:
            output_neural = 0
        y_predict_array[i] = output_neural

    print(y_predict_array)
    return y_predict_array


def predict():
    global y_predict_array
    # y_predict = model_train()

    return y_predict_array


def output():
    global y_predict_array
    # y_predict = model_train()

    return y_predict_array


model_train_automated = RepeatedTimer(10, model_train)

if __name__ == '__main__':
    app.run(port=3003, debug=True)
