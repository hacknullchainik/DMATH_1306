from NIKITAT import *
from chernov import *
from ALEX import *


def MUL_Nk_N(num: NNumber, k):
    # Просто добавляем нули в конце числа
    number1 = num.get_num()
    number1.reverse()
    for i in range(k):
        number1.append(0)
    return NNumber(number1)


def POZ_Z_D(num: Integer):
    # Проверяем сначала первый символ массива,
    # ведь если наше число было нулем, в первом элементе тоже будет ноль
    if num.get_num()[0] == 0:
        return 0

    elif num.get_sign():
        return 1

    else:
        return 2


def TRANS_Q_Z(num: RNumber):
    # Создаём массив, в который будет записан результат и записываем числитель в
    # служебную переменную
    numer_list = []
    numer = num.get_num()

    # Проверяем, равен ли знаменатель единице и продолжаем работу в случае равенства

    if num.get_den() == 1:
        # Проверяем знак знаменателя, т.к. знак дроби хранится в нем
        if numer > 0:
            sign = False
        else:
            sign = True

        # Передаем в массив по одной цифре числа и переворачиваем его в конце, т.к
        # в массив цифры заноcились с конца

        numer = abs(numer)

        while numer > 0:
            numer_list.append(numer % 10)
            numer //= 10

        numer_list.reverse()

        return Integer(numer_list, sign)

    # В случае, если знаменатель
    # не равен нулю, функция возвращает изначальную дробь

    else:
        return num


def ADD_NN_N(number1: NNumber, number2: NNumber):
    # Создаем дубликаты наших цифровых массивов (по факту - чисел) для более удобной работы
    bigger_num = number1.get_num()
    lower_num = number2.get_num()
    result = []
    i = 0

    # Если числа были введены не так, что сначала большее, меняем их местами, дабы избежать возможных ошибок

    if COM_NN_D(number1, number2) == 1:
        bigger_num, lower_num = lower_num, bigger_num

    # Сначала просто складываем поразрядно все числа, на сколько хватит разрядов в меньшем числе
    # и заносим в результирующий массив
    for i in range(len(lower_num)):
        result.append(bigger_num[i] + lower_num[i])

    # Добавляем числа, которые в большем числе были в больших разрядах, чем в меньшем
    for j in range(i + 1, len(bigger_num)):
        result.append(bigger_num[j])

    # Переносим в следующие разряды десятки, которые могли получиться в результате сложения
    # При необходимости,, добавляем еще один разряд в конце
    for i in range(len(result)):
        if result[i] > 9:
            result[i] -= 10
            if i == len(result) - 1:
                result.append(1)
            else:
                result[i + 1] += 1
    # Переворачиваем массив, так как работали с обратным порядком цифр
    result.reverse()

    return NNumber(result)


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

    while COM_NN_D(NNumber(template_value), NNumber(lower_num)) == 2:
        sub = SUB_NN_N(NNumber(template_value), NNumber(lower_num))
        template_value = sub.get_num()
        template_value.reverse()
        count += 1

    count = count * pow(10, k)

    return count


def MUL_ZZ_Z(num1: Integer, num2: Integer):
    # Запоминаем знаки чисел в соответствующие переменные
    sign1 = num1.get_sign()
    sign2 = num2.get_sign()

    # Берем модуль от каждого из чисел
    lower_num = ABS_Z_N(num1)
    bigger_num = ABS_Z_N(num2)

    # Так как теперь мы имеем 2 натуральных числа можно просто перемножить их
    # соответствующей функцией
    result = MUL_NN_N(lower_num, bigger_num)

    # Знак числа, получаемого при умножении легко вычисляется XOR'ом
    res_sign = sign1 ^ sign2
    result_digits = result.get_num()
    result_digits.reverse()

    result = Integer(result_digits, res_sign)
    return result


def MUL_NN_N(num1: NNumber, num2: NNumber):
    # Записываем числа в числовые массивы
    lower_num = num1.get_num()
    bigger_num = num2.get_num()

    lower_num.reverse()
    bigger_num.reverse()

    # Проверяем, действительно ли в переменной, обозначающей большее число
    # находится большее исло, при необзодимости меняем местами
    if COM_NN_D(num1, num2) == 2:
        lower_num, bigger_num = bigger_num, lower_num

    # result - результат умножения, изначально 0
    result = NNumber([0])

    for i in range(len(lower_num)):
        # curr_digit - текущая цифра меньшего числа, на которую умножаем большее число
        curr_digit = lower_num[len(lower_num) - 1 - i]
        # Умножаем большее число на эту цифру
        mul_result = MUL_ND_N(NNumber(bigger_num), curr_digit)
        # Сдвигаем резальтат умножения
        mul_result = MUL_Nk_N(mul_result, i)
        # Прибавляем к результату умножения число, полученное на данном проходе цикда
        result = ADD_NN_N(result, mul_result)

    return result


def SUB_PP_P(pol1: Polynomial, pol2: Polynomial):
    flag = 0
    result = []
    coefs_bigger = pol1.get_coefs()
    coefs_lower = pol2.get_coefs()

    if pol1.get_exp() < pol2.get_exp():
        coefs_bigger, coefs_lower = coefs_lower, coefs_bigger
        flag = 1

    while len(coefs_bigger) > len(coefs_lower):
        coefs_lower.append(RNumber(0, 1))

    for i in range(len(coefs_bigger)):
        if flag:
            result.append(SUB_QQ_Q(coefs_lower[i], coefs_bigger[i]))
        else:
            result.append(SUB_QQ_Q(coefs_bigger[i], coefs_lower[i]))

    print([i.__str__() for i in coefs_bigger])
    print([i.__str__() for i in coefs_lower])
    return result


# rli1 = [RNumber(i * 3, 2 + i) for i in range(5)]
# rli2 = [RNumber(i, 2 + i) for i in range(4)]
# print(MUL_ZZ_Z(Integer(list(input()), False), Integer(list(input()), False)))
# print(MUL_ND_N(NNumber([1,0]), 2))
# print(MUL_ND_N(NNumber(list(input())), 2))
# print(SUB_PP_P(Polynomial(rli1), Polynomial(rli2)))

#print(SUB_PP_P(Polynomial(rli1), Polynomial(rli2)))


print(MUL_ZZ_Z(Integer([1,0], False), Integer([2], False)))
