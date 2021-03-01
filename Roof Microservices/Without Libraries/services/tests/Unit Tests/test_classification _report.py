import unittest
from services.classification_report_microservice import app

import numpy as np
import json
from json import JSONEncoder


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


class ClassificationReportTests(unittest.TestCase):

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

    def test_ac_classification_report_output_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/ac_control/classification_report')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_speed_classification_report_output_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/speed/classification_report')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
