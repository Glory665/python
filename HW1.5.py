# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

QUARTER = 4
Firm = namedtuple('Firm', 'name, profit, total')
firm_count = int(input("Введите количество предприятий: "))
firm = list()
sum_ = 0

for i in range(1, firm_count + 1):
    name_ = input(f'Введите наименование предприятия №{i}: ')
    profit_ = list()
    for k in range(1, QUARTER + 1):
        profit_.append(float(input(f'Введите прибыль за {k}-й квартал: ')))
    total_ = sum(profit_)
    sum_ += total_
    firm.append(Firm(name_, profit_, total_))

# средняя прибыль всех предприятий за год

average = sum_ / firm_count
print(f'Средняя прибыль всех предприятий за год: {average}')

names_high = list()
names_low = list()
for x in range(firm_count):
    if firm[x].total > average:
        names_high.append(firm[x].name)
    elif firm[x].total < average:
        names_low.append(firm[x].name)

print('Предприятия с прибылью выше средней:')
print(*names_high)
print('*' * 40)
print('Предприятия с прибылью ниже средней:')
print(*names_low)

##################################################

# 2. Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from itertools import zip_longest

def sum_f(first, second):
    BASE = 16
    numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    number_dic = dict(zip(numbers, list(range(BASE))))
    first = first[::-1]
    second = second[::-1]
    third = []

    c = 0
    for first_, second_ in zip_longest(first, second, fillvalue = '0'):
        third.append(numbers[(number_dic[first_] + number_dic[second_] + c) % 16])
        c = (number_dic[first_] + number_dic[second_] + c) // 16
    else:
        third.append(numbers[c % 16])

    return third[::-1]

def multi_f(first, second):
    numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    multi = '0'

    first = first[::-1]
    second = second[::-1]

    for i in range(len(second)):
        third = []
        if i > 0:
            third = ['0'] * i
        c = 0
        for j in first:
            a = numbers.index(second[i])
            b = numbers.index(j)
            third.append(numbers[(a * b + c) % 16])
            c = (a * b + c) // 16

            if j == len(first):
                break
        third.append(str(c))

        n2 = third[::-1]
        multi = sum_f(multi, n2)

    return(multi)

n1 = 'A2'
n2 = 'C4F'

print(f'Сумма чисел равна: {sum_f(n1, n2)}')
print(f'Произведение чисел равно: {multi_f(n1, n2)}')

# с применением модуля collections

from collections import deque

DEC_NUMS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
            'C': 12, 'D': 13, 'E': 14, 'F': 15}
HEX_NUMS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

hex_first = list(input('Введите первое шестнадцатиричное число: ').upper())
hex_second = list(input('Введите второе шестнадцатиричное число: ').upper())
num_count = max(len(hex_first), len(hex_second))
num_first = deque(hex_first)
num_second = deque(hex_second)

if len(hex_first) > len(hex_second):
    for _ in range(num_count - len(hex_second)):
        num_second.appendleft('0')
elif len(hex_first) < len(hex_second):
    for _ in range(num_count - len(hex_first)):
        num_first.appendleft('0')

result_dec = deque()
transfer = 0
for _ in range(num_count):
    sum_ = DEC_NUMS[num_first.pop()] + DEC_NUMS[num_second.pop()] + transfer
    if sum_ > 15:
        transfer = 1
        sum_ -= 16
    else:
        transfer = 0
    result_dec.appendleft(sum_)
if transfer == 1:
    result_dec.appendleft(1)

result_hex = list()
for _ in range(len(result_dec)):
    result_hex.append(HEX_NUMS[result_dec.popleft()])

print(f'Сумма чисел равна: {"".join(result_hex)}')