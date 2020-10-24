# Load libraries
from sklearn.metrics import accuracy_score
import numpy as np

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import requests
from flask import Flask

import json
from json import JSONEncoder


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


app = Flask(__name__)


@app.route('/accuracy', methods=['GET'])
def ac_status_output():
    """ Get lists based on window_opening """
    accuracy_value = accuracy()
    return str(accuracy_value)


def get_y_test_data():
    try:
        req = requests.get("http://localhost:3001/y_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_predict_data():
    try:
        req = requests.get("http://localhost:3003/predict")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def accuracy():
    print("hello")
    accuracy_value = accuracy_score(get_y_test_data(), get_predict_data())
    print('Accuracy: ', accuracy_value)

    print('confusion_matrix: ')
    print(confusion_matrix(get_y_test_data(), get_predict_data()))

    print('classification_report: ')
    print(classification_report(get_y_test_data(), get_predict_data()))
    return accuracy_value


if __name__ == '__main__':
    app.run(port=3002, debug=True)
