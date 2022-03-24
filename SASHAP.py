from Dtypes import RNumber, NNumber, Integer, Polynomial


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
        # в массив цифры заночились с конца

        while numer > 0:
            numer_list.append(numer % 10)
            numer //= 10

        numer_list.reverse()

        return Integer(numer_list, sign)

    # В случае, если знаменатель
    # не равен нулю, функция возвращает изначальную дробь

    else:
        return num


def COM_NN_D(num1: NNumber, num2: NNumber):
    # Берём числа в нормальном порядке
    num1 = num1.get_num()
    num2 = num2.get_num()
    num2.reverse()
    num1.reverse()
    # Сравниваем по цифрам, если длины чисел равны
    if len(num1) == len(num2):
        for i in range(len(num1)):
            if num1[i] > num2[i]:
                return 2
            if num2[i] > num1[i]:
                return 1
        return 0
    elif len(num1) > len(num2):
        return 2
    else:
        return 1


def ADD_NN_N(number1: NNumber, number2: NNumber):
    # Создаем дубликаты наших цифровых массивов (по факту - чисел) для более удобной работы
    bigger_num = number1.get_num()
    lower_num = number2.get_num()
    result = []

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
            if i == len(result):
                result.append(1)
            else:
                result[i + 1] += 1
    # Переворачиваем массив, так как работали с обратным порядком цифр
    result.reverse()

    return NNumber(result)


