import requests
import pandas as pd
import pprint

# Use the python requests library to fetch the data
res = requests.get("https://json.link/XUtG4ceic4.json")

# format the response as a python object from json object
events = res.json()

# view the json data format
pprint.pprint(events)

# Create a dictionary for the column names
column_dict = {k:[] for k in events[0].keys()}

# for each separate dictionary (inner json object/individual event), 
# add items to our column dictionary
[{column_dict[k].append(v) for k,v in event.items()} for event in events]

# convert to a row/column based object, similar to an excel or CSV
event_dataframe = pd.DataFrame(column_dict)

print(event_dataframe.head())

print(event_dataframe.drop_duplicates())

event_dataframe.to_csv("coffee_iot.csv")
