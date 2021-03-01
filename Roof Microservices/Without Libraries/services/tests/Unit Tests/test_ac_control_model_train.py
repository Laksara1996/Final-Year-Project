import unittest
from services.ac_control_model_train_microservice import app

import numpy as np
import json
from json import JSONEncoder


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


class AcControlModelTrainTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_predict_data_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/ac_control/predict')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_wh_data_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/roof/wh')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_bh_data_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/roof/bh')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_wo_data_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/roof/wo')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_bo_data_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/roof/bo')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
