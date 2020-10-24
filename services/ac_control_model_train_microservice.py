# Load libraries
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier

import requests
from flask import Flask
import os

import json
from json import JSONEncoder


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


app = Flask(__name__)


@app.route('/predict', methods=['GET'])
def predict():
    """ Get lists based on window_opening """

    number_array = predict()
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("Printing JSON serialized NumPy array")
    print(encodedNumpyData)
    return encodedNumpyData


def get_x_train_data():
    try:
        req = requests.get("http://localhost:3001/x_train")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_y_train_data():
    try:
        req = requests.get("http://localhost:3001/y_train")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_x_test_data():
    try:
        req = requests.get("http://localhost:3001/x_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def predict():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    # fix random seed for reproducibility
    seed = 7
    np.random.seed(seed)

    def baseline_model():
        # create model
        model = Sequential()
        model.add(Dense(32, input_dim=2, activation='relu'))
        model.add(Dense(12, activation='relu'))
        model.add(Dense(4, activation='softmax'))

        # compile model
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        return model

    estimator = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=5, verbose=0)

    estimator.fit(get_x_train_data(), get_y_train_data())

    predict = estimator.predict(get_x_test_data())

    return predict

if __name__ == '__main__':
    app.run(port=3003, debug=True)
