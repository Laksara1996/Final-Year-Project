# Load libraries
from threading import Timer

from sklearn.model_selection import train_test_split
import numpy as np

import requests
from flask import Flask, jsonify
from flask_caching import Cache

import json

from json import JSONEncoder

import time


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


config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "simple",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)

app.config.from_mapping(config)
cache = Cache(app)

air_condition_data_array = []
passenger_count_data_array = []
window_opening_data_array = []

ac_x_train = []
ac_x_test = []
ac_y_train = []
ac_y_test = []
ac_input = []


# AC REST Apis

@app.route('/ac_control/input', methods=['GET'])
# @cache.cached(timeout=300)
def ac_control_input_list():
    global ac_input

    start_time = time.time()
    number_array = ac_input
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---input %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/ac_control/x_train', methods=['GET'])
# @cache.cached(timeout=300)
def ac_control_x_train():
    global ac_x_train

    start_time = time.time()
    number_array = ac_x_train
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---x_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/ac_control/x_test', methods=['GET'])
# @cache.cached(timeout=300)
def ac_control_x_test():
    global ac_x_test

    start_time = time.time()
    number_array = ac_x_test
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---x_test %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/ac_control/y_test', methods=['GET'])
# @cache.cached(timeout=300)
def ac_control_y_test():
    global ac_y_test

    start_time = time.time()
    number_array = ac_y_test
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_test %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/ac_control/y_train', methods=['GET'])
# @cache.cached(timeout=300)
def ac_control_y_train():
    global ac_y_train

    start_time = time.time()
    number_array = ac_y_train
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


def get_air_condition_data_roof():
    global air_condition_data_array
    try:
        req = requests.get("http://localhost:3001/roof/ac_data")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])
        air_condition_data_array = finalNumpyArray.copy()

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_passenger_count_data_roof():
    global passenger_count_data_array
    try:
        req = requests.get("http://localhost:3001/roof/passenger_data")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])
        passenger_count_data_array = finalNumpyArray.copy()

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_window_opening_data_roof():
    global window_opening_data_array
    try:
        req = requests.get("http://localhost:3001/roof/window_data")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])
        window_opening_data_array = finalNumpyArray.copy()

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def ac_control_train_split():
    global air_condition_data_array, window_opening_data_array, passenger_count_data_array, ac_x_train, ac_x_test, \
        ac_y_train, ac_y_test, ac_input

    window_opening_data = [int(i) for i in window_opening_data_array]
    passenger_count_data = [int(i) for i in passenger_count_data_array]

    air_condition_data = [int(i) for i in air_condition_data_array]

    X = np.array((passenger_count_data, window_opening_data)).T
    Y = air_condition_data

    ac_input = X.copy()

    ac_x_train, ac_x_test, ac_y_train, ac_y_test = train_test_split(X, Y, test_size=0.20, random_state=0)


passenger_data_automated = RepeatedTimer(15, get_passenger_count_data_roof)
window_data_automated = RepeatedTimer(15, get_window_opening_data_roof)
ac_data_automated = RepeatedTimer(15, get_air_condition_data_roof)

ac_train_split_automated = RepeatedTimer(20, ac_control_train_split)

if __name__ == '__main__':
    app.run(port=4001, debug=True)
