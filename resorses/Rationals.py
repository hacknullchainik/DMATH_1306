from Dtypes import RNumber, Integer, NNumber
from Integers import *


# Сокращение дроби
def RED_Q_Q(drob: RNumber):
    # сохраняем числитель
    num = drob.get_num()
    # сохраняем знак
    sign = num.get_sign()
    # сохраняем знаменатель
    den = drob.get_den()
    # находим нод
    gcd = GCF_NN_N(den, ABS_Z_N(num))
    # делим числитель и знаменатель на нод
    num = DIV_NN_N(num, gcd)
    den = DIV_NN_N(den, gcd)
    # возвращаем результат
    return RNumber(Integer(num.get_num()[::-1], sign), NNumber(den.get_num()[::-1]))


# Проверка на целое
def INT_Q_B(num: RNumber):
    # Если знаменатель 0 - число целое
    if num.get_num().get_num()[0] == 0:
        return True
    else:
        # сокращаем дробь
        num2 = RED_Q_Q(num)
        # првоеряем является ли знаменатель 1 в сокращенной дроби
        if (num2.get_den().get_num()[0] == 1):
            return True
        else:
            return False


# Преобразование из целого в дробное
def TRANS_Z_Q(num: Integer):
    return RNumber(num.__str__())


# Из дробного в целое, если а/1
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


# Сложение дробей
def ADD_QQ_Q(num1: RNumber, num2: RNumber):
    # Вычисляем НОК (знаменатель искомой дроби)
    den = LCM_NN_N(num1.get_den(), num2.get_den())
    # Вычисляем числитель первой дроби после приведения к общему знаменателю
    num1_converted = MUL_ZZ_Z(num1.get_num(), TRANS_N_Z(DIV_NN_N(den, num1.get_den())))
    # Вычисляем числитель второй дроби после приведения к общему знаменателю
    num2_converted = MUL_ZZ_Z(num2.get_num(), TRANS_N_Z(DIV_NN_N(den, num2.get_den())))
    # Суммируем числители
    num = ADD_ZZ_Z(num1_converted, num2_converted)
    # Возвращаем сокращённую дробь
    return RED_Q_Q(RNumber(num, den))


# Вычитание дробей
def SUB_QQ_Q(num_1: RNumber, num_2: RNumber):
    # Вычисляем НОК (знаменатель искомой дроби)
    den = LCM_NN_N(num_1.get_den(), num_2.get_den())
    # Вычисляем числитель первой дроби после приведения к общему знаменателю
    num_1_converted = MUL_ZZ_Z(num_1.get_num(), TRANS_N_Z(DIV_NN_N(den, num_1.get_den())))
    # Вычисляем числитель второй дроби после приведения к общему знаменателю
    num_2_converted = MUL_ZZ_Z(num_2.get_num(), TRANS_N_Z(DIV_NN_N(den, num_2.get_den())))
    # Суммируем числители
    num = SUB_ZZ_Z(num_1_converted, num_2_converted)
    # Возвращаем сокращённую дробь
    return RED_Q_Q(RNumber(num, den))


# Умножение дробей
def MUL_QQ_Q(n1: RNumber, n2: RNumber):
    # берутся отдельно числители(num1, num2, с учетом их знака) и знаменатели(den1, den2)
    num1 = n1.get_num()
    num2 = n2.get_num()

    den1 = n1.get_den()
    den2 = n2.get_den()

    # первый числитель умножается на второй,
    # а первый знаменатель умножается на второй
    # результирующий числитель и знаменатель записываются в result_num и result_den, соответственно.
    result_num = MUL_ZZ_Z(num1, num2)
    result_den = MUL_NN_N(den1, den2)

    return RED_Q_Q(RNumber(result_num, result_den))


# Деление дробей
def DIV_QQ_Q(n1: RNumber, n2: RNumber):
    # берутся отдельно числители(num1, num2, с учетом их знака) и знаменатели(den1, den2)

    num1 = n1.get_num()
    num2 = n2.get_num()

    den1 = n1.get_den()
    den2 = n2.get_den()

    # первый числитель умножается на второй,
    # а первый знаменатель умножается на второй
    # результирующий числитель и знаменатель записываются в result_num и result_den, соответственно.
    # если знаки результирующего числителя и знаменателя одинаковы - результат положителен,
    # иначе - отрицателен
    # знак считаем XOR'ом
    sign = num1.get_sign() ^ num2.get_sign()

    den2 = Integer(den2.get_num()[::-1], False)
    num2 = NNumber(num2.get_num()[::-1])
    result_num = MUL_ZZ_Z(num1, den2)
    result_den = MUL_NN_N(den1, num2)
    result_num = result_num.get_num()[::-1]
    result_den = result_den.get_num()[::-1]
    # возвращаем сокращенную дробь
    return RED_Q_Q(RNumber(Integer(result_num, sign), NNumber(result_den)))