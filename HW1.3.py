# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

my_list = list(range(2, 100))

for item in range (2,10):
    print(len([i for i in my_list if i % item == 0]))

#####################################################

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

from random import randint

n= int(input('Введите длину массива: '))
a = [randint(1,42) for item in range(n)] # Создаем массив случайных чисел
print(a) # вывод сформированного массива для проверки

print([i for i, item in enumerate(a) if item % 2 == 0])

#####################################################

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

n= int(input('Введите длину массива: '))
a = [randint(1,100) for item in range(n)]
print(a)
a[a.index(max(a))], a[a.index(min(a))] = (a[a.index(min(a))], a[a.index(max(a))])
print(a)

#####################################################

# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint
from collections import Counter

n= int(input('Введите длину массива: '))
a = [randint(1,100) for item in range(n)]

print(a)
print(Counter(a).most_common(1))

#####################################################

# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

from random import randint

n= int(input('Введите длину массива: '))
a = [randint(-100,100) for item in range(n)]
print(a)


print(f'максимальный отрицательный элемент: {max([i for i in a if i < 0])}, '
      f'позиция в массиве: {a.index(max([i for i in a if i < 0]))}')

#####################################################

# 6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

n= int(input('Введите длину массива: '))
a = [randint(-10,10) for item in range(n)]
print(a)
a_min = a.index(min(a))
a_max = a.index(max(a))
print(a_min)
print(a_max)
dir = 1 if a_max > a_min else -1
print(sum(a[a_min:a_max:dir]) - a[a_min])

#####################################################

# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными),
# так и различаться.

from random import randint

n= int(input('Введите длину массива: '))
a = [randint(-10,10) for item in range(n)]
print(a)
a_sort = sorted(a)
print(a_sort[:2])

#####################################################

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и
# записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

from random import randint

N = 4
a = [[randint(0,10) for i in range(N)] for i in range(N)]
b = []
print(a)
for i, item in enumerate(a):
    b.append(sum(item))
c = a+[b]
print(c)
print('\n'.join(['\t'.join(map(str,item)) for item in c]))

#####################################################

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

N = 4
a = [[randint(0,10) for i in range(N)] for i in range(N)]

print('\n'.join(['\t'.join(map(str,item)) for item in a]))

for i in range(4):
    for j in range(4):
        print(max([min((a[i][j]) for i in range(4)) for j in range(4)]))
        exit(0)






