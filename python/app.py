import pandas as pd 
import numpy as np
import flask

mainTable = pd.read_csv("raw_data.csv")

#print(mainTable)

def sortedFrame(frame, state):
    sortedDataframe = frame[frame['state'] == state]
    sortedDataframe['date'] = pd.to_datetime(sortedDataframe['date'], errors='coerce')
    sortedDataframe = sortedDataframe.sort_values('date', ascending = True)
    return sortedDataframe

app = flask.Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route("/createuser", method=["POST"])
def create_user():
    return CreateUserService().create(request.get_json())
@app.route('/locations/<state>')

def getPostsByState(state):
    return sortedFrame(mainTable, state).to_json(orient = 'table')


if __name__ == "__main__":
	Schema();
    app.run(debug = True)