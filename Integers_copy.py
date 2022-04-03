from Integers import *
import Integers, Naturals
from Integers_test import Itest

# ВСЕ ПРЕДСТАВЛЕННЫЕ ФУНКЦИИ ПРАВИЛЬНО НЕ РАБОТАЮТ,
# В ОСНОВНОЙ ФАЙЛ КИДАТЬ НЕ НАДО

def MOD_ZZ_Z(num: Integer, num_2: Integer):
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
    a_1 = Integers.MUL_ZZ_Z(b, q)

    # SUB_ZZ_Z() -> pending from Nastia <-
    # Substructing the value of the divident multiplied by the quotient from the dividend
    r = SUB_ZZ_Z(a, a_1)

    # MUL_ZM_Z FROM NIKITAT.PY
    # Putting the right sign the resulting integer.
    if a.get_sign() and b.get_sign():
        pass
    else:
        r = Integers.MUL_ZM_Z(r)

    return r


def SUB_ZZ_Z(num1: Integer, num2: Integer):
    # - + = - - (сложение)
    # + - = + + (сложение)
    # - - = - + (не сложение)
    # + + = + -  (не сложение)
    if num1.get_sign() != num2.get_sign():
        res = ADD_NN_N(ABS_Z_N(num1), ABS_Z_N(num2)).get_num()
        res.reverse()
        res = Integer(res, num1.get_sign())
    else:
        if COM_NN_D(num1, num2) == 2:
            sig = num1.get_sign()
        else:
            if num2.get_sign():
                sig = 0
            else:
                sig = 1
        res = SUB_NN_N(ABS_Z_N(num1), ABS_Z_N(num2)).get_num()
        res.reverse()
        res = Integer(res, sig)
    return res


def DIV_ZZ_Z(n: Integer, m: Integer):
    res = []
    # Проверяем числа на знаки (узнаём, в результате будет положительное число или отрицательное)
    if (Integers.POZ_Z_D(n) + Integers.POZ_Z_D(m)) == 4:
        sign = False
    elif (Integers.POZ_Z_D(n) + Integers.POZ_Z_D(m)) == 3:
        sign = True
    else:
        sign = False

    # Берём абсолютные значения (знак уже запомнили) и применяем обычное деление натуральных чисел
    # В результате всё равно целое
    n = Integers.ABS_Z_N(n)
    m = Integers.ABS_Z_N(m)
    res = Naturals.DIV_NN_N(n, m).get_num()

    return Integer(res, sign)


Itest(['MOD_ZZ_Z', 'SUB_ZZ_Z', 'DIV_ZZ_Z'])
