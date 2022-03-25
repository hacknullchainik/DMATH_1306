from Dtypes import Integer, NNumber, RNumber, Polynomial

#Проверка на целое, если рациональное
#число является целым,то «да», иначе «нет»
def INT_Q_B(num: RNumber):
    # проверяем равен ли знаменатель 1
    if num.get_den() == 1:
        return True
    else:
        return False