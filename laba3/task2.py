import random

data = []
for i in range(10):
    data.append(random.randint(-10, 10))
print(data)
first = True
newData = data.copy()

for element in data:
    if first and element > 0:
        first = False
        continue

    if element > 0:
        temp = element
        newData.remove(element)
        newData.insert(0, element)


print(newData)
