# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random as rnd
import timeit as tnt
import sys
import statistics

N = 100
list = []
for i in range(N):
    list.append(rnd.randint(-100, 100))
print(f'Первичный список:\n{list}')

def spisok_sort(list):
    for i in range(N-1):
        for j in range(N-i-1):
            if list[j] < list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list
print(f'Отсортированный список:\n{spisok_sort(list)}')

print(tnt.timeit('spisok_sort(list)', number=1000, globals=globals())) # 0.6859153
print(sys.getsizeof(spisok_sort(list))) # 920
# Оптимизированный алгоритм
def spisok_sort(list):
    sort_cnt = 1
    while sort_cnt < len(list):
        for i in range(len(list) - sort_cnt):
            if list[i] < list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                is_sort = False
        sort_cnt += 1
        return list
        if is_sort:
            break

print(f'Отсортированный список:\n{spisok_sort(list)}')

print(tnt.timeit('spisok_sort(list)', number=1000, globals=globals())) # 0.01078889999999999
print(sys.getsizeof(spisok_sort(list))) # 920

#############################################

# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

N = 10
list1 = []
for i in range(N):
    list1.append(rnd.randint(0, 50))
print(f'Первичный список:\n{list1}')

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):

    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)

print(f'Отсортированный список:\n{merge_sort(list1)} - Сортировка методом слияния')

#############################################

# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки,
# который не рассматривался на уроках

M = 4
list_3 = []
for i in range(2 * M + 1):
    list_3.append(rnd.randint(0, 50))
print(f'Первичный список:\n{list_3}')

mid = statistics.median(list_3)
print(f'Медиана массива: {mid}')

left_list = []
right_list = []
for i, item in enumerate(list_3):
    if item <= mid:
        left_list.append(item)
    else:
        right_list.append(item)
print(f'Значения меньше медианы:\n{left_list}')
print(f'Значения больше медианы:\n{right_list}')


def sort_gnome(base_array):
    array = base_array.copy()
    i = 1
    j = 2
    while i < len(array):
        if array[i - 1] < array[i]:
            i = j
            j += 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            i -= 1
            if i == 0:
                i = j
                j += 1
    return array


sort_numbers = sort_gnome(list_3)
print(f'Отсортированный список:\n{sort_numbers}')
print('Sort test OK' if sorted(list_3) == sort_numbers else 'Sort test failed')
median_ = sort_numbers[len(sort_numbers) // 2]
print(f'Медиана массива: {median_}')


"""
Вариант без использования сортировки.
Суть алгоритма заключается в переборе элементов массива и 
подсчете для каждого элемента кол-ва элементов меньше его.
"""


def search_median(array):
    assert len(array) % 2 != 0, 'длина массива должна быть нечетной'
    for i in range(len(array)):
        counter = 0
        for j in range(len(array)):
            if i != j and array[j] < array[i]:
                counter += 1
        if counter == len(array) // 2:
            return array[i]


med = search_median(list_3)
print(f'Медиана массива: {med}')
