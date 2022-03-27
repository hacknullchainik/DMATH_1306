from Dtypes import Integer, NNumber, Polynomial, RNumber

def TRANS_Z_N(num: Integer):
    num = num.get_num()
    num.reverse()
    return NNumber(num)

def LED_P_Q(mchlen: Polynomial):
    return mchlen.get_coefs()[0]

#f = RNumber(1,5)
#s = RNumber(2)
#t = RNumber(3)
#mchlen = Polynomial([f,s,t])
#print(LED_P_Q(mchlen))