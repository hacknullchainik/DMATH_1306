class Integer:
    # Классическая инициализация
    # sign выбрал за бул, чтобы меньше шансов было упороться
    # Знак рассматриваем как True = '-', False = '+' (1 - есть, 0 - нет)
    # П.с. к инту кастуйте и не ебите себе мозги int(True) == 1
    def __init__(self, numbers, sign: bool = False):
        if isinstance(numbers, list):
            # value - значение, то бишь массив цифр
            numbers = list(map(int, numbers))
            for i in range(len(numbers) - 1):
                if numbers[0] == 0:
                    numbers.pop(0)
                else:
                    break
            # Обратное представление
            self.__value = numbers[::-1]

            # Последний разряд, то бишь если число длины 5, то это 4(т.к. нумерация с нуля)
            self.__rank = len(numbers) - 1
            # Знак
            if len(numbers) > 1 or numbers[0] != 0:
                self.__sign = sign
            else:
                self.__sign = False
        elif isinstance(numbers, str):
            # Проверяем наличие стронний символов
            for i in numbers:
                if i not in '1234567890-+':
                    raise TypeError(f'{i} не может быть использовано в записи Integer')

            # Смотрим и ставим знак
            if numbers[0] == '+':
                numbers = numbers[1:]
            if numbers[0] == '-':
                if len(numbers) == 1:
                    raise TypeError(f'Нельзя создать число исключительно из знака!')
                elif len(numbers) >= 2:
                    if int(numbers[1]):
                        self.__sign = True
                    else:
                        self.__sign = False

                numbers = numbers[1:]
            else:
                self.__sign = False

            # Создаём список
            self.__value = [int(i) for i in numbers]

            # Убираем незначащие нули
            for i in range(len(self.__value) - 1):
                if self.__value[0] == 0:
                    self.__value.pop(0)
                else:
                    self.__value.reverse()
                    break

            # Записываем ранк
            self.__rank = len(self.__value) - 1


        # Если numbers не строка и не список, кидаем ошибку
        else:
            raise TypeError(f'{type(numbers)} не может быть преобразован в Integer')

    # ЧТОБЫ ВЫВОДИЛОСЬ НОРМАЛЬНО ПРИНТОМ
    def __str__(self):
        if self.__sign:
            return '-' + ''.join(map(str, self.__value[::-1]))
        else:
            return ''.join(map(str, self.__value[::-1]))

    def get_num(self):
        return self.__value.copy()

    def get_rank(self):
        return self.__rank

    def get_sign(self):
        return self.__sign


class NNumber:
    # Классическая инициализация
    def __init__(self, numbers):
        # Если задаётся списком
        if isinstance(numbers, list):
            # value - значение, то бишь массив цифр
            numbers = list(map(int, numbers))
            for i in range(len(numbers) - 1):
                if numbers[0] == 0:
                    numbers.pop(0)
                else:
                    break
            self.__value = numbers[::-1]
            # Последний разряд, то бишь если число длины 5, то это 4(т.к. нумерация с нуля)
            self.__rank = len(numbers) - 1

        # Если задаётся строкой
        elif isinstance(numbers, str):
            # Проверяем наличие стронний символов
            for i in numbers:
                if i not in '1234567890':
                    raise TypeError(f'{i} не может быть использовано в записи NNumber')
            # Создаём список
            self.__value = [int(i) for i in numbers]
            # Убираем не значащие нули
            for i in range(len(self.__value) - 1):
                if self.__value[0] == 0:
                    self.__value.pop(0)
                else:
                    self.__value.reverse()
                    break
            # Записываем ранк
            self.__rank = len(self.__value) - 1
        # Если numbers не строка и не список, кидаем ошибку
        else:
            raise TypeError(f'{type(numbers)} не может быть преобразован в NNumbers')

    # ЧТОБЫ ВЫВОДИЛОСЬ НОРМАЛЬНО ПРИНТОМ
    def __str__(self):
        return ''.join(map(str, self.__value[::-1]))

    def get_num(self):
        return self.__value.copy()

    def get_rank(self):
        return self.__rank


# Модуль числа
def ABS_Z_N(num: Integer):
    num = num.get_num()
    num.reverse()
    return NNumber(num)


# Сравнение чисел
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
            if i == len(result) - 1:
                result.append(1)
            else:
                result[i + 1] += 1
    # Переворачиваем массив, так как работали с обратным порядком цифр
    result.reverse()

    return NNumber(result)


def SUB_NN_N(n: NNumber, m: NNumber):
    # Результирующий массив
    res = []
    # Если n больше
    if COM_NN_D(n, m) == 2:
        n = n.get_num()
        m = m.get_num()
        # Заполняем "пустые" (недостающие) разряды нулями (чтобы длины чисел совпадали)
        while len(m) < len(n):
            m.append(0)
        while len(n) < len(m):
            n.append(0)

        # Поциферно вычитаем, занимая единицу, где это нужно
        for i in range(len(m)):
            if n[i] - m[i] < 0:
                res.append(10 + n[i] - m[i])
                n[i + 1] -= 1
            else:
                res.append(n[i] - m[i])

    # Аналогично, если m больше
    elif COM_NN_D(n, m) == 1:
        n = n.get_num()
        m = m.get_num()
        while len(m) < len(n):
            m.append(0)
        while len(n) < len(m):
            n.append(0)

        for i in range(len(n)):
            if m[i] - n[i] < 0:
                res.append(10 + m[i] - n[i])
                m[i + 1] -= 1
            else:
                res.append(m[i] - n[i])
    else:
        res.append(0)

    # Чистим от лишних нулей
    while res[-1] == 0 and len(res) > 1:
        res.pop()
    result = NNumber(res[::-1])
    return result


# делаем вычитание
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


def GCF_PP_P(num1: Polynomial, num2: Polynomial):
    res = MOD_PP_P(num1, num2)
    while (DEG_P_N(res) != 0):
        num1 = num2
        num2 = res
        res = MOD_PP_P(num1, num2)
    return num2