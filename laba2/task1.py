import math

x = int(input("Введите x (|x|<=1) = "))
n = int(input("Введите n = "))

result = 0

for i in range(n):
    result += math.pow(-1, i) * math.pow(x, 2 * i + 1) / 2 * i + 1

print("result = " + str(result))
