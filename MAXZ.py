from Dtypes import Integer, NNumber, RNumber, Polynomial
from SASHAP import MUL_ZZ_Z, TRANS_Q_Z

#Проверка на целое, если рациональное
#число является целым,то «да», иначе «нет»
def INT_Q_B(num: RNumber):
    # проверяем равен ли знаменатель 1
    if num.get_den() == 1:
        return True
    else:
        return False

#НОК натуральных чисел
def LCM_NN_N(num1: NNumber, num2: NNumber):
    #найдем произведение двух чисел:
    mult = MUL_NN_N(num1, num2)
    #найдем НОД двух чисел и НОК разделим на НОД
    #НОК(a,b)=a*b/НОД(a,b)
    return (mult // GCF_NN_N(num1, num2))


#Деление дробей (делитель отличен от нуля)
def DIV_QQ_Q(n1: RNumber, n2: RNumber):
    num1 = TRANS_Q_Z(RNumber(n1.get_num(), 1))
    num2 = TRANS_Q_Z(RNumber(n2.get_num(), 1))
    den1 = TRANS_Q_Z(RNumber(n1.get_den(), 1))
    den2 = TRANS_Q_Z(RNumber(n2.get_den(), 1))
    result_num = MUL_ZZ_Z(num1, den2)
    result_den = MUL_ZZ_Z(den1, num2)

    return RNumber(int(result_num.get_num()[0]), int(result_den.get_num()[0]))

print(DIV_QQ_Q(RNumber(1,2), RNumber(2,3)))