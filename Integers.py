from Dtypes import Integer, NNumber
from Naturals import *

# Модуль числа
def ABS_Z_N(num: Integer):
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
    if num.get_sign():
        result = Integer(num.get_num()[::-1], False)
    else:
        result = Integer(num.get_num()[::-1], True)

    return result

# Из натурального в целое
def TRANS_N_Z(num:NNumber):
    return Integer(num.get_num()[::-1], False)

# из целого (неотрицательного) в натуральное
def TRANS_Z_N(num: Integer):
    num = num.get_num()
    num.reverse()
    return NNumber(num)

# Сумма целых чисел
def ADD_ZZ_Z(num1:Integer, num2:Integer):
    #если знаки чисел равны, то результат складывается
    if num1.get_sign() == num2.get_sign():
        res = ADD_NN_N(ABS_Z_N(num1),ABS_Z_N(num2)).get_num()
        res.reverse()
        res = Integer(res,num1.get_sign())
    #если разные знаки, то будет происходить вычетание со сравнением чисел
    else:
        if (num1.get_sign() == True) and (num2.get_sign() == False) and (COM_NN_D(ABS_Z_N(num1), ABS_Z_N(num2)) == 1):
            res = SUB_NN_N(ABS_Z_N(num2),ABS_Z_N(num1)).get_num()
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
def SUB_ZZ_Z(num1:Integer, num2:Integer):
    # - + = - - (сложение)
    # + - = + + (сложение)
    # - - = - + (не сложение)
    # + + = + -  (не сложение)
    if num1.get_sign() != num2.get_sign():
        res = ADD_NN_N(ABS_Z_N(num1),ABS_Z_N(num2)).get_num()
        res.reverse()
        res = Integer(res,num1.get_sign())
    else:
        if COM_NN_D(num1,num2)  == 2:
            sig = num1.get_sign()
        else:
            if num2.get_sign():
                sig = 0
            else:
                sig = 1
        res = SUB_NN_N(ABS_Z_N(num1),ABS_Z_N(num2)).get_num()
        res.reverse()
        res = Integer(res,sig)
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

    return Integer(res, sign)

# Остаток от деления двух чисел
def MOD_ZZ_Z(num: Integer, num_2: Integer):
    # The function finds the remainder by using the euclidian theorem.
    # 'a' stores the value of the dividend.
    # 'b' stores the value of the divisor.
    # 'q' stores the value of the quotient.
    # 'r' stores the value of the remainder.

    a = Integer(num.get_num()[::-1], num.get_sign())
    b = Integer(num_2.get_num()[::-1], num_2.get_sign())

    # DIV_ZZ_Z FROM NIKITAT.PY
    # Finding the quotient from the division of an integer by an integer
    q = DIV_ZZ_Z(a, b)

    # MUL_ZZ_Z FROM SASHAP.PY
    # Storing the value of the divisor multiplied by the quotient
    a_1 = MUL_ZZ_Z(a, q)

    # SUB_ZZ_Z() -> pending from Nastia <-
    # Substructing the value of the divident multiplied by the quotient from the dividend
    r = SUB_ZZ_Z(a, a_1)

    # MUL_ZM_Z FROM NIKITAT.PY
    # Putting the right sign the resulting integer.
    if a.get_sign() and b.get_sign():
        pass
    else:
        r = MUL_ZM_Z(r)

    return r

