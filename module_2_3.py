my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]  # исходный список
count = 0  # задаем счетчик
print("Список", my_list, '\nПоложительные числы из списка')
while count < len(my_list):
    number = my_list[count]  # задаем число из списка
    count = count + 1  # запускаем счетчик
    if number == 0:
        continue  # пропускаем 0
    elif number < 0:
        print("Встретилось отрицательное число:", number)
        break
    elif count == len(my_list):
        print(number)
        print("Список закончился")
    else:
        print(number)


