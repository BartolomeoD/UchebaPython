inputString = input("inputString = ")
elements = inputString.split(",")
sum = 0
for element in elements:
    sum += int(element)
print("4 " + elements[4])
elements.reverse()
print("reverse = " + ",".join(elements))
print("sum " + str(sum))
print("average " + str(sum / len(elements)))
