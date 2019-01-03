import random
import math

data = []
for i in range(10):
    data.append(random.randint(-10, 10))
print(data)
indexMin = 0
indexMax = 0
minValue = -1000
maxValue = 1000

for i in range(len(data)):
    if data[i] > 0 and data[i] < maxValue:
        indexMax = i
        maxValue = data[i]
    if data[i] < 0 and data[i] > minValue:
        indexMin = i
        minValue = data[i]

print("index Min " + str(indexMin))
print("index Max " + str(indexMax))
highIndex = max(indexMax, indexMin)
lowIndex = min(indexMax, indexMin)

print("highIndex " + str(highIndex))
print("lowIndex " + str(lowIndex))
lowIndex += 1
print("delete data = " + str(data[lowIndex: highIndex]))
result = list(set(data) - set(data[lowIndex: highIndex]))
print(result)
