
num = int(input("Введите трехзначное число: "))

if 100 <= abs(num) <= 999:
    
    num_str = str(num)
 
    reversed_str = num_str[::-1]
 
    reversed_num = int(reversed_str)
    print("Число, прочитанное справа налево:", reversed_num)
else:
    print("Ошибка: введено число не является трехзначным.")