ves = int(input("Введите вес боксера: "))
if ves <= 60:
    print("боксер будет отправлен в категорию: легкий вес")
elif ves <= 64:
    print("боксер будет отправлен в категорию: первый полусредний вес")
elif ves <= 69:
    print("боксер будет отправлен в категорию: полусредний вес")
else:
    print("боксер не будет отправлне ни к одной из этих категорий")
