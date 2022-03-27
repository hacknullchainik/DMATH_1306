from Dtypes import RNumber, NNumber, Integer, Polynomial
from NIKITAT import SUB_NN_N, COM_NN_D
from ALEX import MUL_ND_N


def ADD_1N_N(num: NNumber):
    num = num.get_num()
    int_part = 1
    for ind in range(len(num)):
        num[ind] += int_part
        int_part = num[ind] // 10
        num[ind] %= 10
    if (int_part):
        num.append(int_part)
    num.reverse()
    return NNumber(num)


def SUB_NDN_N(num1: NNumber, digit: int, num2: NNumber):
    num2 = MUL_ND_N(num2, digit)
    if (COM_NN_D(num1, num2) in [2, 0]):
        return SUB_NN_N(num1, num2)
    else:
        print("Negative result")

def ABS_Z_N(num: Integer):
    num = num.get_num()
    num.reverse()
    return NNumber(num)


def TRANS_Z_Q(num: Integer):
    sign = num.get_sign()
    num = list(map(str, num.get_num()))
    num.reverse()
    num = int("".join(num))
    if (sign):
        num = -num
    return RNumber(num, 1)
