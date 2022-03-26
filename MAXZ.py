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

    #берутся отдельно числители(num1, num2, с учетом их знака) и знаменатели(den1, den2)
    if n1.get_num()>0:
        num1 = Integer(list(str(n1.get_num())), False)
    else:
        num1 = Integer(list(str(n1.get_num())[1:]), True)

    if n2.get_num()>0:
        num2 = Integer(list(str(n2.get_num())), False)
    else:
        num2 = Integer(list(str(n2.get_num())[1:]), True)

    den1 = Integer(list(str(n1.get_den())), False)
    den2 = Integer(list(str(n2.get_den())), False)

    #первый числитель умножается на второй знаменатель,
    #а первый знаменатель умножается на второй числитель
    # результирующий числитель и знаменатель записываются в result_num и result_den, соответственно.
    result_num = MUL_ZZ_Z(num1, den2)
    result_den = MUL_ZZ_Z(den1, num2)

    #если знаки результирующего числителя и знаменателя одинаковы - результат положителен,
    #иначе - отрицателен
    if result_num.get_sign()==result_den.get_sign():
        return RNumber(int(''.join(map(str, result_num.get_num()[::-1]))),
                       int(''.join(map(str, result_den.get_num()[::-1]))))
    else:
        return RNumber(-int(''.join(map(str, result_num.get_num()[::-1]))),
                       int(''.join(map(str, result_den.get_num()[::-1]))))