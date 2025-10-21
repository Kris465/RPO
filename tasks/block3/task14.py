# Вводим трехзначное число
num = int(input("Введите трехзначное число: "))

# Проверка, что число действительно трехзначное
if 100 <= num <= 999:
    num_str = str(num)
    first_digit = num_str[0]
    remaining_digits = num_str[1:]
    # Формируем новое число
    new_num_str = remaining_digits + first_digit
    new_num = int(new_num_str)
    print("Полученное число:", new_num)
else:
    print("Ошибка: введено число не является трехзначным.")
