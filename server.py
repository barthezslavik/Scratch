from flask import Flask, request
import numpy as np
import flask

app = Flask(__name__)

# request model prediction
@app.route('/', methods=['GET', 'POST'])
def predict():
    result = 1
    data = {'result': result}
    return flask.jsonify(data)

# start Flask server
app.run(host='0.0.0.0', port=5000, debug=False)