from Dtypes import Integer, NNumber
from Naturals import *


# Модуль числа
def ABS_Z_N(num: Integer):
    # Возвращаем числа без знака
    num = num.get_num()
    num.reverse()
    return NNumber(num)


# Сравнение с нулем
def POZ_Z_D(num: Integer):
    # Проверяем сначала первый символ массива,
    # ведь если наше число было нулем, единственным элекментом массива  будет ноль
    if num.get_num()[-1] == 0:
        return 0
    # Проверяем знак числа
    elif num.get_sign():
        return 1
    else:
        return 2


# Умножение числа на -1
def MUL_ZM_Z(num: Integer):
    # Меняем знак числа
    if num.get_sign():
        result = Integer(num.get_num()[::-1], False)
    else:
        result = Integer(num.get_num()[::-1], True)

    return result


# Из натурального в целое
def TRANS_N_Z(num: NNumber):
    # возвращаем число со знаком +
    return Integer(num.get_num()[::-1], False)


# из целого (неотрицательного) в натуральное
def TRANS_Z_N(num: Integer):
    # берем число без знака и переводим в тип integer
    num = num.get_num()
    num.reverse()
    return NNumber(num)


# Сумма целых чисел
def ADD_ZZ_Z(num1: Integer, num2: Integer):
    # если знаки чисел равны, то результат складывается
    if num1.get_sign() == num2.get_sign():
        res = ADD_NN_N(ABS_Z_N(num1), ABS_Z_N(num2)).get_num()
        res.reverse()
        res = Integer(res, num1.get_sign())
    # если разные знаки, то будет происходить вычетание со сравнением чисел
    else:
        if (num1.get_sign() == True) and (num2.get_sign() == False) and (COM_NN_D(ABS_Z_N(num1), ABS_Z_N(num2)) == 1):
            res = SUB_NN_N(ABS_Z_N(num2), ABS_Z_N(num1)).get_num()
            res.reverse()
            res = Integer(res, False)
        elif (num1.get_sign() == True) and (num2.get_sign() == False) and (COM_NN_D(ABS_Z_N(num1), ABS_Z_N(num2)) == 2):
            res = SUB_NN_N(ABS_Z_N(num1), ABS_Z_N(num2)).get_num()
            res.reverse()
            res = Integer(res, True)
        elif (num1.get_sign() == False) and (num2.get_sign() == True) and (COM_NN_D(ABS_Z_N(num1), ABS_Z_N(num2)) == 2):
            res = SUB_NN_N(ABS_Z_N(num1), ABS_Z_N(num2)).get_num()
            res.reverse()
            res = Integer(res, False)
        else:
            res = SUB_NN_N(ABS_Z_N(num2), ABS_Z_N(num1)).get_num()
            res.reverse()
            res = Integer(res, True)
    return res


# Разность целых чисел
def SUB_ZZ_Z(num1: Integer, num2: Integer):
    # Записываем модули чисел в новые переменные чтобы проще было работать
    bigger_num = TRANS_Z_N(num1)
    lower_num = TRANS_Z_N(num2)
    # - + = - - (сложение)
    # + - = + + (сложение)
    # - - = - + (не сложение)
    # + + = + -  (не сложение)

    # Как видно из таблицы выше - если знаки разные, то это железобетонно сложение по модулю
    # знак результата будет определяться знаком уменьшаемого
    if num1.get_sign() != num2.get_sign():
        res = ADD_NN_N(ABS_Z_N(num1), ABS_Z_N(num2)).get_num()
        res.reverse()
        res = Integer(res, num1.get_sign())
    # Если не сложение - значит вычитание по модулю, остается определить знак результата, в данном случаее просто
    # перебором вариантов
    else:
        if COM_NN_D(bigger_num, lower_num) == 2:
            sig = num1.get_sign()
        else:
            if num2.get_sign():
                sig = 0
            else:
                sig = 1

        if COM_NN_D(bigger_num, lower_num) == 1:
            bigger_num, lower_num = lower_num, bigger_num

        res = SUB_NN_N(bigger_num, lower_num).get_num()
        res.reverse()
        res = Integer(res, sig)
    return res


# Произведение целых чисел
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


# Целая часть деления двух чисел
def DIV_ZZ_Z(num: Integer, num_2: Integer):
    if num_2.get_num()[0] == 0:
        raise ZeroDivisionError
    # Конвертируем числа из типа Integer в тип Nnumber
    a = TRANS_Z_N(num)
    b = TRANS_Z_N(num_2)

    # Отношение модулей записываем в отдельную переменную для удобства
    temp = DIV_NN_N(a, b)
    # Запоминаем занки, для определения будущего знака числа
    sign1 = num.get_sign()
    sign2 = num_2.get_sign()
    if COM_NN_D(MUL_NN_N(temp, b), a) == 0:
        return Integer(temp.get_num(), (sign1 ^ sign2))

    # перебираем варианты знаков чисел и для каждого делаем свою процедуру деления
    # подробнее можете ознакомиться вот тут, очень подробно и явно понятнее
    # http://www.cleverstudents.ru/numbers/division_of_integers_with_remainder.html
    if sign1 == False and sign2 == False:
        res = temp
    elif sign1 == False and sign2 == True:
        res = Integer(temp.get_num()[::-1], True)
    elif sign1 == True and sign2 == False:
        res = Integer(temp.get_num()[::-1], True)
        res = SUB_ZZ_Z(res, Integer("1", False))
    elif sign1 == True and sign2 == True:
        res = ADD_ZZ_Z(Integer(temp.get_num()[::-1], False), Integer("1", False))

    return res


def MOD_ZZ_Z(num: Integer, num_2: Integer):
    # Проверяем делитель на ноль
    if num_2.get_num()[0] == 0:
        raise ZeroDivisionError

    div = DIV_ZZ_Z(num, num_2)
    if MUL_ZZ_Z(div, num_2) == num:
        return Integer("0", False)

    # Конвертируем числа из типа Integer в тип Nnumber
    a = TRANS_Z_N(num)
    b = TRANS_Z_N(num_2)

    # Запоминаем остаток от деления модулей чисел для удобства
    temp = MOD_NN_N(a, b)
    # Запоминаем занки, для определения будущего знака числа
    sign1 = num.get_sign()
    sign2 = num_2.get_sign()

    # На том же сайте расписано все и про остатки, для каждого случая варианты разные
    if sign1 == False and sign2 == False:
        res = Integer(temp.get_num()[::-1], False)
    elif sign1 == False and sign2 == True:
        res = Integer(temp.get_num()[::-1], False)
    elif sign1 == True and sign2 == False:
        res = SUB_ZZ_Z(num, MUL_ZZ_Z(num_2, div))
    elif sign1 == True and sign2 == True:
        res = SUB_ZZ_Z(num, MUL_ZZ_Z(num_2, div))

    return res
