from Dtypes import Integer, NNumber, Polynomial, RNumber
from SASHAP import MUL_ZZ_Z


def TRANS_Z_N(num: Integer):
    num = num.get_num()
    num.reverse()
    return NNumber(num)

def LED_P_Q(mchlen: Polynomial):
    return mchlen.get_coefs()[0]

def MUL_QQ_Q(n1: RNumber, n2: RNumber):
    # берутся отдельно числители(num1, num2, с учетом их знака) и знаменатели(den1, den2)
    if n1.get_num() > 0:
        num1 = Integer([int(i) for i in str(n1.get_num()) if '0' <= i <= '9'], False)
    else:
        num1 = Integer([int(i) for i in str(n1.get_num()) if '0' <= i <= '9'], True)

    if n2.get_num() > 0:
        num2 = Integer([int(i) for i in str(n2.get_num()) if '0' <= i <= '9'], False)
    else:
        num2 = Integer([int(i) for i in str(n2.get_num()) if '0' <= i <= '9'], True)

    den1 = Integer([int(i) for i in str(n1.get_den()) if '0' <= i <= '9'], False)
    den2 = Integer([int(i) for i in str(n2.get_den()) if '0' <= i <= '9'], False)

    # первый числитель умножается на второй,
    # а первый знаменатель умножается на второй
    # результирующий числитель и знаменатель записываются в result_num и result_den, соответственно.
    result_num = MUL_ZZ_Z(num1, num2)
    result_den = MUL_ZZ_Z(den1, den2)

    # если знаки результирующего числителя и знаменателя одинаковы - результат положителен,
    # иначе - отрицателен
    if result_num.get_sign() == result_den.get_sign():
        return RNumber(int(''.join(map(str, result_num.get_num()[::-1]))),
                       int(''.join(map(str, result_den.get_num()[::-1]))))
    else:
        return RNumber(-int(''.join(map(str, result_num.get_num()[::-1]))),
                       int(''.join(map(str, result_den.get_num()[::-1]))))

#n1 = RNumber(10,2)
#n2 = RNumber(-2,3)
#print(MUL_QQ_Q(n1,n2))


#f = RNumber(1,5)
#s = RNumber(2)
#t = RNumber(3)
#mchlen = Polynomial([f,s,t])
#print(LED_P_Q(mchlen))