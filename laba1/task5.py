from laba1.NumberHepler import NumberHelper

number = int(input("number = "))
numbers = NumberHelper.GetOneByOne(number)
composition = 1
sum = 0
for numb in numbers:
    sum += numb
    composition *= numb

print("sum = " + str(sum))
print("composition = " + str(composition))
