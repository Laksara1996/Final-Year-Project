# Load libraries
from sklearn.metrics import accuracy_score
import numpy as np

import requests
from flask import Flask

import json
from json import JSONEncoder

import time
from threading import Timer

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


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

# Use the application default credentials
cred = credentials.Certificate(
    'F:\ACADEMIC\Semester 7\CO 421 CO 425 Final Year Project\Project\Microservices-python-implmentation\FinalYearProject-e8c0676a307f.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection('Global_Accuracy').document('test')

ac_accuracy = 0
speed_accuracy = 0


@app.route('/ac_control/accuracy', methods=['GET'])
def ac_status_accuracy():
    global ac_accuracy

    start_time = time.time()
    accuracy_value = ac_accuracy
    print("---ac accuracy %s seconds ---" % (time.time() - start_time))
    return str(accuracy_value)


@app.route('/speed/accuracy', methods=['GET'])
def speed_accuracy_output():
    global speed_accuracy
    start_time = time.time()
    accuracy_value = speed_accuracy
    print("---speed accuracy %s seconds ---" % (time.time() - start_time))
    return str(accuracy_value)


def get_ac_control_y_test_data():
    try:
        req = requests.get("http://localhost:5001/ac_control/y_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_ac_control_predict_data():
    try:
        req = requests.get("http://localhost:5003/ac_control/predict")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_speed_y_test_data():
    try:
        req = requests.get("http://localhost:5001/speed/y_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_speed_predict_data():
    try:
        req = requests.get("http://localhost:5201/speed/predict")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_ac_cloud_wh():
    try:
        req = requests.get("http://localhost:5201/cloud/wh")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_ac_cloud_bh():
    try:
        req = requests.get("http://localhost:5201/cloud/bh")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_ac_cloud_wo():
    try:
        req = requests.get("http://localhost:5201/cloud/wo")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_ac__cloud_bo():
    try:
        req = requests.get("http://localhost:5201/cloud/bo")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_speed_cloud_wh():
    try:
        req = requests.get("http://localhost:5003/cloud/wh")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_speed_cloud_bh():
    try:
        req = requests.get("http://localhost:5003/cloud/bh")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_speed_cloud_wo():
    try:
        req = requests.get("http://localhost:5003/cloud/wo")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_speed_cloud_bo():
    try:
        req = requests.get("http://localhost:5003/cloud/bo")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def ac_control_accuracy():
    global ac_accuracy

    y_test = get_ac_control_y_test_data()
    predict_data = get_ac_control_predict_data()

    print("predict len", len(predict_data))
    print("y_test len", len(y_test[:len(predict_data)]))

    ac_accuracy = accuracy_score(y_test[:len(predict_data)], predict_data)
    print('Accuracy: ', ac_accuracy)


def speed_accuracy_calculator():
    global speed_accuracy

    y_test = get_speed_y_test_data()
    predict_data = get_speed_predict_data()

    print("predict len", len(predict_data))
    print("y_test len", len(y_test[:len(predict_data)]))

    speed_accuracy = accuracy_score(y_test[:len(predict_data)], predict_data)
    print('Accuracy: ', ac_accuracy)


def send_accuracy_data():
    global speed_accuracy, ac_accuracy

    ac_wh = get_ac_cloud_wh()
    ac_bh = get_ac_cloud_bh()
    ac_wo = get_ac_cloud_wo()
    ac_bo = get_ac__cloud_bo()

    speed_wh = get_speed_cloud_wh()
    speed_bh = get_speed_cloud_bh()
    speed_wo = get_speed_cloud_wo()
    speed_bo = get_speed_cloud_bo()

    doc = doc_ref.get()
    if doc.exists:
        result = doc.to_dict()
        if result["ac_accuracy"] < ac_accuracy:
            doc_ref.set({
                'ac_accuracy': ac_accuracy,
                'ac_wh': ac_wh,
                'ac_bh': ac_bh,
                'ac_wo': ac_wo,
                'ac_bo': ac_bo,
            })
        if result["speed_accuracy"] < speed_accuracy:
            doc_ref.set({
                'speed_accuracy': speed_accuracy,
                'speed_wh': speed_wh,
                'speed_bh': speed_bh,
                'speed_wo': speed_wo,
                'speed_bo': speed_bo,
            })
    else:
        print(u'No such document!')


ac_accuracy_automated = RepeatedTimer(100, ac_control_accuracy)
speed_accuracy_automated = RepeatedTimer(100, speed_accuracy_calculator)


data_sent_automated = RepeatedTimer(110, send_accuracy_data)

if __name__ == '__main__':
    app.run(port=5002, debug=True)
