from Dtypes import NNumber, Integer, RNumber, Polynomial
from Integers import *
from Naturals import *
from Rationals import *
# остаток от деления большего на меньшее или равное
# код не будет работать из за ошибки в функции Div_NN_N
# можно писать доп условия с увеличением остатка при ситуации 2,399 до 2,4. . . А оно надо ?
def DIV_NN_N(n: NNumber, m: NNumber):
    # Создаём результирующий массив
    res = 0
    # Сравниваем числа. Если n больше, то делим n на m. Иначе - m на n
    if Naturals.COM_NN_D(n, m) == 2:
        div = n
        res = 0
        # Получаем само число и поциферно вычисляем результат деления
        while Naturals.COM_NN_D(div, m)!=1:
            res += DIV_NN_Dk(div, m)
            # Ниже операция вычитания из делимого части делителя. Нашли первую цифру деления - DIV_NN_Dk(div, m),
            # затем вычли из делимого делитель умноженный на эту цифру. Получили новый делитель. Повторяем,
            # пока делимое больше делителя
            div = Naturals.SUB_NDN_N(div, DIV_NN_Dk(div, m), m)
    elif Naturals.COM_NN_D(n, m) == 1:
        n = n.get_num()[::-1]
        m = m.get_num()[::-1]
        div = m
        while Naturals.COM_NN_D(div, n) != 1:
            res += Naturals.DIV_NN_Dk(div, m)
            div = Naturals.SUB_NDN_N(div, DIV_NN_Dk(div, n), n)
    else:
        res += 1
    return NNumber([i for i in str(res).split()])

def MOD_NN_N(num1: NNumber, num2: NNumber):
    
    x = 0 # < - для увеличение разрядности первого числа, можно увеличить разрядность путём создания вместа x массива 0
    # берём целое от деления
    k = DIV_NN_N(num1,num2)
    k.reverse()
    k.append(x) # увеличиваем разрядность
    num1 = num1.get_num()
    num1.reverse()
    num1.append(x) # увеличиваем разрядность первого чила 
    num1 = NNumber(num1)
    # находим частное от большего первого и оригинального второго - получаем большее по разрядности частное(включающее первую цифру остатка)
    l = DIV_NN_N(num1,num2)
    # к примеру, при 10 и 4: l = 2, k = 25, увеличиваем l до 20, находим k = 25 (100/4), далее k - l = 5/ / / наш остаток
    res = SUB_NDN_N(k,1,l)
    return res

def ADD_QQ_Q(num1:RNumber,num2:RNumber):
    print(num1.get_num(),num2.get_den()) #целое
    print(num2.get_num(),num2.get_den())
    znam1 = num1.get_den()
    znam2 = num2.get_den()
    LCM = LCM_NN_N(znam1,znam2) # находим Нод
    #переход от N в Z для возможности применения ф-ций
    LCM = LCM.get_num()
    LCM.reverse()
    LCM = Integer(LCM)
    znam1 = znam1.get_num()
    znam1.reverse()         # это не говнокод, это из за недостатка функций, вы не понимаете)))))
    znam1 = Integer(znam1)
    znam2 = znam2.get_num()
    znam2.reverse()
    znam2 = Integer(znam2)
    x = Integer('1') # потому что могу )
    y = Integer('1') # потому что умею )
    #увеличиваем x 
    while znam1!=LCM:
        x  = ADD_ZZ_Z(x,Integer('1'))
        MUL_ZZ_Z(znam1,x)
    #увеличиваем y
    while znam2!=LCM:
        y  = ADD_ZZ_Z(y,Integer('1'))
        MUL_ZZ_Z(znam2,y)
    # числитель = числ1 * x + числ2 * y (x и y - множитили от Нод)
    num = ADD_ZZ_Z(MUL_ZZ_Z(num1.get_num(),x),MUL_ZZ_Z(num2.get_num(),y))
    res = RNumber(num,LCM)
    return res

def MUL_PQ_Q(n: Polynomial, m: RNumber):
    res = []
    # Берём массив коэффициентов
    work = n.get_coefs()
    # И каждый коэффициент умножаем на число m
    for i in range(len(work)):
        res.append(MUL_QQ_Q(work[i], m))
    res.reverse()
    return Polynomial(res)

# умножение многочленов
def MUL_PP_P(num1: Polynomial, num2: Polynomial):
    ar1 = num1.get_coefs()
    ar1.reverse()
    for i in range(len(ar1)):
        re = MUL_Pxk_P(MUL_PQ_Q(num2,ar1[i]),len(ar1)-(i+1))
        if (i == 0):
            res = re
        else:
            res = ADD_PP_P(res,re)
    return res
