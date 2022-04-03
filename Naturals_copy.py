from Dtypes import NNumber, Integer, RNumber, Polynomial
from Integers import *
from Naturals import *
from Rationals import *
from Naturals_test import Ntest


def INT_Q_B(num: RNumber):
    # сокращаем дробь
    num2 = RED_Q_Q(num)

    # првоеряем является ли знаменатель 1 в сокращенной дроби
    if (num2.get_den() == 1) or (num2.get_num() == 0):
        return True
    else:
        return False

Ntest(['INT_Q_B'])