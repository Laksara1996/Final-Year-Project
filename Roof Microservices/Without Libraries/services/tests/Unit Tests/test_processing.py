import unittest
from services.processing_microservice import app

import numpy as np
import json
from json import JSONEncoder


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


class ProcessingTests(unittest.TestCase):

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

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_speed_data_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/roof/speed_data')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_driver_rush_data_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/roof/driver_rush_data')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_visibility_data_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/roof/visibility_data')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_rain_intensity_data_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/roof/rain_intensity_data')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_pitch_data_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/roof/pitch_data')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_ac_data_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/roof/ac_data')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_passenger_data_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/roof/passenger_data')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_window_data_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/roof/window_data')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_speed_input_list_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/speed/input')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_speed_x_train_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/speed/x_train')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_speed_x_test_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/speed/x_test')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_speed_y_test_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/speed/y_test')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_speed_y_train_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/speed/y_train')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_ac_control_input_list_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/ac_control/input')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_ac_control_x_train_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/ac_control/x_train')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_ac_control_x_test_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/ac_control/x_test')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_ac_control_y_test_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/ac_control/y_test')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_ac_control_y_train_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/ac_control/y_train')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_home_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')

        # print(result.data.decode())

        # assert the response data
        self.assertEqual(result.data.decode(), "Hello World!!!")

    # def test_speed_data(self):
    #     # sends HTTP GET request to the application
    #     # on the specified path
    #     result = self.app.get('/roof/speed_data')
    #     decodedArrays = json.loads(result.data.decode())
    #     finalNumpyArray = np.asarray(decodedArrays["array"])
    #
    #     print(finalNumpyArray)
    #
    #     # assert the response data
    #     self.assertEqual(result.data.decode(), "Hello World!!!")


if __name__ == '__main__':
    unittest.main()
