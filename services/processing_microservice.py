# Load libraries
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


config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "simple",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)

app.config.from_mapping(config)
cache = Cache(app)


@app.route('/breaking/input', methods=['GET'])
@cache.cached(timeout=300)
def breaking_input_list():
    start_time = time.time()
    number_array = breaking_data_frame()
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---input %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/breaking/x_train', methods=['GET'])
@cache.cached(timeout=300)
def breaking_x_train():
    start_time = time.time()
    number_array = breaking_train_split("x_train")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---x_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/breaking/x_test', methods=['GET'])
@cache.cached(timeout=300)
def breaking_x_test():
    start_time = time.time()
    number_array = breaking_train_split("x_test")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---x_test %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/breaking/y_test', methods=['GET'])
@cache.cached(timeout=300)
def breaking_y_test():
    start_time = time.time()
    number_array = breaking_train_split("y_test")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_test %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/breaking/y_train', methods=['GET'])
@cache.cached(timeout=300)
def breaking_y_train():
    start_time = time.time()
    number_array = breaking_train_split("y_train")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/ac_control/input', methods=['GET'])
@cache.cached(timeout=300)
def ac_control_input_list():
    start_time = time.time()
    number_array = ac_control_train_split("input")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---input %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/ac_control/x_train', methods=['GET'])
@cache.cached(timeout=300)
def ac_control_x_train():
    start_time = time.time()
    number_array = ac_control_train_split("x_train")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---x_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/ac_control/x_test', methods=['GET'])
@cache.cached(timeout=300)
def ac_control_x_test():
    start_time = time.time()
    number_array = ac_control_train_split("x_test")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---x_test %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/ac_control/y_test', methods=['GET'])
@cache.cached(timeout=300)
def ac_control_y_test():
    start_time = time.time()
    number_array = ac_control_train_split("y_test")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_test %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/ac_control/y_train', methods=['GET'])
@cache.cached(timeout=300)
def ac_control_y_train():
    start_time = time.time()
    number_array = ac_control_train_split("y_train")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


def get_speed_data():
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


def get_air_condition_data():
    try:
        req = requests.get("http://localhost:5000//data/airConditionStatus")
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


def get_passenger_count_data():
    try:
        req = requests.get("http://localhost:5000//data/passengerCount")
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


def get_window_opening_data():
    try:
        req = requests.get("http://localhost:5000//data/windowOpening")
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


def get_kmeans_output_data():
    try:
        req = requests.get("http://localhost:3102/breaking/kmeans_output")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def breaking_data_frame():
    speed_data = [float(i) for i in get_speed_data()]
    passenger_count_data = [int(i) for i in get_passenger_count_data()]
    load_data = [int(i) for i in get_load_data()]

    X = np.array((speed_data, passenger_count_data, load_data)).T
    print(X)
    return X


def breaking_train_split(req):
    speed_data = [float(i) for i in get_speed_data()]
    passenger_count_data = [int(i) for i in get_passenger_count_data()]
    load_data = [int(i) for i in get_load_data()]

    X = np.array((speed_data, passenger_count_data, load_data)).T
    Y = get_kmeans_output_data()

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


def ac_control_train_split(req):
    window_opening_data = [int(i) for i in get_window_opening_data()]
    passenger_count_data = [int(i) for i in get_passenger_count_data()]

    air_condition_data = [int(i) for i in get_air_condition_data()]

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


if __name__ == '__main__':
    app.run(port=3001, debug=True)
