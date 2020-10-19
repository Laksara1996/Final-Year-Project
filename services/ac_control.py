# Load libraries
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier

import requests
from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/lists/air_condition', methods=['GET'])
def air_condition_lists():
    """ Get lists based on air_condition """

    number_array = get_air_condition_data()
    return jsonify(number_array)


@app.route('/lists/passenger_count', methods=['GET'])
def passenger_count_lists():
    """ Get lists based on passenger_count """

    number_array = get_passenger_count_data()
    return jsonify(number_array)


@app.route('/lists/window_opening', methods=['GET'])
def window_opening_lists():
    """ Get lists based on window_opening """

    number_array = get_window_opening_data()
    return jsonify(number_array)


@app.route('/lists/ac_status_output', methods=['GET'])
def ac_status_output():
    """ Get lists based on window_opening """

    number_array = neural_network_function()
    return jsonify(number_array)


def get_air_condition_data():
    try:
        req = requests.get("http://localhost:5000//data/airConditionStatus")
        req_text = req.text[1:-1]
        number = ""
        number_array = []
        for i in req_text:
            if i == ',':
                number_array.append(number)
                number = ""
                continue
            number = number + i
        number_array = [float(i) for i in number_array]
        # print(number_array)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


def get_passenger_count_data():
    try:
        req = requests.get("http://localhost:5000//data/passengerCount")
        req_text = req.text[1:-1]
        number = ""
        number_array = []
        for i in req_text:
            if i == ',':
                number_array.append(number)
                number = ""
                continue
            number = number + i
        number_array = [float(i) for i in number_array]
        # print(number_array)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


def get_window_opening_data():
    try:
        req = requests.get("http://localhost:5000//data/windowOpening")
        req_text = req.text[1:-1]
        number = ""
        number_array = []
        for i in req_text:
            if i == ',':
                number_array.append(number)
                number = ""
                continue
            number = number + i
        number_array = [float(i) for i in number_array]
        # print(number_array)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return number_array


def neural_network_function():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    # fix random seed for reproducibility
    seed = 7
    np.random.seed(seed)

    window_opening_data = [int(i) for i in get_window_opening_data()]
    passenger_count_data = [int(i) for i in get_passenger_count_data()]

    air_condition_data = [int(i) for i in get_air_condition_data()]

    X = np.array((passenger_count_data, window_opening_data)).T
    Y = air_condition_data

    print("X")
    print(X)
    print("y")
    print(Y)

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

    # split train and test
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=0)

    estimator.fit(X_train, Y_train)

    print(estimator.predict(X_test))
    print('Accuracy: ', accuracy_score(Y_test, estimator.predict(X_test)))

    df = pd.DataFrame(estimator.predict(X), columns=['output'])
    print("output")
    print(df['output'].values.tolist())

    return df['output'].values.tolist()


if __name__ == '__main__':
    app.run(port=3001, debug=True)
