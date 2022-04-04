from ALEX import TRANS_N_Z
from Dtypes import Integer, NNumber, RNumber, Polynomial
from Naturals import*
from Rationals import*
from Integers import*
from Polynomials import*


# Проверка числа на ноль


def NZER_N_B(n: NNumber):
    # Число - 0, если все его цифры нули
    for i in range(len(n.get_num())):
        if n.get_num()[i] != 0:
            return True
    else:
        return False


# Проверка на целое, если рациональное
# число является целым,то «да», иначе «нет»
def INT_Q_B(num: RNumber):
    if num.get_num().get_num()[0] == 0:
        return True
    else:
        # сокращаем дробь
        num2 = RED_Q_Q(num)
        # првоеряем является ли знаменатель 1 в сокращенной дроби
        if (num2.get_den().get_num()[0] == 1):
            return True
        else:
            return False


# НОК натуральных чисел
def LCM_NN_N(num1: NNumber, num2: NNumber):
    # найдем произведение двух чисел:
    mult = MUL_NN_N(num1, num2)
    # найдем НОД двух чисел и произведение разделим на НОД
    # НОК(a,b)=a*b/НОД(a,b)
    if (mult.get_num() != 0):
        return DIV_NN_N(mult, GCF_NN_N(num1, num2))
    else:
        return NNumber('0')


# Деление дробей (делитель отличен от нуля)
def DIV_QQ_Q(n1: RNumber, n2: RNumber):
    # берутся отдельно числители(num1, num2, с учетом их знака) и знаменатели(den1, den2)

    if n1.get_sign() == False:
        num1 = Integer([int(i) for i in str(n1.get_num().get_num()[::-1]) if '0' <= i <= '9'], False)
    else:
        num1 = Integer([int(i) for i in str(n1.get_num().get_num()[::-1]) if '0' <= i <= '9'], True)

    if n2.get_sign() == False:
        num2 = Integer([int(i) for i in str(n2.get_num().get_num()[::-1]) if '0' <= i <= '9'], False)
    else:
        num2 = Integer([int(i) for i in str(n2.get_num().get_num()[::-1]) if '0' <= i <= '9'], True)

    den1 = NNumber([int(i) for i in str(n1.get_den().get_num()[::-1]) if '0' <= i <= '9'])
    den2 = NNumber([int(i) for i in str(n2.get_den().get_num()[::-1]) if '0' <= i <= '9'])

    # первый числитель умножается на второй,
    # а первый знаменатель умножается на второй
    # результирующий числитель и знаменатель записываются в result_num и result_den, соответственно.




    # если знаки результирующего числителя и знаменателя одинаковы - результат положителен,
    # иначе - отрицателен
    if (num1.get_sign() == False and num2.get_sign() == False) or (num1.get_sign() == True and num2.get_sign() == True):
        den2 = Integer(den2.get_num()[::-1], False)
        num2 = NNumber(num2.get_num()[::-1])
        result_num = MUL_ZZ_Z(num1, den2)
        result_den = MUL_NN_N(den1, num2)
        result_num = result_num.get_num()[::-1]
        result_den = result_den.get_num()[::-1]
        return RED_Q_Q(RNumber(Integer(result_num ,False), NNumber(result_den)))
    else:
        den2 = Integer(den2.get_num()[::-1], False)
        num2 = NNumber(num2.get_num()[::-1])
        result_num = MUL_ZZ_Z(num1, den2)
        result_den = MUL_NN_N(den1, num2)
        result_num = result_num.get_num()[::-1]
        result_den = result_den.get_num()[::-1]
        return RED_Q_Q(RNumber(Integer(result_num,True), NNumber(result_den)))


# степень многочлена
def DEG_P_N(pol: Polynomial):
    return pol.get_exp()

# производная многочлена
def DER_P_P(pol: Polynomial):
    pol2 = []
    #если многочлен ненулевой степени, то перемножаем
    #коэффициенты с каждой степенью, иначе выводим нуль
    if pol.get_exp()!=0:
        for i in range(1,len(pol.get_coefs())):
            j = i
            j = RNumber(Integer([i],False), NNumber([1]))
            pol2.append(MUL_QQ_Q(pol.get_coefs()[i], j))
        return Polynomial(pol2[::-1])
    else:
        return Polynomial('0')

#n1 = RNumber('-100','40')
#n2 = RNumber('-2','30')
#print(DIV_QQ_Q(n1,n2))

#сложение целых чисел
def ADD_ZZ_Z(num1:Integer, num2:Integer):
    #если знаки чисел равны, то результат складывается
    if num1.get_sign() == num2.get_sign():
        res = ADD_NN_N(ABS_Z_N(num1),ABS_Z_N(num2)).get_num()
        res.reverse()
        res = Integer(res,num1.get_sign())
    #если разные знаки, то будет происходить вычетание со сравнением чисел
    else:
        if (num1.get_sign() == True) and (num2.get_sign() == False) and (COM_NN_D(ABS_Z_N(num1), ABS_Z_N(num2)) == 1):
            res = SUB_NN_N(ABS_Z_N(num2),ABS_Z_N(num1)).get_num()
            res.reverse()
            res = Integer(res, False)
        elif (num1.get_sign() == True) and (num2.get_sign() == False) and (COM_NN_D(ABS_Z_N(num1), ABS_Z_N(num2)) == 2):
            res = SUB_NN_N(ABS_Z_N(num1), ABS_Z_N(num2)).get_num()
            res.reverse()
            res = Integer(res, True)
        elif (num1.get_sign() == False) and (num2.get_sign() == True) and (COM_NN_D(ABS_Z_N(num1), ABS_Z_N(num2)) == 2):
            res = SUB_NN_N(ABS_Z_N(num1), ABS_Z_N(num2)).get_num()
            res.reverse()
            res = Integer(res, False)
        else:
            res = SUB_NN_N(ABS_Z_N(num2), ABS_Z_N(num1)).get_num()
            res.reverse()
            res = Integer(res, True)
    return res

#print(DIV_NN_N(NNumber('1123125'), NNumber('15165')))

from Naturals_test import Ntest,Nlist
from Integers_test import Itest,Ilist
from Rationals_test import Rtest,Rlist
from Polynomials_test import Ptest,Plist


#print(GCF_NN_N(NNumber('1122211111111'), NNumber('100000000000000000000000000000000000')))
#print(MUL_NN_N(NNumber('136666666666666666666653'), NNumber('123')))

#Rtest(["DIV_QQ_Q"])

