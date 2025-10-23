num = int(input("Введите трехзначное число: "))

if 100 <= num <= 999:
    num_str = str(num)
    last_digit = num_str[-1]
    remaining_digits = num_str[:-1]
    # Формируем новое число
    new_num_str = last_digit + remaining_digits
    new_num = int(new_num_str)
    print("Полученное число:", new_num)
else:
    print("Ошибка: введено число не является трехзначным.")
