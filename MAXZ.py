from Dtypes import Integer, NNumber, RNumber, Polynomial
from SASHAP import MUL_ZZ_Z, MUL_NN_N

#Проверка на целое, если рациональное
#число является целым,то «да», иначе «нет»
def INT_Q_B(num: RNumber):
    # сокращаем дробь
    num2=RED_Q_Q(num)

    #првоеряем является ли знаменатель 1 в сокращенной дроби
    if (num2.get_den() == 1) or (num2.get_num() == 0):
        return True
    else:
        return False

#НОК натуральных чисел
def LCM_NN_N(num1: NNumber, num2: NNumber):
    #найдем произведение двух чисел:
    mult = MUL_NN_N(num1, num2)
    #найдем НОД двух чисел и произведение разделим на НОД
    #НОК(a,b)=a*b/НОД(a,b)
    return DIV_NN_N(mult, GCF_NN_N(num1, num2))


#Деление дробей (делитель отличен от нуля)
def DIV_QQ_Q(n1: RNumber, n2: RNumber):

    #берутся отдельно числители(num1, num2, с учетом их знака) и знаменатели(den1, den2)
    if n1.get_num()>0:
        num1 = Integer([int(i) for i in str(n1.get_num()) if '0'<=i<='9'], False)
    else:
        num1 = Integer([int(i) for i in str(n1.get_num()) if '0'<=i<='9'], True)

    if n2.get_num()>0:
        num2 = Integer([int(i) for i in str(n2.get_num()) if '0'<=i<='9'], False)
    else:
        num2 = Integer([int(i) for i in str(n2.get_num()) if '0'<=i<='9'], True)

    den1 = Integer([int(i) for i in str(n1.get_den()) if '0'<=i<='9'], False)
    den2 = Integer([int(i) for i in str(n2.get_den()) if '0'<=i<='9'], False)

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