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
    # ведь если наше число было нулем, в первом элементе тоже будет ноль
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
    bigger_num = TRANS_Z_N(num1)
    lower_num = TRANS_Z_N(num2)
    # - + = - - (сложение)
    # + - = + + (сложение)
    # - - = - + (не сложение)
    # + + = + -  (не сложение)
    if num1.get_sign() != num2.get_sign():
        res = ADD_NN_N(ABS_Z_N(num1), ABS_Z_N(num2)).get_num()
        res.reverse()
        res = Integer(res, num1.get_sign())
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
def DIV_ZZ_Z(n: Integer, m: Integer):
    res = []
    # Проверяем числа на знаки (узнаём, в результате будет положительное число или отрицательное)
    if (POZ_Z_D(n) + POZ_Z_D(m)) == 4:
        sign = False
    elif (POZ_Z_D(n) + POZ_Z_D(m)) == 3:
        sign = True
    else:
        sign = False

    # Берём абсолютные значения (знак уже запомнили) и применяем обычное деление натуральных чисел
    # В результате всё равно целое
    n = ABS_Z_N(n)
    m = ABS_Z_N(m)
    res = DIV_NN_N(n, m).get_num()
    res.reverse()

    return Integer(res, sign)


# Остаток от деления двух чисел
def MOD_ZZ_Z(num: Integer, num_2: Integer):
    # Конвертируем числа из типа Integer в тип Nnumber
    a = TRANS_Z_N(num)
    b = TRANS_Z_N(num_2)

    # Запоминаем занки, для определения будущего знака числа
    sign1 = num.get_sign()
    sign2 = num_2.get_sign()

    # С помощью XOR определяем знак результата
    sign_res = sign1 ^ sign2

    # Применяем уже готовую функцию для натуральных чисел
    res = MOD_NN_N(a, b)

    # Формируем результат
    result = TRANS_N_Z(res).get_num()
    result = Integer(result, sign_res)

    return result
