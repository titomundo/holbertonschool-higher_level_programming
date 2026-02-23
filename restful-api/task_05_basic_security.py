#!/usr/bin/python3

"""task_05_basic_security
Creating a simple python server with basic and JWT authentication
"""

from flask import Flask
from flask import request
from flask import jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import get_jwt
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "Holberton School"
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(
        users.get(username)["password"], password
    ):
        return username


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.post("/login")
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username is None or password is None:
        return jsonify({"error": "Missing Credentials"}), 401

    current = users.get(username)

    if not current or not check_password_hash(current["password"], password):
        return jsonify({"error": "Invalid Credentials"}), 401

    data = {"role": current["role"]}
    access_token = create_access_token(username, additional_claims=data)
    return jsonify(access_token=access_token)


@app.route("/jwt-protected")
@jwt_required()
def protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_protected():
    current_user = get_jwt()
    role = current_user.get("role")

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
