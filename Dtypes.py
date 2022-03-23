class Integer:
    # Классическая инициализация
    # sign выбрал за бул, чтобы меньше шансов было упороться
    # Знак рассматриваем как True = '-', False = '+' (1 - есть, 0 - нет)
    # П.с. к инту кастуйте и не ебите себе мозги int(True) == 1
    def __init__(self, number: list, sign:bool):
        # value - значение, то бишь массив цифр
        self.value = number
        # Последний разряд, то бишь если число длины 5, то это 4(т.к. нумерация с нуля)
        self.rank = len(number) - 1
        # Знак
        self.sign = sign



class RNumber:
    # числитель, знаменатель - всё просто
    def __init__(self, numerator:int, denominator:int):
        self.num = numerator
        self.den = denominator
        if self.num < 0 and self.den < 0:
            self.num = abs(self.num)
            self.den = abs(self.den)
        elif self.num < 0 or self.den < 0:
            if self.den < 0:
                self.num = -self.num
                self.den = -self.den


class Polynomial:
    # ЭТТЕНШН крч
    # Список коэффициентов пусть будет списком из объектов класса Rnumber
    def __init__(self, coefficients:list, exponent:int):
        self.coefs = coefficients
        # Макс степень
        self.exp = exponent

class NNubmer:
    # Классическая инициализация
    def __init__(self,number:list):
        # value - значение, то бишь массив цифр
        self.value = number
        # Последний разряд, то бишь если число длины 5, то это 4(т.к. нумерация с нуля)
        self.rank = len(number)-1