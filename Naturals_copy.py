from Dtypes import NNumber, Integer, RNumber, Polynomial
from Integers import *
from Naturals import *
from Rationals import *
from Naturals_test import Ntest


def DIV_NN_Dk(num1: NNumber, num2: NNumber):
    # Этот алгоритм полностью повторяет деление в столбик, если с комментариями будет
    # что-то непонятно, распишите деление 2-х рандомных чисел и смотря на вашу запись и алгоритм, все поймете

    # Заносим значения чисел в числовой массив
    curr_num = 0
    count = 0
    template_value = []
    lower_num = num1.get_num()
    bigger_num = num2.get_num()

    lower_num.reverse()
    bigger_num.reverse()

    # Проверяем, действительно ли в переменной, обозначающей большее число
    # находится большее исло, при необзодимости меняем местами

    if COM_NN_D(num1, num2) == 2:
        lower_num, bigger_num = bigger_num, lower_num

    # Проверка делителя на 0
    if not int(NNumber(lower_num).__str__()):
        raise ZeroDivisionError

    # Берем из большего числа столько цифр, сколько их в меньшем и заносим
    # в массив с временным значением

    for i in range(len(lower_num)):
        template_value.append(bigger_num[i])
        curr_num = i

    # Если так получилось, что число, получившееся на предыдущем шаге меньше
    # числа, на которое делим, берем ещё одну цифру

    if COM_NN_D(NNumber(lower_num), NNumber(template_value)) == 2:
        template_value.append(bigger_num[curr_num + 1])

    # k - переменная, обозначающая степень десятки и она разности длин
    # начального большего числа и получившегося из последних шагов

    k = len(bigger_num) - len(template_value)

    # Пока получившееся число больше меньшего числа, отнимаем от него меньшее
    # при этом на каждом шаге прибаляем к переменной count 1, эта переменная показывает
    # на сколько мы "умножили" меьншее число

    while COM_NN_D(NNumber(template_value), NNumber(lower_num)) != 1:
        sub = SUB_NN_N(NNumber(template_value), NNumber(lower_num))
        template_value = sub.get_num()
        template_value.reverse()
        count += 1

    count = count * pow(10, k)

    return count


Ntest(['INT_Q_B'])
