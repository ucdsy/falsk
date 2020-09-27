from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)
json_data = []
url = 'http://132.249.238.41/limesurvey/index.php/admin/remotecontrol'
username = "admin"
password = "ecrr"



import get_survey # this will be your file name; minus the `.py`

app = Flask(__name__)

@app.route('/')
def retrieve_csv(methods=['GET']):
    return get_survey.python_get_response(url, username, password)


# @app.route('/', methods=['GET'])
# def hello_world():
#     return jsonify({'message' : 'Hello, World!'})

@app.route('/survey', methods=['GET'])
def returnAll():
    return jsonify({'survey' : json_data})

@app.route('/survey/<string:name>', methods=['GET'])
def returnOne(name):
    theOne = json_data[0]
    for i,q in enumerate(json_data):
        if q['name'] == name:
            theOne = json_data[i]
    return jsonify({'survey' : theOne})

@app.route('/survey', methods=['POST'])

def addOne():
    new_json_data = request.get_json()
    json_data.append(new_json_data)
    data = pd.DataFrame(json_data)
    resp = data.to_csv('hello.csv')


    return jsonify({'survey' : json_data})

@app.route('/survey/<string:name>', methods=['PUT'])
def editOne(name):
    new_json_data = request.get_json()
    for i,q in enumerate(json_data):
        if q['name'] == name:
            json_data[i] = new_json_data
    qs = request.get_json()
    return jsonify({'survey' : json_data})

@app.route('/survey/<string:name>', methods=['DELETE'])
def deleteOne(name):
    for i,q in enumerate(json_data):
        if q['name'] == name:
            del json_data[i]
    return jsonify({'survey' : json_data})




if __name__ == "__main__":
    app.run()