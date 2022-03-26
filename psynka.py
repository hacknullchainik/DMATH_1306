from Dtypes import Integer, NNumber

def TRANS_Z_N(num: Integer):
    num = num.get_num()
    num.reverse()
    return NNumber(num)
