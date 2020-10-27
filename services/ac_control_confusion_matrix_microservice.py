# Load libraries
import numpy as np

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


@app.route('/confusion_matrix', methods=['GET'])
def ac_status_output():
    """ Get lists based on window_opening """
    confusion_matrix_function()
    return "hello"
    # return str(confusion_matrix_value)


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


def confusion_matrix_function():

    print('confusion_matrix: ')
    confusion_matrix_value = confusion_matrix(get_y_test_data(), get_predict_data())
    print(confusion_matrix_value)
    # return confusion_matrix_value


if __name__ == '__main__':
    app.run(port=3004, debug=True)
