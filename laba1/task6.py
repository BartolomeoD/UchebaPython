from laba1.NumberHepler import NumberHelper

number = int(input("number = "))
numbers = NumberHelper.GetOneByOne(number)

result = "";
for numb in numbers:
    result += str(numb)
print("number = " + result)
