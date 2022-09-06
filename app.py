from flask import Flask, jsonify, request
from parse import main

app = Flask(__name__)

client = app.test_client()

@app.route('/', methods=['POST'])
def add():
	new = request.get_json()
	data = main(new)
	return jsonify(data)


if __name__ == '__main__':
	app.run()
