# 2. Напишите программу, которая найдёт произведение 
# пар чисел списка. Парой считаем первый и последний 
# элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


from random import randint


razmer = int(input('Введите размер массива '))
list = []
list2 = []

for i in range(razmer):
    list.append(randint(1, 5))

for i in range(len(list)):
    while i < len(list)/2 and razmer > len(list)/2:
        razmer = razmer - 1
        a = list[i] * list[razmer]
        list2.append(a)
        i += 1

print(list)
print(list2)