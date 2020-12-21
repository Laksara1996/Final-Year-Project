# Load libraries
import logging

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


config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "simple",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)

app.config.from_mapping(config)
cache = Cache(app)

# estimator = 0

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
logger = logging.getLogger('ac_control_model_microservice')

@app.route('/ac_control/predict', methods=['GET'])
@cache.cached(timeout=300)
def predict_data():
    logger.debug('predict data requested')
    start_time = time.time()
    number_array = predict()
    logger.debug('predicted data:%s',number_array)
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    logger.debug('json file loaded')
    print("---predict_data %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/ac_control/output', methods=['GET'])
@cache.cached(timeout=300)
def output_data():
    start_time = time.time()
    number_array = output()
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---output_data %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


def get_x_train_data():
    logger.debug('get_x_train_data requested')
    try:
        req = requests.get("http://localhost:3001/ac_control/x_train")
        logger.debug('req:%s',req.text)
        decodedArrays = json.loads(req.text)
        logger.debug('Json file loaded')

        finalNumpyArray = np.asarray(decodedArrays["array"])
        logger.debug('value:%s',finalNumpyArray)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_y_train_data():
    logger.debug('get_y_train_data requested')
    try:
        req = requests.get("http://localhost:3001/ac_control/y_train")
        logger.debug('req:%s', req.text)
        decodedArrays = json.loads(req.text)
        logger.debug('Json file loaded')
        finalNumpyArray = np.asarray(decodedArrays["array"])
        logger.debug('value:%s', finalNumpyArray)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_x_test_data():
    try:
        req = requests.get("http://localhost:3001/ac_control/x_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_input_data():
    try:
        req = requests.get("http://localhost:3001/ac_control/input")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def estimator_train():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
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
    x_data = get_x_train_data()
    y_data = get_y_train_data()
    logger.debug('estimator.fit is going to call')
    estimator.fit(x_data, y_data)
    logger.debug('estimator.fit completed')
    return estimator


def predict():
    logger.debug('predict requsted')
    # global estimator
    estimator = estimator_train()
    logger.debug('estimator:%s',estimator)
    predict_value = estimator.predict(get_x_test_data())
    logger.debug('predict_value:%s',predict_value)

    return predict_value


def output():

    logger.debug('output requsted')
    # global estimator
    estimator = estimator_train()
    logger.debug('estimator:%s', estimator)
    output_value = estimator.predict(get_input_data())
    logger.debug('output_value:%s', output_value)

    return output_value


# rt = RepeatedTimer(50, estimator_train)  # it auto-starts, no need of rt.start()

if __name__ == '__main__':
    app.run(port=3003, debug=True)
