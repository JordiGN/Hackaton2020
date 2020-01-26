# import pandas as pd
# import numpy as np
# import datetime as dt
# import os 


# mainTable = pd.read_csv("raw_data.csv")

# #print(mainTable)

# def sortedFrame(frame, state):
#     sortedDataframe = frame[frame['state'] == state]
#     sortedDataframe['date'] = pd.to_datetime(sortedDataframe['date'], errors='coerce')
#     sortedDataframe = sortedDataframe.sort_values('date', ascending = True)
#     return sortedDataframe


# print(sortedFrame(mainTable, "MN"))

