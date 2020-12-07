# Load libraries
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier

import requests
from flask import Flask
from flask_caching import Cache
import os

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


@app.route('/breaking/predict', methods=['GET'])
@cache.cached(timeout=300)
def predict_data():

    start_time = time.time()
    number_array = predict()
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---predict_data %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/breaking/output', methods=['GET'])
@cache.cached(timeout=300)
def output_data():

    start_time = time.time()
    number_array = output()
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---output_data %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


def get_x_train_data():
    try:
        req = requests.get("http://localhost:3001/breaking/x_train")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

        print("x train length")
        print(len(finalNumpyArray))

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_y_train_data():
    try:
        req = requests.get("http://localhost:3001/breaking/y_train")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

        print("y train length")
        print(len(finalNumpyArray))

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_x_test_data():
    try:
        req = requests.get("http://localhost:3001/breaking/x_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_input_data():
    try:
        req = requests.get("http://localhost:3001/breaking/input")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def estimator_train():
    # os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    # seed = 7
    # np.random.seed(seed)

    def baseline_model():
        # create model
        model = Sequential()
        model.add(Dense(500, activation='relu', input_dim=3))
        model.add(Dense(100, activation='relu'))
        model.add(Dense(50, activation='relu'))
        model.add(Dense(3, activation='softmax'))

        # compile model
        # optimizer='adam' learning rate
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    estimator = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=20, verbose=0)
    estimator.fit(get_x_train_data(), get_y_train_data())
    return estimator


def predict():
    estimator = estimator_train()
    predict_value = estimator.predict(get_x_test_data())
    print(predict_value)
    return predict_value


def output():
    estimator = estimator_train()
    output_value = estimator.predict(get_input_data())
    print(output_value)
    return output_value


if __name__ == '__main__':
    app.run(port=3103, debug=True)
