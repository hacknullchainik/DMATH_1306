class Integer:
    # Классическая инициализация
    # sign выбрал за бул, чтобы меньше шансов было упороться
    # Знак рассматриваем как True = '-', False = '+' (1 - есть, 0 - нет)
    # П.с. к инту кастуйте и не ебите себе мозги int(True) == 1
    def __init__(self, numbers: list, sign:bool):
        # value - значение, то бишь массив цифр
        self.__value = numbers[::-1]
        # Последний разряд, то бишь если число длины 5, то это 4(т.к. нумерация с нуля)
        self.__rank = len(numbers) - 1
        # Знак
        self.__sign = sign

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
    def __init__(self, numerator:int, denominator:int):
        self.__num = numerator
        self.__den = denominator
        if not denominator:
            raise ZeroDivisionError
        if self.__num < 0 and self.__den < 0:
            self.__num = abs(self.__num)
            self.__den = abs(self.__den)
        elif self.__num < 0 or self.__den < 0:
            if self.__den < 0:
                self.__num = -self.__num
                self.__den = -self.__den

    # ЧТОБЫ ВЫВОДИЛОСЬ НОРМАЛЬНО ПРИНТОМ
    def __str__(self):
        if not self.__num:
            return f'{self.__num}'
        else:
            return f'{self.__num}/{self.__den}'

    def get_num(self):
        return self.__num

    def get_den(self):
        return self.__den


class Polynomial:
    # ЭТТЕНШН крч
    # Список коэффициентов пусть будет списком из объектов класса Rnumber
    def __init__(self, coefficients:list):
        self.__coefs = coefficients[::-1]
        # Макс степень
        self.__exp = len(self.__coefs)

    # ЧТОБЫ ВЫВОДИЛОСЬ НОРМАЛЬНО ПРИНТОМ
    def __str__(self):
        return ' '.join([f'({r.__str__()})'+f'x^{len(self.__coefs)-1-i}' for i, r in enumerate(self.__coefs) if r.get_num() != 0])

    def get_coefs(self):
        return self.__coefs.copy()

    def get_exp(self):
        return self.__exp


class NNumber:
    # Классическая инициализация
    def __init__(self,numbers:list):
        # value - значение, то бишь массив цифр
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
