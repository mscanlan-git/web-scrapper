import json
# data to be saved
data = [
    {'name': 'John', 'surname': 'Doe', 'age': 25},
    {'name': 'Jane', 'surname': 'Smith', 'age': 30},
    {'name': 'Bob', 'surname': 'Johnson', 'age': 40},
]
# open a file for writing
with open('data.json', mode='w') as file:
# write the data to the file
    json.dump(data,file)