from Dtypes import Integer, NNumber
import Naturals

# Модуль числа
def ABS_Z_N(num: Integer):
    num = num.get_num()
    num.reverse()
    return NNumber(num)

#FIXED
# Сравнение с нулем
def POZ_Z_D(num: Integer):
    # Проверяем сначала первый символ массива,
    # ведь если наше число было нулем, в первом элементе тоже будет ноль
    if num.get_num()[-1] == 0:
        return 0
    elif num.get_sign():
        return 1

    else:
        return 2

# FIXED
# Умножение числа на -1
def MUL_ZM_Z(num: Integer):
    if num.get_sign():
        result = Integer(num.get_num()[::-1], False)
    else:
        result = Integer(num.get_num()[::-1], True)

    return result

# FIXED
# Из натурального в целое
def TRANS_N_Z(num:NNumber):
    return Integer(num.get_num()[::-1], False)


# из целого (неотрицательного) в натуральное
def TRANS_Z_N(num: Integer):
    num = num.get_num()
    num.reverse()
    return NNumber(num)

# Сумма целых чисел
# ADD_ZZ_Z

# Разность целых чисел
# SUB_ZZ_Z

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
    result = Naturals.MUL_NN_N(lower_num, bigger_num)

    # Знак числа, получаемого при умножении легко вычисляется XOR'ом
    res_sign = sign1 ^ sign2
    result_digits = result.get_num()
    result_digits.reverse()

    result = Integer(result_digits, res_sign)
    return result

# Целая часть деления двух чисел
# DIV_ZZ_Z

# Остаток от деления двух целых чисел
# MOD_ZZ_Z