number = int(input("Введите трехзначное число:"))

list = list(map(int, str(number)))

print(list[1], list[2], list[0]) 
print(list[1], list[0], list[2])
print(list[2], list[1], list[0])
print(list[1], list[1], list[1])
print(list[2], list[1], list[1])
print(list[2], list[2], list[1])