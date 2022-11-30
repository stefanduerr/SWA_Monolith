import csv
import pandas
colnames = ['Caller', 'Callee', 'NumberOfCallsLastYear']
data = pandas.read_csv('CallerCallee.csv', sep=";", header=0)

vals = pandas.DataFrame(data)
vals = vals.drop('NumberOfCallsLastYear', axis=1)
data = vals.values.tolist()

print(data)

with open('ServiceList_.csv', newline='') as f:
    reader = csv.reader(f)
    services = list(reader)



# with open('CallerCallee.csv', newline='') as f:
#     reader = csv.reader(f)
#     data = list(reader)

# print(data)