from threading import Timer
from time import sleep

import numpy as np

from flask import Flask
from flask_caching import Cache

from json import JSONEncoder


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


x = 0


def hello(name):
    global x
    print("Hello %s!" % name)
    x = "hell"
    return 5


rt = RepeatedTimer(2, hello, "World")  # it auto-starts, no need of rt.start()


@app.route('/test', methods=['GET'])
# @cache.cached(timeout=300)
def predict_data():
    global x
    return str(x)


# try:
#     print("go")
#     # your long-running job goes here...
#     sleep(60)
# except:
#     print("error")
#     # rt.stop()  # better in a try/finally block to make sure the program ends!

if __name__ == '__main__':
    # print("starting...")
    app.run(port=4000, debug=True)
