class NNumber:
    # Классическая инициализация
    def __init__(self,numbers:list):
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
    def __init__(self, numbers: list, sign:bool = False):
        # value - значение, то бишь массив цифр
        numbers = list(map(int,numbers))
        for i in range(len(numbers)-1):
            if numbers[0] == 0:
                numbers.pop(0)
            else:
                break
        self.__value = numbers[::-1]
        # Последний разряд, то бишь если число длины 5, то это 4(т.к. нумерация с нуля)
        self.__rank = len(numbers) - 1
        # Знак
        if len(numbers)>1 or numbers[0] != 0:
            self.__sign = sign
        else:
            self.__sign = False

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
    # Теперь непросто, я невнимательно прочитал условие числитель - целое, знаменатель натуральное
    def __init__(self, numerator:Integer, denominator:NNumber = NNumber([1])):
        # если знаменатель == 0 кидаем ошибку
        if int(denominator.__str__()) == 0:
            raise ZeroDivisionError("Знаменатель отрицательный!")

        if numerator.__str__()[0] == '-':
            if int(numerator.__str__()[1:]) == 0:
                self.__num = numerator
                self.__den = 1
            else:
                self.__num = numerator
                self.__den = denominator

        else:
            if int(numerator.__str__()) == 0:
                self.__num = numerator
                self.__den = 1
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


class Polynomial:
    # ЭТТЕНШН крч
    # Список коэффициентов пусть будет списком из объектов класса Rnumber
    def __init__(self, coefficients:list):
        for i in range(len(coefficients)-1):
            if int(coefficients[0]) == 0:
                coefficients.pop(0)
            else:
                break
        self.__coefs = coefficients[::-1]
        # Макс степень
        self.__exp = len(self.__coefs)-1

    # ЧТОБЫ ВЫВОДИЛОСЬ НОРМАЛЬНО ПРИНТОМ
    def __str__(self):
        return ' '.join([f'({r.__str__()})'+f'x^{len(self.__coefs)-1-i}' for i, r in enumerate(self.__coefs) if r.get_num() != 0])

    def get_coefs(self):
        return self.__coefs.copy()

    def get_exp(self):
        return self.__exp


