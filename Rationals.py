from Dtypes import RNumber, Integer, NNumber
from Integers import *

# Сокращение дроби
def RED_Q_Q(drob: RNumber):
    num = drob.get_num()
    sign = num.get_sign()
    den = drob.get_den()
    gcd = GCF_NN_N(den,ABS_Z_N(num))
    num = DIV_NN_N(num,gcd)
    den = DIV_NN_N(den, gcd)
    return RNumber(Integer(num.get_num()[::-1],sign), NNumber(den.get_num()[::-1]))

# Проверка на целое
def INT_Q_B(num: RNumber):
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
def ADD_QQ_Q(num1:RNumber,num2:RNumber):
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
    if n1.get_sign() == False:
        num1 = Integer([int(i) for i in str(n1.get_num()) if '0' <= i <= '9'], False)
    else:
        num1 = Integer([int(i) for i in str(n1.get_num()) if '0' <= i <= '9'], True)

    if n2.get_sign() == False:
        num2 = Integer([int(i) for i in str(n2.get_num()) if '0' <= i <= '9'], False)
    else:
        num2 = Integer([int(i) for i in str(n2.get_num()) if '0' <= i <= '9'], True)

    den1 = NNumber([int(i) for i in str(n1.get_den()) if '0' <= i <= '9'])
    den2 = NNumber([int(i) for i in str(n2.get_den()) if '0' <= i <= '9'])

    # первый числитель умножается на второй,
    # а первый знаменатель умножается на второй
    # результирующий числитель и знаменатель записываются в result_num и result_den, соответственно.
    result_num = MUL_ZZ_Z(num1, num2)
    result_den = MUL_NN_N(den1, den2)


    # если знаки результирующего числителя и знаменателя одинаковы - результат положителен,
    # иначе - отрицателен
    if result_num.get_sign() == False:
        result_num = result_num.get_num()[::-1]
        result_den = result_den.get_num()[::-1]
        return RNumber(Integer(result_num ,False), NNumber(result_den))
    else:
        result_num = result_num.get_num()[::-1]
        result_den = result_den.get_num()[::-1]
        return RNumber(Integer(result_num,True), NNumber(result_den))

# Деление дробей
def DIV_QQ_Q(n1: RNumber, n2: RNumber):
    # берутся отдельно числители(num1, num2, с учетом их знака) и знаменатели(den1, den2)

    if n1.get_sign() == False:
        num1 = Integer([int(i) for i in str(n1.get_num().get_num()[::-1]) if '0' <= i <= '9'], False)
    else:
        num1 = Integer([int(i) for i in str(n1.get_num().get_num()[::-1]) if '0' <= i <= '9'], True)

    if n2.get_sign() == False:
        num2 = Integer([int(i) for i in str(n2.get_num().get_num()[::-1]) if '0' <= i <= '9'], False)
    else:
        num2 = Integer([int(i) for i in str(n2.get_num().get_num()[::-1]) if '0' <= i <= '9'], True)

    den1 = NNumber([int(i) for i in str(n1.get_den().get_num()[::-1]) if '0' <= i <= '9'])
    den2 = NNumber([int(i) for i in str(n2.get_den().get_num()[::-1]) if '0' <= i <= '9'])

    # первый числитель умножается на второй,
    # а первый знаменатель умножается на второй
    # результирующий числитель и знаменатель записываются в result_num и result_den, соответственно.
    # если знаки результирующего числителя и знаменателя одинаковы - результат положителен,
    # иначе - отрицателен
    if (num1.get_sign() == False and num2.get_sign() == False) or (num1.get_sign() == True and num2.get_sign() == True):
        den2 = Integer(den2.get_num()[::-1], False)
        num2 = NNumber(num2.get_num()[::-1])
        result_num = MUL_ZZ_Z(num1, den2)
        result_den = MUL_NN_N(den1, num2)
        result_num = result_num.get_num()[::-1]
        result_den = result_den.get_num()[::-1]
        return RED_Q_Q(RNumber(Integer(result_num ,False), NNumber(result_den)))
    else:
        den2 = Integer(den2.get_num()[::-1], False)
        num2 = NNumber(num2.get_num()[::-1])
        result_num = MUL_ZZ_Z(num1, den2)
        result_den = MUL_NN_N(den1, num2)
        result_num = result_num.get_num()[::-1]
        result_den = result_den.get_num()[::-1]
        return RED_Q_Q(RNumber(Integer(result_num, True), NNumber(result_den)))


