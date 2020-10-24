# Load libraries
from sklearn.model_selection import train_test_split
import numpy as np

import requests
from flask import Flask, jsonify

import json

from json import JSONEncoder


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


app = Flask(__name__)


@app.route('/lists/air_condition', methods=['GET'])
def air_condition_lists():
    """ Get lists based on air_condition """

    number_array = get_air_condition_data()
    return jsonify(number_array)


@app.route('/lists/passenger_count', methods=['GET'])
def passenger_count_lists():
    """ Get lists based on passenger_count """

    number_array = get_passenger_count_data()
    return jsonify(number_array)


@app.route('/lists/window_opening', methods=['GET'])
def window_opening_lists():
    """ Get lists based on window_opening """

    number_array = get_window_opening_data()
    return jsonify(number_array)


@app.route('/input', methods=['GET'])
def input_list():
    """ Get lists based on window_opening """

    number_array = train_split("input")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    return encodedNumpyData


@app.route('/x_train', methods=['GET'])
def x_train():
    """ Get lists based on window_opening """

    number_array = train_split("x_train")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    return encodedNumpyData


@app.route('/x_test', methods=['GET'])
def x_test():
    """ Get lists based on window_opening """

    number_array = train_split("x_test")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    return encodedNumpyData


@app.route('/y_test', methods=['GET'])
def y_test():
    """ Get lists based on window_opening """

    number_array = train_split("y_test")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    return encodedNumpyData


@app.route('/y_train', methods=['GET'])
def y_train():
    """ Get lists based on window_opening """

    number_array = train_split("y_train")
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    return encodedNumpyData


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


def train_split(req):
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
