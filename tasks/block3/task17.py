number = int(input("Введите число: "))
a = number // 100
b = number // 10 % 10
c = number % 10

print(a * 100 + c * 10 + b)
