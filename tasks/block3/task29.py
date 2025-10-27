n = int(input("Введите число "))
cot = n // 100
posl = n % 10
cered = n % 100 // 10
print(cered * 100 + cot * 10 + posl)
