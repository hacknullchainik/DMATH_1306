from Dtypes import Integer, NNumber, Polynomial, RNumber
from SASHAP import MUL_ZZ_Z, MUL_NN_N


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

#n1 = RNumber('25','2')
#n2 = RNumber('-2','30')
#print(MUL_QQ_Q(n1,n2))


#f = RNumber(1,5)
#s = RNumber(2)
#t = RNumber(3)
#mchlen = Polynomial([f,s,t])
#print(LED_P_Q(mchlen))