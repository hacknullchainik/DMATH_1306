# v 0.47 Добавлены плюшки вывода Polynomial, параметр simple у __str__() выводит "сухие" коэфициенты
# v 0.45 (minor) Исправлена ошибка вывода Polynomial
# Че добавил: (Change log) (0.43)
# 1. Integer и NNumber можно теперь задавать строками '123' итп
# 2. RNumber теперь представляется двумя элементами Integer - числитель, NNumber - знаменатель
# 3. RNumber можно задать строкой! '-123/123' или '123','123'
# 4. Polynomial можно задать строкой! '0 0 0 123/166 0 123/123 -1999/1'
# 5. !!!! Ранг чисел задаётся старшим разрядом: ранг 123 == 2

class NNumber:
    # Классическая инициализация
    def __init__(self,numbers):
        # Если задаётся списком
        if isinstance(numbers,list):
            # value - значение, то бишь массив цифр
            numbers = list(map(int, numbers))
            for i in range(len(numbers)-1):
                if numbers[0] == 0:
                    numbers.pop(0)
                else:
                    break
            self.__value = numbers[::-1]
            # Последний разряд, то бишь если число длины 5, то это 4(т.к. нумерация с нуля)
            self.__rank = len(numbers)-1

        # Если задаётся строкой
        elif isinstance(numbers,str):
            # Проверяем наличие стронний символов
            for i in numbers:
                if i not in '1234567890':
                    raise TypeError(f'\'{i}\' не может быть использовано в записи NNumber')
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
            self.__rank = len(self.__value)-1
        # Если numbers не строка и не список, кидаем ошибку
        else:
            raise TypeError(f'{type(numbers)} не может быть преобразован в NNumbers')

    # ЧТОБЫ ВЫВОДИЛОСЬ НОРМАЛЬНО ПРИНТОМ
    def __str__(self):
        return ''.join(map(str,self.__value[::-1]))

    def get_num(self):
        return self.__value.copy()

    def get_rank(self):
        return self.__rank


class Integer:
    # Классическая инициализация
    # sign выбрал за бул, чтобы меньше шансов было упороться
    # Знак рассматриваем как True = '-', False = '+' (1 - есть, 0 - нет)
    # П.с. к инту кастуйте и не ебите себе мозги int(True) == 1
    def __init__(self, numbers, sign: bool = False):
        if isinstance(numbers,list):
            # value - значение, то бишь массив цифр
            numbers = list(map(int,numbers))
            for i in range(len(numbers)-1):
                if numbers[0] == 0:
                    numbers.pop(0)
                else:
                    break
            # Обратное представление
            self.__value = numbers[::-1]

            # Последний разряд, то бишь если число длины 5, то это 4(т.к. нумерация с нуля)
            self.__rank = len(numbers) - 1
            # Знак
            if len(numbers)>1 or numbers[0] != 0:
                self.__sign = sign
            else:
                self.__sign = False
        elif isinstance(numbers, str):
            # Проверяем наличие стронний символов
            for i in numbers:
                if i not in '1234567890-+':
                    raise TypeError(f'\'{i}\' не может быть использовано в записи Integer')

            # Смотрим и ставим знак
            if numbers[0] =='+':
                numbers =numbers[1:]
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
            self.__rank = len(self.__value)-1


        # Если numbers не строка и не список, кидаем ошибку
        else:
            raise TypeError(f'{type(numbers)} не может быть преобразован в Integer')

    # ЧТОБЫ ВЫВОДИЛОСЬ НОРМАЛЬНО ПРИНТОМ
    def __str__(self):
        if self.__sign:
            return '-'+''.join(map(str, self.__value[::-1]))
        else:
            return ''.join(map(str, self.__value[::-1]))

    def get_num(self):
        return self.__value.copy()

    def get_rank(self):
        return self.__rank

    def get_sign(self):
        return self.__sign


class RNumber:
    # числитель, знаменатель - всё просто
    # ПС !!!!
    # Теперь непросто, я невнимательно прочитал условие числитель - целое, знаменатель натуральное
    def __init__(self, numerator, denominator = None):
        # Если пара Integer/NNumber
        if isinstance(numerator,Integer) and isinstance(denominator, NNumber):
            pass
        # Если пара строка/строка
        elif isinstance(numerator,str) and isinstance(denominator, str):
            numerator = Integer(numerator)
            denominator = NNumber(denominator)
        # Если пара (строка или Integer) и не задан знаменатель
        elif (isinstance(numerator,str) or isinstance(numerator,Integer)) and denominator is None:
            # Если числитель - строка
            if isinstance(numerator,str):
                # Считаем разделители и
                if numerator.count('/') == 0:
                    numerator = Integer(numerator)
                    denominator = NNumber('1')
                elif numerator.count('/') > 1:
                    raise ValueError('Слишком много \'/\' для RNumber: {}'.format(numerator.count('/')))
                else:
                    numerator, denominator = numerator.split('/')
                    numerator = Integer(numerator)
                    denominator = NNumber(denominator)
            # Иначе (т.е. если числитель и так Integer
            else:
                denominator = NNumber('1')
        else:
            raise TypeError(f'{type(numerator)} и {type(denominator)} не могут быть преобразованны в RNumber')

        # если знаменатель == 0 кидаем ошибку
        if int(denominator.__str__()) == 0:
            raise ZeroDivisionError("Знаменатель отрицательный!")

        if numerator.get_rank() == 0 and not numerator.get_num()[0]:
            self.__num = numerator
            self.__den = NNumber('1')
        else:
            self.__num = numerator
            self.__den = denominator

    # ЧТОБЫ ВЫВОДИЛОСЬ НОРМАЛЬНО ПРИНТОМ
    def __str__(self):
        if self.__den.__str__() == '1':
            return self.__num.__str__()
        else:
            return f'{self.__num.__str__()}/{self.__den.__str__()}'

    def get_num(self):
        return self.__num

    def get_den(self):
        return self.__den

    def get_sign(self):
        return self.__num.get_sign()


class Polynomial:
    # ЭТТЕНШН крч
    # Список коэффициентов пусть будет списком из объектов класса Rnumber
    def __init__(self, coefficients):
        if isinstance(coefficients,list):
            pass
        elif isinstance(coefficients, str):
            coefficients = list(map(RNumber, coefficients.split()))
        else:
            raise TypeError(f'{type(coefficients)} не может быть преобразован в Polynomial')

        for i in range(len(coefficients) - 1):
            if int(coefficients[0].get_num().get_num()[-1]) == 0:
                coefficients.pop(0)
            else:
                break
        self.__coefs = coefficients[::-1]
        # Макс степень
        self.__exp = len(self.__coefs) - 1

    # ЧТОБЫ ВЫВОДИЛОСЬ НОРМАЛЬНО ПРИНТОМ
    def __str__(self, show_exp=False, simple=False):
        # Результирующая строка
        res_str = ''
        # i - счётчик, с - элемент списка
        if simple:
            return ' '.join([i.__str__() for i in self.__coefs[::-1]])
        else:
            for i, c in enumerate(self.__coefs[::-1]):
                # Если число отрицательное
                if c.get_sign():
                    res_str += ' -'

                # Добавляем ' + ' если элемент не последний

                elif i > 0 and int(c.get_num().get_num()[-1]):
                    res_str += ' + '
                # Добавляем элемент в рез. строку, если он не равен 0
                if int(c.get_num().__str__()):
                    if c.get_den().get_rank() == 0 and int(c.get_den().get_num()[0]) == 1:
                        res_str += '{}'.format(c.__str__().replace('-', ''))
                    else:
                        res_str += '({})'.format(c.__str__().replace('-',''))
                    if i-self.__exp != 0:
                        res_str += f'x^{self.__exp-i}'
                elif not i-self.__exp and len(res_str) == 0:
                    res_str += '0'
            if show_exp:
                res_str += f'\nexp is: {self.__exp}'
        return res_str
        # return '  '.join([f'({r.__str__()})'+f'x^{len(self.__coefs)-1-i}' for i, r in enumerate(self.__coefs[::-1]) if r.get_num() != 0])

    def get_coefs(self):
        return self.__coefs.copy()

    def get_exp(self):
        return self.__exp