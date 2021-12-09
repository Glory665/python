import random as rnd
from memory_profiler import profile

# функция для генерации исходного списка

min_item = 0
max_item = 10000

@profile
def gen_list(size, min_item, max_item):
    a = [rnd.randint(min_item, max_item) for item in range(size)]
    return a


if __name__ == '__main__':
    gen_list(100, min_item, max_item)
"""
    Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     9     19.0 MiB     19.0 MiB           1   @profile
    10                                         def gen_list(size, min_item, max_item):
    11     19.0 MiB      0.0 MiB         103       a = [rnd.randint(min_item, max_item) for item in range(size)]
    12     19.0 MiB      0.0 MiB           1       return a

Вывод: Для генерации исходного списка из ДЗ №3 нам потребуется 19.0 Мбайт оперативной памяти
"""

# два алгоритма нахождения i-го по счёту простого числа.

@profile
def simple(n):
    lst = []
    for i in range(2, n+1):
        for j in range (2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst

@profile
def eratosthenes(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve1 = [x for x in sieve if x != 0]
    return sieve1




if __name__ == '__main__':
    simple(1000)
    eratosthenes(1000)

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    30     19.1 MiB     19.1 MiB           1   @profile
    31                                         def simple(n):
    32     19.1 MiB      0.0 MiB           1       lst = []
    33     19.1 MiB      0.0 MiB        1000       for i in range(2, n+1):
    34     19.1 MiB      0.0 MiB       78190           for j in range (2, i):
    35     19.1 MiB      0.0 MiB       78022               if i % j == 0:
    36     19.1 MiB      0.0 MiB         831                   break
    37                                                 else:
    38     19.1 MiB      0.0 MiB         168               lst.append(i)
    39     19.1 MiB      0.0 MiB           1       return lst

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    41     19.1 MiB     19.1 MiB           1   @profile
    42                                         def eratosthenes(n):
    43     19.1 MiB      0.0 MiB           1       sieve = list(range(n + 1))
    44     19.1 MiB      0.0 MiB           1       sieve[1] = 0
    45     19.1 MiB      0.0 MiB        1002       for i in sieve:
    46     19.1 MiB      0.0 MiB        1001           if i > 1:
    47     19.1 MiB      0.0 MiB        2126               for j in range(i + i, len(sieve), i):
    48     19.1 MiB      0.0 MiB        1958                   sieve[j] = 0
    49     19.1 MiB      0.0 MiB        1004       sieve1 = [x for x in sieve if x != 0]
    50     19.1 MiB      0.0 MiB           1       return sieve1

Вывод: Для нахождения i-го по счёту простого числа двумя методами (простым и применяя решето Эрастасфена) нам потребуется 
19.1 Мбайт оперативной памяти для каждого метода. Одинаковый результат и такие маленькие показатели заставляют поставить под сомнение
данный модуль оценки использования оперативной памяти. 
Плюс смущает графа Occurrences!
"""
# Делаем аналогично вышеописанному, используя getsizeof для оценки использования оперативной памяти

from sys import getsizeof

def simple(n):
    lst = []
    for i in range(2, n+1):
        for j in range (2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


def eratosthenes(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve1 = [x for x in sieve if x != 0]
    return sieve1

print(getsizeof(simple(1000)))
print(getsizeof(eratosthenes(1000)))

"""
1432
1432

Вывод: getsizeof учитывает не все, поэтому получаются маленькие значения. 
Лучше использователь специальный модуль для подсчета оперативной памяти

Python 3.9.6
Windows 10 x64
"""

print(getsizeof('first'))