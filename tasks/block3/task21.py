n = int(input("Введите натуральное число n (> 9): "))


if n <= 9:
    print("Число должно быть больше 9.")
else:

    units = n % 10

    tens = (n // 10) % 10

    print(f"Единицы: {units}")
    print(f"Десятки: {tens}")
