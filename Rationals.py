from Dtypes import RNumber, Integer, NNumber
import Natural, Integer

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
# MUL_QQ_Q

# Деление дробей
# DIV_QQ_Q
