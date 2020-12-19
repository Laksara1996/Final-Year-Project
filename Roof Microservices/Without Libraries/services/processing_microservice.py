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


@app.route('/speed/input', methods=['GET'])
# @cache.cached(timeout=300)
def speed_input_list():
    start_time = time.time()
    number_array = speed_train_split("input")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---input %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/speed/x_train', methods=['GET'])
# @cache.cached(timeout=300)
def speed_x_train():
    start_time = time.time()
    number_array = speed_train_split("x_train")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---x_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/speed/x_test', methods=['GET'])
# @cache.cached(timeout=300)
def speed_x_test():
    start_time = time.time()
    number_array = speed_train_split("x_test")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---x_test %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/speed/y_test', methods=['GET'])
# @cache.cached(timeout=300)
def speed_y_test():
    start_time = time.time()
    number_array = speed_train_split("y_test")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_test %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/speed/y_train', methods=['GET'])
# @cache.cached(timeout=300)
def speed_y_train():
    start_time = time.time()
    number_array = speed_train_split("y_train")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/ac_control/input', methods=['GET'])
# @cache.cached(timeout=300)
def ac_control_input_list():
    start_time = time.time()
    number_array = ac_control_train_split("input")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---input %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/ac_control/x_train', methods=['GET'])
# @cache.cached(timeout=300)
def ac_control_x_train():
    start_time = time.time()
    number_array = ac_control_train_split("x_train")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---x_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/ac_control/x_test', methods=['GET'])
# @cache.cached(timeout=300)
def ac_control_x_test():
    start_time = time.time()
    number_array = ac_control_train_split("x_test")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---x_test %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/ac_control/y_test', methods=['GET'])
# @cache.cached(timeout=300)
def ac_control_y_test():
    start_time = time.time()
    number_array = ac_control_train_split("y_test")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_test %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/ac_control/y_train', methods=['GET'])
# @cache.cached(timeout=300)
def ac_control_y_train():
    start_time = time.time()
    number_array = ac_control_train_split("y_train")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


def get_shift_data():
    try:
        req = requests.get("http://localhost:5000//data/shiftNumber")
        req_text = req.text[1:-1]
        number = ""
        number_array = []
        for i in req_text:
            if i == ',':
                number_array.append(number)
                number = ""
                continue
            number = number + i
        number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


def get_pitch_data():
    try:
        req = requests.get("http://localhost:5000//data/pitch")
        req_text = req.text[1:-1]
        number = ""
        number_array = []
        for i in req_text:
            if i == ',':
                number_array.append(number)
                number = ""
                continue
            number = number + i
        number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


def get_rain_intensity_data():
    try:
        req = requests.get("http://localhost:5000//data/rainIntensity")
        req_text = req.text[1:-1]
        number = ""
        number_array = []
        for i in req_text:
            if i == ',':
                number_array.append(number)
                number = ""
                continue
            number = number + i
        number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


def get_visibility_data():
    try:
        req = requests.get("http://localhost:5000//data/visibility")
        req_text = req.text[1:-1]
        number = ""
        number_array = []
        for i in req_text:
            if i == ',':
                number_array.append(number)
                number = ""
                continue
            number = number + i
        number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


def get_driver_rush_data():
    try:
        req = requests.get("http://localhost:5000//data/driver_rush")
        req_text = req.text[1:-1]
        number = ""
        number_array = []
        for i in req_text:
            if i == ',':
                number_array.append(number)
                number = ""
                continue
            number = number + i
        number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


def get_load_data():
    try:
        req = requests.get("http://localhost:5000//data/carLoad")
        req_text = req.text[1:-1]
        number = ""
        number_array = []
        for i in req_text:
            if i == ',':
                number_array.append(number)
                number = ""
                continue
            number = number + i
        number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


def get_vehicle_speed_data():
    try:
        req = requests.get("http://localhost:5000//data/vehicleSpeed")
        req_text = req.text[1:-1]
        number = ""
        number_array = []
        for i in req_text:
            if i == ',':
                number_array.append(number)
                number = ""
                continue
            number = number + i
        number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


@app.route('/ac', methods=['GET'])
# @cache.cached(timeout=300)
def ac_data():
    global air_condition_data_array
    start_time = time.time()
    number_array = air_condition_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/passenger', methods=['GET'])
# @cache.cached(timeout=300)
def passenger_data():
    global passenger_count_data_array
    start_time = time.time()
    number_array = passenger_count_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/window', methods=['GET'])
# @cache.cached(timeout=300)
def window_data():
    global window_opening_data_array
    start_time = time.time()
    number_array = window_opening_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


def get_air_condition_data():
    global air_condition_data_array
    try:
        req = requests.get("http://localhost:5000//data/airConditionStatus")
        req_text = req.text[1:-1]
        number = ""
        number_array = []
        for i in req_text:
            if i == ',':
                number_array.append(number)
                air_condition_data_array.append(float(number))
                number = ""
                continue
            number = number + i
        number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


def get_passenger_count_data():
    global passenger_count_data_array
    try:
        req = requests.get("http://localhost:5000//data/passengerCount")
        req_text = req.text[1:-1]
        number = ""
        number_array = []
        for i in req_text:
            if i == ',':
                number_array.append(number)
                passenger_count_data_array.append(float(number))
                number = ""
                continue
            number = number + i
        number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


def get_window_opening_data():
    global window_opening_data_array
    try:
        req = requests.get("http://localhost:5000//data/windowOpening")
        req_text = req.text[1:-1]
        number = ""
        number_array = []
        for i in req_text:
            if i == ',':
                number_array.append(number)
                window_opening_data_array.append(float(number))
                number = ""
                continue
            number = number + i
        number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


def ac_control_train_split(req):
    global air_condition_data_array, window_opening_data_array, passenger_count_data_array
    window_opening_data = [int(i) for i in window_opening_data_array]
    passenger_count_data = [int(i) for i in passenger_count_data_array]

    air_condition_data = [int(i) for i in air_condition_data_array]

    X = np.array((passenger_count_data, window_opening_data)).T
    Y = air_condition_data

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=0)

    if req == "x_test":
        return X_test
    elif req == "x_train":
        return X_train
    elif req == "y_train":
        return Y_train
    elif req == "input":
        return X
    else:
        return Y_test


def speed_train_split(req):
    shift_data = [float(i) for i in get_shift_data()]
    pitch_data = [int(i) for i in get_pitch_data()]
    passenger_count_data = [int(i) for i in get_passenger_count_data()]
    rain_intensity_data = [int(i) for i in get_rain_intensity_data()]
    visibility_data = [int(i) for i in get_visibility_data()]
    driver_rush_data = [int(i) for i in get_driver_rush_data()]

    speed_data = [float(i) for i in get_vehicle_speed_data()]

    X = np.array(
        (shift_data, pitch_data, passenger_count_data, rain_intensity_data, visibility_data, driver_rush_data)).T
    Y = speed_data

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

    print(X)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=0)

    if req == "x_test":
        return X_test
    elif req == "x_train":
        return X_train
    elif req == "y_train":
        return Y_train
    elif req == "input":
        return X
    else:
        return Y_test


passenger_data_automated = RepeatedTimer(10, get_passenger_count_data)
window_data_automated = RepeatedTimer(10, get_window_opening_data)
ac_data_automated = RepeatedTimer(10, get_air_condition_data)

if __name__ == '__main__':
    app.run(port=3001, debug=True)
