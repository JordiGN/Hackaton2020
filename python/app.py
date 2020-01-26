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

@app.route('/locations/<state>')

def getPostsByState(state):
    return sortedFrame(mainTable, state).to_json(orient = 'table')


if __name__ == "__main__":
    app.run(debug = True)