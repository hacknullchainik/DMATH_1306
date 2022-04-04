from Polynomials import *
from Naturals_test import *
from Polynomials_test import *
from Rationals_test import *
from Integers_test import *


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
    numer = num.get_num()

    # Проверяем, равен ли знаменатель единице и продолжаем работу в случае равенства

    if COM_NN_D(num.get_den(), NNumber("1")) == 0:
        return numer

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
    # if COM_NN_D(num1, NNumber("0")) == 0:
    #     return 0
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
    if not int(num2.__str__()):
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
    flag = 0  # Переменная, показывающая, менялись ли значения местами
    result = []
    coefs_bigger = pol1.get_coefs()
    coefs_lower = pol2.get_coefs()

    # Меняем местами массивы коэффициентов, если степень первого больше степени второго
    if pol1.get_exp() < pol2.get_exp():
        coefs_bigger, coefs_lower = coefs_lower, coefs_bigger
        flag = 1

    # Добавляем незначащие нули в массиве коэффициентов многочлена с меньшей степенью, пока длины массивов
    # не будут одинаковыми
    while len(coefs_bigger) > len(coefs_lower):
        coefs_lower.append(RNumber("0"))

    # Вычитаем соответствующие коэффициенты
    for i in range(len(coefs_bigger)):
        if flag:
            result.append(SUB_QQ_Q(coefs_lower[i], coefs_bigger[i]))
        else:
            result.append(SUB_QQ_Q(coefs_bigger[i], coefs_lower[i]))

    result.reverse()

    return Polynomial(result)

#
# Ntest(Nlist)
# Itest(Ilist)
# Rtest(Rlist)


# Ptest(Plist)
# a, b = '123', '-9'
# print(str(int(a) // int(b)))

# print(LCM_NN_N(NNumber('1122211111111'), NNumber('100000000000000000000000000000000000')))
# Itest(['DIV_ZZ_Z'])

# print(DIV_ZZ_Z(Integer("319"), Integer("76")))
# print(DIV_ZZ_Z(Integer("-123"), Integer))
# Rtest(Rlist)
Ptest(['MOD_PP_P'])
# print(MUL_ND_N(NNumber("116"), 9))
# print("MUL_ZZ_Z: 116 * 19 = {0}".format(MUL_ZZ_Z(Integer("116"), Integer("19"))))


# print(SUB_ZZ_Z(Integer("2"), Integer("5")))
# print(-1022309069483458235506786240306/773217126302724074012569452338179)
# print(-5447957122673541/4120528591947753500)
# print(DIV_PP_P(Polynomial('2 -11 19 -13 3'), Polynomial('2 -3 1')))
# print("MOD_ZZ_Z (123mod(-9)): {0}".format(MOD_ZZ_Z(Integer('123'), Integer('-9'))))
# print(MUL_NN_N(NNumber("4331817108397227"), NNumber("228")))
# print(4331817108397227*228)

# print(6726762439834275649822587948797802587/862536767676790869428574869848935876)
# print(45582315319138840/5844776483523759)
# print(987654321234567890/2)

def DIV_ZZ_Z(num: Integer, num_2: Integer):
    # Конвертируем числа из типа Integer в тип Nnumber
    a = TRANS_Z_N(num)
    b = TRANS_Z_N(num_2)

    temp = DIV_NN_N(a, b)
    # Запоминаем занки, для определения будущего знака числа
    sign1 = num.get_sign()
    sign2 = num_2.get_sign()

    if sign1 == False and sign2 == False:
        res = temp
    elif sign1 == False and sign2 == True:
        res = Integer(temp.get_num(), True)
    elif sign1 == True and sign2 == False:
        res = Integer(temp.get_num(), True)
        res = SUB_ZZ_Z(res, Integer("1", False))
    elif sign1 == True and sign2 == True:
        res = ADD_ZZ_Z(Integer(temp.get_num(), False), Integer("1", False))

    return res


def MOD_ZZ_Z(num: Integer, num_2: Integer):
    # Конвертируем числа из типа Integer в тип Nnumber

    a = TRANS_Z_N(num)
    b = TRANS_Z_N(num_2)

    div = DIV_ZZ_Z(num, num_2)

    temp = MOD_NN_N(a, b)
    # Запоминаем занки, для определения будущего знака числа
    sign1 = num.get_sign()
    sign2 = num_2.get_sign()

    if sign1 == False and sign2 == False:
        res = Integer(temp.get_num(), False)
    elif sign1 == False and sign2 == True:
        res = Integer(temp.get_num(), False)
    elif sign1 == True and sign2 == False:
        res = SUB_ZZ_Z(num, MUL_ZZ_Z(num_2, div))
    elif sign1 == True and sign2 == True:
        res = SUB_ZZ_Z(num, MUL_ZZ_Z(num_2, div))

    return res

def MUL_Pxk_P(poly_1: Polynomial, poly_2: int):
    poly_2 = Polynomial('1' + ' 0 ' * poly_2)

    p_1 = ''
    p_2_cof = 0

    # This loop looks for the coefficient of the x^k that will be multiplied to poly_1.
    for i in poly_2.get_coefs():
        if i.get_num() != 0:
            p_2_cof = i

    # Multiplying each coefficient to one another.
    for i in poly_1.get_coefs()[::-1]:
        p_1 += str(MUL_QQ_Q(i, p_2_cof))
        p_1 += ' '
    p_1 = p_1[:-1]

    # Increasing the value of the exponents of our polynomial by k.
    for i in range(poly_2.get_exp()):
        p_1 += ' 0'

    return Polynomial(p_1)