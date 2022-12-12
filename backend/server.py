# create a flask server to add two numbers
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/add", methods=["POST"])
def add():
    data = request.form
    result = int(data["num1"]) * int(data["num2"])
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, port=3002)
