import csv
# data to be saved
data = [
    ['Jay', 'Dominic', 25],
    ['Justin', 'Seam', 30],
    ['Bob', 'Lans', 40],
    ]
# open a file for writing
with open('data.csv', mode='w', newline='') as file:
# create a csv writer object
    writer = csv.writer(file)
# write the data to the file
writer.writerows(data)