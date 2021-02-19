# Load libraries
import os
from threading import Timer
import numpy as np
from dask.tests.test_system import psutil
from flask import Flask
from json import JSONEncoder


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


app = Flask(__name__)

cpu_usage_data = 0
memory_usage_data = 0
raspberry_temperature_data = 0
performance_data = 0


def measure_temp():
    global raspberry_temperature_data
    raspberry_temperature_data = os.popen("vcgencmd measure_temp").readline()
    return raspberry_temperature_data.replace("temp=", "")


@app.route('/roof/performance', methods=['GET'])
def performance():
    global performance_data
    if cpu_usage_data <= 40.0 or memory_usage_data <= 70:
        performance_data = 0
    else:
        performance_data = 1
    print("performance", performance_data)
    return str(performance_data)


def get_memory_usage():
    global memory_usage_data
    memory_usage_data = psutil.virtual_memory().percent
    print('Memory usage:', memory_usage_data)
    return memory_usage_data


def get_cpu_measure_data():
    global cpu_usage_data
    cpu_usage_data = psutil.cpu_percent()
    print("cpu", cpu_usage_data)
    return cpu_usage_data


def automated_data_request():
    get_cpu_measure_data()
    performance()


data_request_automated = RepeatedTimer(1, automated_data_request)

if __name__ == '__main__':
    app.run(port=3006, debug=True, host='0.0.0.0')
