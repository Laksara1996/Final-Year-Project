# Load libraries
from sklearn.metrics import accuracy_score
import numpy as np

import requests
from flask import Flask

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


app = Flask(__name__)

global_ac_accuracy = 0
global_speed_accuracy = 0


@app.route('/ac_control/accuracy', methods=['GET'])
def ac_status_accuracy():
    global global_ac_accuracy

    start_time = time.time()
    accuracy_value = global_ac_accuracy
    print("---ac accuracy %s seconds ---" % (time.time() - start_time))
    return str(accuracy_value)


@app.route('/speed/accuracy', methods=['GET'])
def speed_accuracy_output():
    global global_speed_accuracy

    start_time = time.time()
    accuracy_value = global_speed_accuracy
    print("---speed accuracy %s seconds ---" % (time.time() - start_time))
    return str(accuracy_value)


def get_vehicle_ac_status_accuracy():
    global global_ac_accuracy

    try:
        req = requests.get("http://localhost:4002/ac_control/accuracy")
        accuracy = float(req.text)

        length = get_ac_control_predict_data_length()
        print("ac length", length)
        if length > 1000:
            if accuracy > global_ac_accuracy:
                global_ac_accuracy = accuracy

    except requests.exceptions.ConnectionError:
        return "Service unavailable"


def get_second_vehicle_ac_status_accuracy():
    global global_ac_accuracy

    try:
        req = requests.get("http://localhost:4102/ac_control/accuracy")
        accuracy = float(req.text)

        length = get_second_ac_control_predict_data_length()

        if length > 100:
            if accuracy > global_ac_accuracy:
                global_ac_accuracy = accuracy
        print("ac", global_ac_accuracy)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"


def get_vehicle_speed_accuracy():
    global global_speed_accuracy
    try:
        req = requests.get("http://localhost:4002/speed/accuracy")
        accuracy = float(req.text)

        length = get_speed_predict_data_length()
        print("speed length", length)
        if length > 100:
            if accuracy > global_speed_accuracy:
                global_speed_accuracy = accuracy

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return accuracy


def get_second_vehicle_speed_accuracy():
    global global_speed_accuracy
    try:
        req = requests.get("http://localhost:4102/speed/accuracy")
        accuracy = float(req.text)

        length = get_second_speed_predict_data_length()
        print("speed length", length)
        if length > 100:
            if accuracy > global_speed_accuracy:
                global_speed_accuracy = accuracy
        print("speed", global_speed_accuracy)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return accuracy


def get_ac_control_predict_data_length():
    try:
        req = requests.get("http://localhost:4003/ac_control/predict")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return len(finalNumpyArray)


def get_speed_predict_data_length():
    try:
        req = requests.get("http://localhost:4201/speed/predict")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return len(finalNumpyArray)


def get_second_ac_control_predict_data_length():
    try:
        req = requests.get("http://localhost:4103/ac_control/predict")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return len(finalNumpyArray)


def get_second_speed_predict_data_length():
    try:
        req = requests.get("http://localhost:4301/speed/predict")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return len(finalNumpyArray)


ac_accuracy_automated_1 = RepeatedTimer(40, get_vehicle_ac_status_accuracy)
ac_accuracy_automated_2 = RepeatedTimer(40, get_second_vehicle_ac_status_accuracy)

speed_accuracy_automated_1 = RepeatedTimer(40, get_vehicle_speed_accuracy)
speed_accuracy_automated_2 = RepeatedTimer(40, get_second_vehicle_speed_accuracy)

if __name__ == '__main__':
    app.run(port=4500)
