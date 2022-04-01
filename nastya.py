from Dtypes import *
from Polynomials import *


def SUB_ZZ_Z(num1:Integer, num2:Integer):
    # - + = - - (сложение)
    # + - = + + (сложение)
    # - - = - + (не сложение)
    # + + = + -  (не сложение)
    if num1.get_sign() != num2.get_sign():
        res = ADD_NN_N(ABS_Z_N(num1),ABS_Z_N(num2)).get_num()
        res.reverse()
        res = Integer(res,num1.get_sign())
    else:
        if COM_NN_D(num1,num2)  == 2:
            sig = num1.get_sign()
        else:
            if num2.get_sign():
                sig = 0
            else:
                sig = 1
        res = SUB_NN_N(ABS_Z_N(num1),ABS_Z_N(num2)).get_num()
        res.reverse()
        res = Integer(res,sig)
    return res

def GCF_PP_P(num1:Polynomial,num2:Polynomial):
    res = MOD_PP_P(num1,num2)
    while(DEG_P_N(res)!=0):
        num1 = num2
        num2=res
        res = MOD_PP_P(num1,num2)
    return num2