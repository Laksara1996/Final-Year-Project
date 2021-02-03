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


#
# config = {
#     "DEBUG": True,  # some Flask specific configs
#     "CACHE_TYPE": "simple",  # Flask-Caching related configs
#     "CACHE_DEFAULT_TIMEOUT": 300
# }

app = Flask(__name__)

# app.config.from_mapping(config)
# cache = Cache(app)

air_condition_data_array = []
passenger_count_data_array = []
window_opening_data_array = []
pitch_data_array = []
rain_intensity_data_array = []
visibility_data_array = []
driver_rush_data_array = []
speed_data_array = []

speed_x_train_data = []
speed_x_test_data = []
speed_y_train_data = []
speed_y_test_data = []
speed_input = []

ac_x_train = []
ac_x_test = []
ac_y_train = []
ac_y_test = []
ac_input = []


# Sent Data To the FOG

@app.route('/roof/speed_data', methods=['GET'])
# @cache.cached(timeout=300)
def speed_data():
    global speed_data_array

    start_time = time.time()
    number_array = speed_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    print("----speed amount of data = %s ------" % len(number_array))
    return encodedNumpyData


@app.route('/roof/driver_rush_data', methods=['GET'])
# @cache.cached(timeout=300)
def driver_rush_data():
    global driver_rush_data_array

    start_time = time.time()
    number_array = driver_rush_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    print("----amount of data = %s ------" % len(number_array))
    return encodedNumpyData


@app.route('/roof/visibility_data', methods=['GET'])
# @cache.cached(timeout=300)
def visibility_data():
    global visibility_data_array

    start_time = time.time()
    number_array = visibility_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    print("----amount of data = %s ------" % len(number_array))
    return encodedNumpyData


@app.route('/roof/rain_intensity_data', methods=['GET'])
# @cache.cached(timeout=300)
def rain_intensity_data():
    global rain_intensity_data_array

    start_time = time.time()
    number_array = rain_intensity_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/roof/pitch_data', methods=['GET'])
# @cache.cached(timeout=300)
def pitch_data():
    global pitch_data_array

    start_time = time.time()
    number_array = pitch_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/roof/ac_data', methods=['GET'])
# @cache.cached(timeout=300)
def ac_data():
    global air_condition_data_array

    start_time = time.time()
    number_array = air_condition_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/roof/passenger_data', methods=['GET'])
# @cache.cached(timeout=300)
def passenger_data():
    global passenger_count_data_array
    start_time = time.time()
    number_array = passenger_count_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/roof/window_data', methods=['GET'])
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
    print("----input amount of data = %s ------" % len(number_array))
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
    print("----x_train amount of data = %s ------" % len(number_array))
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
    print("----x_test_amount of data = %s ------" % len(number_array))
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
    print("----y_test_amount of data = %s ------" % len(number_array))
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
    print("----y_train amount of data = %s ------" % len(number_array))
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
    print("----input amount of data = %s ------" % len(number_array))
    return encodedNumpyData


@app.route('/ac_control/x_train', methods=['GET'])
# @cache.cached(timeout=300)
def ac_control_x_train():
    global ac_x_train
    print(type(ac_x_train))
    start_time = time.time()
    number_array = ac_x_train
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---x_train %s seconds ---" % (time.time() - start_time))
    print("----x_train amount of data = %s ------" % len(number_array))
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
    print("----x_test amount of data = %s ------" % len(number_array))
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
    print("----y_test amount of data = %s ------" % len(number_array))
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
    print("----y_train amount of data = %s ------" % len(number_array))
    return encodedNumpyData


# Getting Data From Testbed

def get_pitch_data():
    global pitch_data_array
    try:
        req = requests.get("http://192.168.1.105:5000//data/pitch")
        req_text = req.text[1:-1]
        number = ""
        number_array = []
        for i in req_text:
            if i == ',':
                number_array.append(number)
                pitch_data_array.append(float(number))
                number = ""
                continue
            number = number + i
        if number != "":
            number_array.append(number)
        number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


def get_rain_intensity_data():
    global rain_intensity_data_array
    try:
        req = requests.get("http://192.168.1.105:5000//data/rainIntensity")
        req_text = req.text[1:-1]
        number = ""
        number_array = []
        for i in req_text:
            if i == ',':
                number_array.append(number)
                rain_intensity_data_array.append(float(number))
                number = ""
                continue
            number = number + i
        if number != "":
            number_array.append(number)
        number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


def get_visibility_data():
    global visibility_data_array
    try:
        req = requests.get("http://192.168.1.105:5000//data/visibility")
        req_text = req.text[1:-1]
        number = ""
        number_array = []
        for i in req_text:
            if i == ',':
                number_array.append(number)
                visibility_data_array.append(float(number))
                number = ""
                continue
            number = number + i
        if number != "":
            number_array.append(number)
        number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


def get_driver_rush_data():
    global driver_rush_data_array
    try:
        req = requests.get("http://192.168.1.105:5000//data/driver_rush")
        req_text = req.text[1:-1]
        number = ""
        number_array = []
        for i in req_text:
            if i == ',':
                number_array.append(number)
                driver_rush_data_array.append(float(number))
                number = ""
                continue
            number = number + i
        if number != "":
            number_array.append(number)
        number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


def get_vehicle_speed_data():
    global speed_data_array
    try:
        req = requests.get("http://192.168.1.105:5000//data/vehicleSpeed")
        req_text = req.text[1:-1]
        number = ""
        number_array = []
        for i in req_text:
            if i == ',':
                number_array.append(number)
                speed_data_array.append(float(number))
                number = ""
                continue
            number = number + i
        if number != "":
            number_array.append(number)
        number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


def get_air_condition_data():
    global air_condition_data_array
    try:
        req = requests.get("http://192.168.1.105:5000//data/airConditionStatus")
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
        if number != "":
            number_array.append(number)
        number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


def get_passenger_count_data():
    global passenger_count_data_array
    try:
        req = requests.get("http://192.168.1.105:5000//data/passengerCount")
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
        if number != "":
            number_array.append(number)
        number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


def get_window_opening_data():
    global window_opening_data_array
    try:
        req = requests.get("http://192.168.1.105:5000//data/windowOpening")
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
        if number != "":
            number_array.append(number)
        number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


# AC Train Split

def ac_control_train_split():
    global air_condition_data_array, window_opening_data_array, passenger_count_data_array, ac_x_train, ac_x_test, \
        ac_y_train, ac_y_test, ac_input

    window_opening_data = [int(i) for i in window_opening_data_array]
    passenger_count_data = [int(i) for i in passenger_count_data_array]

    air_condition_data = [int(i) for i in air_condition_data_array]

    X = np.array((passenger_count_data, window_opening_data)).T
    Y = air_condition_data

    if len(X) == len(Y):
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
        # print(speed_y_train_data)


def automated_data_request():
    get_passenger_count_data()
    get_window_opening_data()
    get_air_condition_data()
    get_pitch_data()
    get_rain_intensity_data()
    get_visibility_data()
    get_driver_rush_data()
    get_vehicle_speed_data()


def automated_train_split():
    ac_control_train_split()
    speed_train_split()


data_request_automated = RepeatedTimer(5, automated_data_request)
train_split_automated = RepeatedTimer(11, automated_train_split)

if __name__ == '__main__':
    app.run(port=3001, host='0.0.0.0', debug=True)
