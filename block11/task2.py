# Создание пустого списка для хранения элементов
array = []

# Ввод 10 элементов с клавиатуры
for i in range(10):
    value = int(input(f"Введите {i + 1}-й элемент массива: "))
    array.append(value)

# Печать массива
print("Массив заполнен следующими элементами:")
print(array)
