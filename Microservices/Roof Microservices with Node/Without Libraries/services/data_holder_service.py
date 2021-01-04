# Load libraries
import numpy as np
from flask import Flask, request
from flask_caching import Cache
import json
from json import JSONEncoder
import queue


class DataHolder:
    __instance = None

    @staticmethod
    def getInstance():
        if DataHolder.__instance is None:
            DataHolder()
        return DataHolder.__instance

    def __init__(self):
        if DataHolder.__instance is not None:
            raise Exception("This is a singleton")
        else:
            self.__tempdata_q = queue.Queue()
            self.__speeddata_q = queue.Queue()
            DataHolder.__instance = self

    def addData(self, data):
        if data is not None:
            self.__tempdata_q.put(data)

    def getData(self):
        if not self.__tempdata_q.empty():
            return self.__tempdata_q.get(timeout=100)
        return "No data found"

    def addSpeedata(self, data):
        if data is not None:
            self.__speeddata_q.put(data)

    def getSpeedData(self):
        return self.__speeddata_q.get(timeout=100)




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


@app.route('/lst/tempdata', methods=['POST'])
def add_testdata_to_queue():
    record = json.loads(request.data)
    DataHolder.getInstance().addData(record)
    return "success"

@app.route('/lst/gettempdata', methods=['GET'])
def get_testdata_to_queue():
    return DataHolder.getInstance().getData()

if __name__ == '__main__':
    app.run(port=3101, debug=True)
