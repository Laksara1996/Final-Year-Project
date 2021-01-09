# Load libraries
import numpy as np
from flask import Flask, request
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
            self.__cloud_wh_data_q = queue.Queue()
            self.__cloud_bh_data_q = queue.Queue()
            self.__cloud_wo_data_q = queue.Queue()
            self.__cloud_bo_data_q = queue.Queue()
            self.__cloud_accuracy_data_q = queue.Queue()
            DataHolder.__instance = self

    def add_cloud_wh_data(self, data):
        if data is not None:
            self.__cloud_wh_data_q.put(data)

    def get_cloud_wh_data(self):
        if not self.__cloud_wh_data_q.empty():
            return self.__cloud_wh_data_q.get(timeout=100)
        return "No data found"

    def add_cloud_bh_data(self, data):
        if data is not None:
            self.__cloud_bh_data_q.put(data)

    def get_cloud_bh_data(self):
        if not self.__cloud_bh_data_q.empty():
            return self.__cloud_bh_data_q.get(timeout=100)
        return "No data found"

    def add_cloud_wo_data(self, data):
        if data is not None:
            self.__cloud_wo_data_q.put(data)

    def get_cloud_wo_data(self):
        if not self.__cloud_wo_data_q.empty():
            return self.__cloud_wo_data_q.get(timeout=100)
        return "No data found"

    def add_cloud_bo_data(self, data):
        if data is not None:
            self.__cloud_bo_data_q.put(data)

    def get_cloud_bo_data(self):
        if not self.__cloud_bo_data_q.empty():
            return self.__cloud_bo_data_q.get(timeout=100)
        return "No data found"

    def add_cloud_acuracy_Data(self, data):
        if data is not None:
            self.__cloud_accuracy_data_q.put(data)

    def get_cloud_accuracy_Data(self):
        if not self.__cloud_accuracy_data_q.empty():
            return self.__cloud_accuracy_data_q.get(timeout=100)
        return "No data found"


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


@app.route('/cloud/ac_control/add_cloud_wh', methods=['POST'])
def add_cloud_data_to_queue():
    record = json.loads(request.data)
    DataHolder.getInstance().add_cloud_wh_data(record)
    return "success"


@app.route('/cloud/speed/get_cloud_wh', methods=['GET'])
def get_cloud_data_to_queue():
    return DataHolder.getInstance().get_cloud_wh_data()


@app.route('/cloud/speed/add_cloud_bh', methods=['POST'])
def add_cloud_data_to_queue():
    record = json.loads(request.data)
    DataHolder.getInstance().add_cloud_bh_data(record)
    return "success"


@app.route('/cloud/speed/get_cloud_bh', methods=['GET'])
def get_cloud_data_to_queue():
    return DataHolder.getInstance().get_cloud_bh_data()


@app.route('/cloud/speed/add_cloud_wo', methods=['POST'])
def add_cloud_data_to_queue():
    record = json.loads(request.data)
    DataHolder.getInstance().add_cloud_wo_data(record)
    return "success"


@app.route('/cloud/speed/get_cloud_wo', methods=['GET'])
def get_cloud_data_to_queue():
    return DataHolder.getInstance().get_cloud_wo_data()


@app.route('/cloud/speed/add_cloud_bo', methods=['POST'])
def add_cloud_data_to_queue():
    record = json.loads(request.data)
    DataHolder.getInstance().add_cloud_bo_data(record)
    return "success"


@app.route('/cloud/speed/get_cloud_bo', methods=['GET'])
def get_cloud_data_to_queue():
    return DataHolder.getInstance().get_cloud_bo_data()


@app.route('/cloud/speed/add_cloud_accuracy', methods=['POST'])
def add_cloud_data_to_queue():
    record = json.loads(request.data)
    DataHolder.getInstance().add_cloud_acuracy_Data(record)
    return "success"


@app.route('/cloud/speed/get_cloud_accuracy', methods=['GET'])
def get_cloud_data_to_queue():
    return DataHolder.getInstance().get_cloud_accuracy_Data()


if __name__ == '__main__':
    app.run(port=3102, host='0.0.0.0', debug=True)
