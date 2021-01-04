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
pitch_data_array = []
rain_intensity_data_array = []
visibility_data_array = []
driver_rush_data_array = []
speed_data_array = []

ac_x_train = []
ac_x_test = []
ac_y_train = []
ac_y_test = []
ac_input = []

speed_x_train_data = []
speed_x_test_data = []
speed_y_train_data = []
speed_y_test_data = []
speed_input = []


# Sent Data To the Cloud

@app.route('/fog/speed_data', methods=['GET'])
# @cache.cached(timeout=300)
def speed_data():
    global speed_data_array

    start_time = time.time()
    number_array = speed_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/fog/driver_rush_data', methods=['GET'])
# @cache.cached(timeout=300)
def driver_rush_data():
    global driver_rush_data_array

    start_time = time.time()
    number_array = driver_rush_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/fog/visibility_data', methods=['GET'])
# @cache.cached(timeout=300)
def visibility_data():
    global visibility_data_array

    start_time = time.time()
    number_array = visibility_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/fog/rain_intensity_data', methods=['GET'])
# @cache.cached(timeout=300)
def rain_intensity_data():
    global rain_intensity_data_array

    start_time = time.time()
    number_array = rain_intensity_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/fog/pitch_data', methods=['GET'])
# @cache.cached(timeout=300)
def pitch_data():
    global pitch_data_array

    start_time = time.time()
    number_array = pitch_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/fog/ac_data', methods=['GET'])
# @cache.cached(timeout=300)
def ac_data():
    global air_condition_data_array

    start_time = time.time()
    number_array = air_condition_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/fog/passenger_data', methods=['GET'])
# @cache.cached(timeout=300)
def passenger_data():
    global passenger_count_data_array
    start_time = time.time()
    number_array = passenger_count_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/fog/window_data', methods=['GET'])
# @cache.cached(timeout=300)
def window_data():
    global window_opening_data_array
    start_time = time.time()
    number_array = window_opening_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


# Speed REST Apis

@app.route('/speed/input', methods=['GET'])
# @cache.cached(timeout=300)
def speed_input_list():
    global speed_input
    start_time = time.time()
    number_array = speed_input
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---input %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/speed/x_train', methods=['GET'])
# @cache.cached(timeout=300)
def speed_x_train():
    global speed_x_train_data

    start_time = time.time()
    number_array = speed_x_train_data
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---x_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/speed/x_test', methods=['GET'])
# @cache.cached(timeout=300)
def speed_x_test():
    global speed_x_test_data
    start_time = time.time()
    number_array = speed_x_test_data
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---x_test %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/speed/y_test', methods=['GET'])
# @cache.cached(timeout=300)
def speed_y_test():
    global speed_y_test_data
    start_time = time.time()
    number_array = speed_y_test_data
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_test %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/speed/y_train', methods=['GET'])
# @cache.cached(timeout=300)
def speed_y_train():
    global speed_y_train_data
    start_time = time.time()
    number_array = speed_y_train_data
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


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


def get_speed_data_roof():
    global speed_data_array
    try:
        req = requests.get("http://localhost:3001/roof/speed_data")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])
        speed_data_array = finalNumpyArray.copy()

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_driver_rush_data_roof():
    global driver_rush_data_array
    try:
        req = requests.get("http://localhost:3001/roof/driver_rush_data")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])
        driver_rush_data_array = finalNumpyArray.copy()

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_visibility_data_roof():
    global visibility_data_array
    try:
        req = requests.get("http://localhost:3001/roof/visibility_data")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])
        visibility_data_array = finalNumpyArray.copy()

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_rain_intensity_data_roof():
    global rain_intensity_data_array
    try:
        req = requests.get("http://localhost:3001/roof/rain_intensity_data")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])
        rain_intensity_data_array = finalNumpyArray.copy()

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_pitch_data_roof():
    global pitch_data_array
    try:
        req = requests.get("http://localhost:3001/roof/pitch_data")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])
        pitch_data_array = finalNumpyArray.copy()

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


# AC Train Split

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


# Speed Train Split

def speed_train_split():
    global pitch_data_array, passenger_count_data_array, rain_intensity_data_array, \
        visibility_data_array, driver_rush_data_array, speed_data_array, \
        speed_x_train_data, speed_x_test_data, speed_y_train_data, speed_y_test_data, speed_input

    pitch_data = [int(i) for i in pitch_data_array]
    passenger_count_data = [int(i) for i in passenger_count_data_array]
    rain_intensity_data = [int(i) for i in rain_intensity_data_array]
    visibility_data = [int(i) for i in visibility_data_array]
    driver_rush_data = [int(i) for i in driver_rush_data_array]

    speed_data = [float(i) for i in speed_data_array]

    X = np.array(
        (pitch_data, passenger_count_data, rain_intensity_data, visibility_data, driver_rush_data)).T
    Y = speed_data

    if len(X) == len(Y):

        for i in range(len(Y)):
            if Y[i] == 0:
                Y[i] = 0
            elif Y[i] <= 5:
                Y[i] = 1
            elif Y[i] <= 10:
                Y[i] = 2
            elif Y[i] <= 15:
                Y[i] = 3
            elif Y[i] <= 20:
                Y[i] = 4
            elif Y[i] > 20:
                Y[i] = 5
                Y[i] = 5

        speed_input = X.copy()

        speed_x_train_data, speed_x_test_data, speed_y_train_data, speed_y_test_data = train_test_split(X, Y,
                                                                                                        test_size=0.20
                                                                                                        ,
                                                                                                        random_state=0)


passenger_data_automated = RepeatedTimer(15, get_passenger_count_data_roof)
window_data_automated = RepeatedTimer(15, get_window_opening_data_roof)
ac_data_automated = RepeatedTimer(15, get_air_condition_data_roof)
pitch_data_automated = RepeatedTimer(15, get_pitch_data_roof)
rain_intensity_data_automated = RepeatedTimer(15, get_rain_intensity_data_roof)
visibility_data_automated = RepeatedTimer(15, get_visibility_data_roof)
driver_rush_data_automated = RepeatedTimer(15, get_driver_rush_data_roof)
speed_data_automated = RepeatedTimer(15, get_speed_data_roof)

ac_train_split_automated = RepeatedTimer(20, ac_control_train_split)
speed_train_split_automated = RepeatedTimer(20, speed_train_split)

if __name__ == '__main__':
    app.run(port=4001, debug=True)
