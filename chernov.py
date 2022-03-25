from Dtypes import RNumber, NNumber, Integer, Polynomial

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


def ABS_Z_N(num: Integer):
    num = num.get_num()
    num.reverse()
    return NNumber(num)


def TRANS_Z_Q(num: Integer):
    sign = num.get_sign()
    num = list(map(str, num.get_num()))
    num.reverse()
    num = int("".join(num))
    print(num, 1, sign)
    #return RNumber()

