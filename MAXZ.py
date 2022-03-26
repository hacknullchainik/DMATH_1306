from Dtypes import Integer, NNumber, RNumber, Polynomial

#Проверка на целое, если рациональное
#число является целым,то «да», иначе «нет»
def INT_Q_B(num: RNumber):
    # проверяем равен ли знаменатель 1
    if num.get_den() == 1:
        return True
    else:
        return False

#НОК натуральных чисел
def LCM_NN_N(num1:NNumber, num2:NNumber):
    #найдем произведение двух чисел:
    mult=MUL_NN_N(num1, num2)
    #найдем НОД двух чисел и НОК разделим на НОД
    #НОК(a,b)=a*b/НОД(a,b)
    result (mult // GCF_NN_N(num1, num2))