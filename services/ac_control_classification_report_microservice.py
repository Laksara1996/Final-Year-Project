# Load libraries
import numpy as np

from sklearn.metrics import classification_report

import requests
from flask import Flask

import json
from json import JSONEncoder

import time

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


app = Flask(__name__)


@app.route('/classification_report', methods=['GET'])
def classification_report_output():
    """ Get lists based on window_opening """
    start_time = time.time()
    classification_report_function()
    print("---classification_report %s seconds ---" % (time.time() - start_time))
    return "classification report"
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


def classification_report_function():

    print('classification_report: ')
    print(classification_report(get_y_test_data(), get_predict_data()))


if __name__ == '__main__':
    app.run(port=3005, debug=True)
