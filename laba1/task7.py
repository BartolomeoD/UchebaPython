from laba1.NumberHepler import NumberHelper

number = int(input("number = "))
numbers = NumberHelper.GetOneByOne(number)
last = numbers[len(numbers) - 1]
del numbers[len(numbers) - 1]
numbers.insert(0, last)
result = ""
for numb in reversed(numbers):
    result += str(numb)

print("result = " + result)
