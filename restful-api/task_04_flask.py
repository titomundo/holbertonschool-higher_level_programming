#!/usr/bin/python3

"""task_04_flask:
Creating a simple webserver using the flask framework
"""

from flask import Flask
from flask import jsonify
from flask import request
from json import loads

app = Flask(__name__)
users = dict()


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<string:username>")
def get_user(username):
    data = users.get(username)

    if data is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])


@app.post("/add_user")
def add_user():
    data = request.json
    response_data = dict()
    status = 201

    try:
        loads(request.data)
    except ValueError as err:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if username is None:
        response_data["error"] = "Username is required"
        status = 400
    elif users.get(username) is not None:
        response_data["error"] = "Username already exists"
        status = 409
    else:
        users[username] = data
        response_data["message"] = "User added"
        response_data["user"] = data

    return jsonify(response_data), status


if __name__ == "__main__":
    app.run()
