# 1'. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



print ('Введите количество элементов списка')
n = int(input())
from random import randint 
spisok = [randint(1,10) for x in range(n)]
print('Начальный список: ', spisok)

x = [spisok[i] for i in range(1, len(spisok), 2)]
#print(f"Элементы стоящие на нечётных позициях: {x}")
print(f"Сумма элементов списка, стоящих на нечётной позиции {sum(x)}")