# Load libraries
import numpy as np
from flask import Flask, request
import json
from json import JSONEncoder
import queue
import requests


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
            self.__fog_wh_data_q = queue.Queue()
            self.__fog_bh_data_q = queue.Queue()
            self.__fog_wo_data_q = queue.Queue()
            self.__fog_bo_data_q = queue.Queue()
            self.__fog_accuracy_data_q = queue.Queue()
            DataHolder.__instance = self

    def add_fog_wh_data(self, data):
        if data is not None:
            self.__fog_wh_data_q.put(data)

    def get_fog_wh_data(self):
        if not self.__fog_wh_data_q.empty():
            return self.__fog_wh_data_q.get(timeout=100)
        return "No data found"

    def add_fog_bh_data(self, data):
        if data is not None:
            self.__fog_bh_data_q.put(data)

    def get_fog_bh_data(self):
        if not self.__fog_bh_data_q.empty():
            return self.__fog_bh_data_q.get(timeout=100)
        return "No data found"

    def add_fog_wo_data(self, data):
        if data is not None:
            self.__fog_wo_data_q.put(data)

    def get_fog_wo_data(self):
        if not self.__fog_wo_data_q.empty():
            return self.__fog_wo_data_q.get(timeout=100)
        return "No data found"

    def add_fog_bo_data(self, data):
        if data is not None:
            self.__fog_bo_data_q.put(data)

    def get_fog_bo_data(self):
        if not self.__fog_bo_data_q.empty():
            return self.__fog_bo_data_q.get(timeout=100)
        return "No data found"

    def add_fog_acuracy_Data(self, data):
        if data is not None:
            self.__fog_accuracy_data_q.put(data)

    def get_fog_accuracy_Data(self):
        if not self.__fog_accuracy_data_q.empty():
            return self.__fog_accuracy_data_q.get(timeout=100)
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


@app.route('/fog/ac_control/add_fog_wh', methods=['POST'])
def add_fog_data_to_queue():
    record = json.loads(request.data)
    DataHolder.getInstance().add_fog_wh_data(record)
    return "success"

@app.route('/fog/speed/get_fog_wh', methods=['GET'])
def get_fog_data_to_queue():
    # return DataHolder.getInstance().get_fog_wh_data()
    try:
        outData = '{ "name":"John", "age":30, "city":"New York"}'
        # jsondata = json.loads(outData)
        req = requests.post("http://localhost:3102/cloud/ac_control/add_cloud_wh",data=outData)
        requestStatus = req.text
    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return "success"


@app.route('/fog/speed/add_fog_bh', methods=['POST'])
def add_fog_data_to_queue1():
    record = json.loads(request.data)
    DataHolder.getInstance().add_fog_bh_data(record)
    return "success"

@app.route('/fog/speed/get_fog_bh', methods=['GET'])
def get_fog_data_to_queue1():
    return DataHolder.getInstance().get_fog_bh_data()



@app.route('/fog/speed/add_fog_wo', methods=['POST'])
def add_fog_data_to_queue2():
    record = json.loads(request.data)
    DataHolder.getInstance().add_fog_wo_data(record)
    return "success"

@app.route('/fog/speed/get_fog_wo', methods=['GET'])
def get_fog_data_to_queue2():
    return DataHolder.getInstance().get_fog_wo_data()



@app.route('/fog/speed/add_fog_bo', methods=['POST'])
def add_fog_data_to_queue3():
    record = json.loads(request.data)
    DataHolder.getInstance().add_fog_bo_data(record)
    return "success"

@app.route('/fog/speed/get_fog_bo', methods=['GET'])
def get_fog_data_to_queue3():
    return DataHolder.getInstance().get_fog_bo_data()



@app.route('/fog/speed/add_fog_accuracy', methods=['POST'])
def add_fog_data_to_queue4():
    record = json.loads(request.data)
    DataHolder.getInstance().add_fog_acuracy_Data(record)
    return "success"

@app.route('/fog/speed/get_fog_accuracy', methods=['GET'])
def get_fog_data_to_queue4():
    return DataHolder.getInstance().get_fog_accuracy_Data()


if __name__ == '__main__':
    app.run(port=3103, host='0.0.0.0')
