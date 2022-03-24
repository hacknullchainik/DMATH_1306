from Dtypes import Integer, NNumber, RNumber, Polynomial

def MUL_ZM_Z(num: Integer):
    #Берём знак числа и меняем его на противоположном
    if num.get_sign():
        result = Integer(num.get_num(), 0)
    else:
        result = Integer(num.get_num(), 1)
    return result


