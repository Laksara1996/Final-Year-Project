import requests
from flask import Flask, jsonify, make_response
import json
import os

app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

with open('{}/database/todo.json'.format(database_path), "r") as jsf:
    todo_list = json.load(jsf)


@app.route('/', methods=['GET'])
def hello():
    ''' Greet the user '''

    return "Todo service is up"


@app.route('/lists', methods=['GET'])
def show_lists():
    ''' Displays all the lists '''

    tlists = []
    for username in todo_list:
        for lname in todo_list[username]:
            tlists.append(lname)
    return jsonify(lists=tlists)


@app.route('/lists/<username>', methods=['GET'])
def user_list(username):
    ''' Returns a user oriented list '''

    if username not in todo_list:
        return "No list found"

    return jsonify(todo_list[username])


@app.route('/lists/air_condition', methods=['GET'])
def air_condition_lists():
    """ Get lists based on air_condition """

    number_array = get_air_condition_data()
    return str(number_array[0])


@app.route('/lists/passenger_count', methods=['GET'])
def passenger_count_lists():
    """ Get lists based on passenger_count """

    number_array = get_passenger_count_data()
    return str(number_array[0])


@app.route('/lists/window_opening', methods=['GET'])
def window_opening_lists():
    """ Get lists based on window_opening """

    number_array = get_window_opening_data()
    return str(number_array[0])


def get_air_condition_data():
    try:
        req = requests.get("http://localhost:5000//data/air_condition_status")
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
        req = requests.get("http://localhost:5000//data/passenger_count")
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
        req = requests.get("http://localhost:5000//data/window_opening")
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


if __name__ == '__main__':
    app.run(port=3001, debug=True)
