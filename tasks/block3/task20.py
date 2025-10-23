number = 1234
reversed_number = int(str(number)[::-1])
print(reversed_number)

number = 5434
num_str = str(number)

# Переставляем цифры: вторая, первая,  четвертая, третья.
result = int(num_str[1] + num_str[0] + num_str[3] + num_str[2])
print(result)
