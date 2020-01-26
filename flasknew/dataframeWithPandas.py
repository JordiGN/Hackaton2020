# from flask import Flask, request, render_template, session, redirect
# import numpy as np
# import pandas as pd

# mainTable = pd.read_csv("raw_data.csv")

# #print(mainTable)
# app = Flask('location/<state>')
# def html_table():
#     return render_template('loginform.html', tables = [mainTable.to_html(classes = 'data')], titles = mainTable.columns.values)

# def sortedFrame(frame, state):
#     sortedDataframe = frame[frame['state'] == state]
#     sortedDataframe['date'] = pd.to_datetime(sortedDataframe['date'], errors='coerce')
#     sortedDataframe = sortedDataframe.sort_values('date', ascending = True)
#     return sortedDataframe


# if __name__ == '__main__':
#     app.run(host='0.0.0.0')
# #print(sortedFrame(mainTable, "MN"))