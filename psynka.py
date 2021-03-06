from Dtypes import Integer, NNumber, Polynomial, RNumber
from Integers import ABS_Z_N
from Naturals import DIV_NN_N, MOD_NN_N, MUL_Nk_N
from Naturals_test import Ntest
from SASHAP import MUL_ZZ_Z, MUL_NN_N, ADD_NN_N
from NIKITAT import COM_NN_D, DIV_ZZ_Z
from MAXZ import NZER_N_B
from Rationals_test import *
import unittest

def TRANS_Z_N(num: Integer):
    num = num.get_num()
    num.reverse()
    return NNumber(num)

def LED_P_Q(mchlen: Polynomial):
    return mchlen.get_coefs()[0]

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

# нод
def GCF_NN_N(num1: NNumber,num2: NNumber):
    while True:
        # в бесконечном цикле делим числа друг на друга и записываем остаток от деления в меньшее из них. выполняется пока одно из чисел не станет нулем
        if not int(num1.__str__()) or not int(num2.__str__()):
            return ADD_NN_N(num1, num2)
        if COM_NN_D(num1 ,num2) == 2:
            num1 = MOD_NN_N(num1, num2)
        else:
            num2 = MOD_NN_N(num2, num1)
        # возвращаем суммы чисел, чтобы не сравнивать их
        if not int(num1.__str__()) or not int(num2.__str__()):
            return ADD_NN_N(num1, num2)


# сокращение дробей
def RED_Q_Q(drob: RNumber):
    #сохраняем числитель
    num = drob.get_num()
    # сохраняем знак
    sign = num.get_sign()
    # сохраняем знаменатель
    den = drob.get_den()
    # находим нод
    gcd = GCF_NN_N(den,ABS_Z_N(num))
    # делим числитель и знаменатель на нод
    num = DIV_NN_N(num,gcd)
    den = DIV_NN_N(den, gcd)
    # возвращаем результат
    return RNumber(Integer(num.get_num()[::-1],sign), NNumber(den.get_num()[::-1]))

#n1 = RNumber('-987654321234567890','228')
#n2 = RNumber('0','30')
#print(RED_Q_Q(n1))
#num = NNumber([1,2])
#a = NNumber('0')
#b = NNumber('0')
#print(GCF_NN_N(a, b))

#a = TestRationals()
#print(a.test_RED_Q_Q())

#Rtest(['RED_Q_Q'])
#num1 = NNumber('4331817108397227')
#num2 = NNumber('228')
#print(MUL_NN_N( num1, num2))
#Ntest(['MUL_NN_N'])

#if __name__ == '__main__':
    #unittest.main()
#print(MUL_Nk_N(num, -2))
#f = RNumber(1,5)
#s = RNumber(2)
#t = RNumber(3)
#mchlen = Polynomial([f,s,t])
#print(LED_P_Q(mchlen))
