from Dtypes import RNumber, Integer, NNumber
from Naturals import *
from Integers import *

# Сокращение дроби
# RED_Q_Q

# Проверка на целое
# INT_Q_B

# Преобразование из целого в дробное
def TRANS_Z_Q(num: Integer):
    sign = num.get_sign()
    num = list(map(str, num.get_num()))
    num.reverse()
    num = int("".join(num))
    if (sign):
        num = -num
    return RNumber(num, 1)

# Из дробного в целое, если а/1
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

# Сложение дробей
# ADD_QQ_Q

# Вычитание дробей
# SUB_QQ_Q

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
# DIV_QQ_Q
