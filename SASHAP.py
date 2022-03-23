from Dtypes import RNumber, NNumber, Integer, Polynomial


def POZ_Z_D(num: Integer):
    if num.get_sign():
        return 1
    elif num.get_num()[0] == 0:
        return 0
    else:
        return 2
