import csv
import pandas
colnames = ['Caller', 'Callee', 'NumberOfCallsLastYear']
data = pandas.read_csv('CallerCallee.csv', sep=";", header=0)

vals = pandas.DataFrame(data)
vals = vals.drop('NumberOfCallsLastYear', axis=1)
data = vals.values.tolist()

# print(data)

with open('ServiceList_.csv', newline='') as f:
    reader = csv.reader(f)
    services = list(reader)

# print(services)

d = {}

for i in range(1, 9):
    # key = f"group{i}"
    key = i
    d[key] = []

print(d)


list1 = [[1,2],[3,4],[5,6],[1,5],[3,2],[7,8]]



list2 = [[1],[2],[3],[4],[5],[6],[7],[8]]

for y in range(1,9):
    for x in list1:
        if x[0] == y or x[1] == y:
            # key = f"group{y}"
            key = y
            d[key] += x
# for a in d:
#     for b in d:
#         if a[0] in b:
#             print("True")
print(d)
dic = {}
x = 0

for a in range(1,8):
    if d[a][0] == d[a+1][0]:
        d[a] += d[a+1]
        key = f"group{a}"
        dic[key] = d[a]





print(d)
print(dic)
print(d[1][0])

for x in dic:
    for y in dic[x]:
        if y == 1:
            print(True)
            

print(dic)