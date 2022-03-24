from Dtypes import RNumber, NNumber, Integer, Polynomial


def POZ_Z_D(num: Integer):
    if num.get_num()[0] == 0:
        return 0

    elif num.get_sign():
        return 1

    else:
        return 2

def TRANS_Z_Q(num:RNumber):
    if num.get_den() == 1:


print(POZ_Z_D(Integer([1,2,3], True)))

print(POZ_Z_D(Integer([1,2,3], False)))
print(POZ_Z_D(Integer([0], False)))