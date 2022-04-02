# остаток от деления большего на меньшее или равное
# код не будет работать из за ошибки в функции Div_NN_N
# можно писать доп условия с увеличением остатка при ситуации 2,399 до 2,4. . . А оно надо ?
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
