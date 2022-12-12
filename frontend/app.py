# flake8: noqa

import requests
from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__, template_folder="templates")


backend_url = "http://localhost:3002/"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add():
    num1 = int(request.form["num1"])
    num2 = int(request.form["num2"])

    response = requests.post(backend_url + "/add", data={"num1": num1, "num2": num2})
    result = response.json()

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
