# Load libraries
from threading import Timer

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


@app.route('/speed/x_train', methods=['GET'])
@cache.cached(timeout=300)
def speed_input_list():
    start_time = time.time()
    number_array = get_speed_x_train_data()
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---input %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


def get_speed_x_train_data():
    try:
        req = requests.get("http://localhost:3001/speed/x_train")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

        print("y train length")
        print(len(finalNumpyArray))

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


# rt = RepeatedTimer(3, get_speed_data)  # it auto-starts, no need of rt.start()

if __name__ == '__main__':
    app.run(port=4001, debug=True)
