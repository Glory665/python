import random as rnd
import timeit as tit
import cProfile

# функция для генерации исходного списка

min_item = 0
max_item = 10000

def gen_list(size, min_item, max_item):
    a = [rnd.randint(min_item, max_item) for item in range(size)]
    return a

# Вариант 1
# С применением встроенных функций min, max, index

def change_min_max(a):
    min_pos = a.index(min(a))
    max_pos = a.index(max(a))
    a[min_pos], a[max_pos] = a[max_pos], a[min_pos]
    return a


num_100 = gen_list(100, min_item, max_item)
num_1000 = gen_list(1000, min_item, max_item)
num_10000 = gen_list(10000, min_item, max_item)

print(tit.timeit('change_min_max(num_100)', number=1000, globals=globals())) # 0.0073155000000000026
print(tit.timeit('change_min_max(num_1000)', number=1000, globals=globals())) # 0.0619745
print(tit.timeit('change_min_max(num_10000)', number=1000, globals=globals())) # 0.7638068

cProfile.run('change_min_max(num_10000)')

"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 HW1.4.py:12(change_min_max)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""

# Вариант 2
# С применением цикла for

def change_min_max_1(a):
    min_pos = 0
    max_pos = 0
    min_ = a[0]
    max_ = a[0]

    for i in range(1, len(a)):
        if a[i] < min_:
            min_ = a[i]
            min_pos = i
        elif a[i] > max_:
            max_ = a[i]
            max_pos = i
    a[min_pos], a[max_pos] = a[max_pos], a[min_pos]
    return a

print(tit.timeit('change_min_max_1(num_100)', number=1000, globals=globals())) # 0.019947600000000065
print(tit.timeit('change_min_max_1(num_1000)', number=1000, globals=globals())) # 0.17098210000000003
print(tit.timeit('change_min_max_1(num_10000)', number=1000, globals=globals())) # 1.3465710000000002

cProfile.run('change_min_max_1(num_10000)')

"""
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 HW1.4.py:29(change_min_max_1)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
# Вариант 3
# С применением цикла while

def change_w(a):
    min_pos = 0
    max_pos = 0
    min_ = a[0]
    max_ = a[0]
    i = 0

    while i < len(a):
        if a[i] < min_:
            min_ = a[i]
            min_pos = i
        elif a[i] > max_:
            max_ = a[i]
            max_pos = i
        i += 1
    a[min_pos], a[max_pos] = a[max_pos], a[min_pos]
    return a

print(tit.timeit('change_w(num_100)', number=1000, globals=globals())) # 0.02327060000000003
print(tit.timeit('change_w(num_1000)', number=1000, globals=globals())) # 0.2354305000000001
print(tit.timeit('change_w(num_10000)', number=1000, globals=globals())) # 2.8429520999999998

cProfile.run('change_w(num_10000)')

"""
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.007    0.007 <string>:1(<module>)
        1    0.005    0.005    0.007    0.007 HW1.4.py:51(change_w)
        1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
    10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

"""
Вывод:
Во всех трёх вариантах прослеживается линейная зависимость.
Наибольшее быстродействие показал вариант с использованием встроенных функций min и max.
Наихудшие показатели у варианта с использованием цикла while. Также через cProfile в варианте
с циклом while было видно что функция len была вызвана 10001 раз.

"""

################################################

# 2. Написать два алгоритма нахождения i-го по счёту простого числа.

import timeit as tit
import cProfile

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

print(simple(1000))
print(eratosthenes(1000))

print(tit.timeit('simple(1000)', number=1000, globals=globals())) # 6.5812064
print(tit.timeit('eratosthenes(1000)', number=1000, globals=globals())) # 0.32352500000000006

cProfile.run('simple(1000)')

"""
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        1    0.006    0.006    0.006    0.006 HW1.6.py:4(simple)
        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
      168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

cProfile.run('eratosthenes(1000)')

"""
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 HW1.6.py:15(eratosthenes)
        1    0.000    0.000    0.000    0.000 HW1.6.py:22(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      168    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
