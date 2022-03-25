from Dtypes import Integer, NNumber, RNumber, Polynomial

def INT_Q_B(num: RNumber):
    # проверяем равен ли знаменатель 1
    if num.get_den() == 1:
        return True
    else:
        return False