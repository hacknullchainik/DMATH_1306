from Dtypes import NNumber, Integer, RNumber, Polynomial
from Naturals import *
from Integers import *
from Rationals import *


# Сложение многочленов
def ADD_PP_P(pol1: Polynomial, pol2: Polynomial):
    coef1 = pol1.get_coefs()
    coef2 = pol2.get_coefs()

    # Создаем нулевой массив коэф., двина которого равена наибольшему кол-ву коэф. между многочленами
    coef_sum = [RNumber('0')] * max(len(coef1), len(coef2))
    # Прибавляем все коэф. первого многочлена
    for i in range(len(coef1)):
        coef_sum[i] = ADD_QQ_Q(coef_sum[i], coef1[i])
    # Прибавляем все коэф. второго многочлена
    for i in range(len(coef2)):
        coef_sum[i] = ADD_QQ_Q(coef_sum[i], coef2[i])
    # Возвращаем результат
    coef_sum.reverse()
    return Polynomial(coef_sum)


# Вычитание многочленов
def SUB_PP_P(pol1: Polynomial, pol2: Polynomial):
    flag = 0  # Переменная, показывающая, менялись ли значения местами
    result = []
    coefs_bigger = pol1.get_coefs()
    coefs_lower = pol2.get_coefs()

    # Меняем местами массивы коэффициентов, если степень первого больше степени второго
    if pol1.get_exp() < pol2.get_exp():
        coefs_bigger, coefs_lower = coefs_lower, coefs_bigger
        flag = 1

    # Добавляем незначащие нули в массиве коэффициентов многочлена с меньшей степенью, пока длины массивов
    # не будут одинаковыми
    while len(coefs_bigger) > len(coefs_lower):
        coefs_lower.append(RNumber("0"))

    # Вычитаем соответствующие коэффициенты
    for i in range(len(coefs_bigger)):
        if flag:
            result.append(SUB_QQ_Q(coefs_lower[i], coefs_bigger[i]))
        else:
            result.append(SUB_QQ_Q(coefs_bigger[i], coefs_lower[i]))

    result.reverse()

    return Polynomial(result)


# Умножение многочлена на рациональное число
def MUL_PQ_Q(n: Polynomial, m: RNumber):
    res = []
    # Берём массив коэффициентов
    work = n.get_coefs()
    # И каждый коэффициент умножаем на число m
    for i in range(len(work)):
        res.append(MUL_QQ_Q(work[i], m))
    return Polynomial(res[::-1])


# Умножение многочлена на х**к
def MUL_Pxk_P(poly_1: Polynomial, poly_2: int):
    p_1 = ''
    p_2_cof = 0
    poly_2 = Polynomial('1' + ' 0' * poly_2)
    # This loop looks for the coefficient of the x^k that will be multiplied to poly_1.
    for i in poly_2.get_coefs():
        if i.get_num() != 0:
            p_2_cof = i

    # Multiplying each coefficient to one another.
    for i in poly_1.get_coefs()[::-1]:
        p_1 += str(MUL_QQ_Q(i, p_2_cof))
        p_1 += ' '
    p_1 = p_1[:-1]

    # Increasing the value of the exponents of our polynomial by k.
    for i in range(poly_2.get_exp()):
        p_1 += ' 0'

    return Polynomial(p_1)


# Старший коэффициент многочлена
def LED_P_Q(mchlen: Polynomial):
    return mchlen.get_coefs()[-1]


# Степень многочлена
def DEG_P_N(pol: Polynomial):
    return pol.get_exp()


# Вынесение НОК/НОД
def FAC_P_Q(pol: Polynomial):
    coef = pol.get_coefs()
    nums = [ABS_Z_N(i.get_num()) for i in coef]
    dens = [i.get_den() for i in coef]
    lcm = dens[0]
    for i in range(1, len(dens)):
        lcm = LCM_NN_N(lcm, dens[i])
    gcf = nums[0]
    for i in nums:
        gcf = GCF_NN_N(gcf, i)
    gcf = TRANS_N_Z(gcf)
    return RNumber(gcf, lcm)


# Умножение многочленов
def MUL_PP_P(num1: Polynomial, num2: Polynomial):
    ar1 = num1.get_coefs()
    ar1.reverse()
    for i in range(len(ar1)):
        # перемножаем каждый из членов многочлена на 2й многочлен, попутно уменьшая степень
        # (т.к идём от большей степени)
        re = MUL_Pxk_P(MUL_PQ_Q(num2, ar1[i]), len(ar1) - (i + 1))
        if (i == 0):
            res = re
        else:
            # складываем все полученные от перемноожения многочлены
            res = ADD_PP_P(res, re)
    return res


# Целочисленное деление
def DIV_PP_P(n: Polynomial, m: Polynomial):
    # Записываем многочлен-делимое в отдельную переменную для удобства
    temp = n
    # Создаем массив с конечными коэффициентами
    res = []
    # проверяем, не яввляется ли многочлен-делитель нулём
    if not POZ_Z_D((m.get_coefs()[-1]).get_num()):
        raise ZeroDivisionError

    if m.get_exp() > n.get_exp():
        return Polynomial('0')
    # Проверка на то, является ли m числом?
    if m.get_exp() == 0:
        for i in temp.get_coefs()[::-1]:
            res.append(DIV_QQ_Q(i, m.get_coefs()[0]))
    else:
        # Делим пока степень делителя не больше делимого
        while (temp.get_exp() >= m.get_exp()):
            # Записываем коэффициент деления в массив
            res.append(DIV_QQ_Q(LED_P_Q(temp), LED_P_Q(m)))
            # Вычетаем из делимого делитель, умноженный на коэффициент деления, со сдвигом влево
            temp = SUB_PP_P(temp, MUL_Pxk_P(MUL_PQ_Q(m, res[-1]), temp.get_exp() - m.get_exp()))

        # Многочлен, полученный в результате деления будет степени, равной разности степеней делимого и делителя
        # поэтому если мы получили меньше, докидываем на младшие степени нули
        while len(res) <= (n.get_exp() - m.get_exp()):
            res.append(RNumber('0'))
    return Polynomial(res)


# Остаток от деления
def MOD_PP_P(poly_1: Polynomial, poly_2: Polynomial):
    # divid will is the  dividend
    # divis will is the divisor
    divid = poly_1
    divis = poly_2

    # quotient of the division is stored inside of quo
    quo = DIV_PP_P(divid, divis)

    # the result of the multiplication between the divis and the quotien is stored in q_divis.
    q_divis = MUL_PP_P(divis, quo)

    # Once q_divis has been found it is substructed from divid(the dividend).
    res = SUB_PP_P(divid, q_divis)

    # ---THIS CONDITION SEEMS TO BE USELESS BUT I WON'T DELETE IT JUST IN CASE---

    # if the remainder can still be divided by the divisor resent to the function.
    # if the remainder can't be divided anyfurther the function returns the result.
    # if res.get_exp() >= divis.get_exp():
    #     MOD_PP_P(res, divis)

    return res


# НОД
def GCF_PP_P(num1: Polynomial, num2: Polynomial):
    # Записываем многочлены в отдельные переменные для удобства и создаем многочлен, являющийся нулем
    pol1 = num1
    pol2 = num2
    zero = Polynomial('0')
    # Пока обы многочлена больше нуля делим с остатком больший многочлен на меньший и результат записываем в больший
    while COM_PP_D(pol1, zero) and COM_PP_D(pol2, zero):
        if COM_PP_D(pol1, pol2):
            pol1 = MOD_PP_P(pol1, pol2)
        else:
            pol2 = MOD_PP_P(pol2, pol1)
    # Возвращаем сумму полученных остатков
    # Фактически, алгоритм повторяет тот, что используется для целых чисел
    return ADD_PP_P(pol1, pol2)


# Сравнение многочленов
# Это функция служенбная, у нас в списке ее не было, не обращайте на нее внимания
# Для справки, многочлен A будем называть большим многочлена B, если:
# 1) Его степень больше
# 2) Перввый несовпадающий коэффициент, считая от старшей степени, больше
# Например:
# 3х^4+5x^3+2 > 7x^3+ x - по первому признаку
# 5x^3 - 4x^2 - 6x +9 > 3x^3 + 27x^2 + 1247 - по второму признаку
# 3x^4 + 7x^2 - 9x + 4 > 3x^4 + 7x^2 - 9x + 2 - по второму признаку
# Ну многочлены равны, если они одинаковые, тут все просто
def COM_PP_D(pol1: Polynomial, pol2: Polynomial):
    if pol1.get_exp() > pol2.get_exp():
        return True
    elif pol1.get_exp() < pol2.get_exp():
        return False
    else:
        for i in range(pol1.get_exp(), -1, -1):
            if POZ_Z_D(SUB_QQ_Q(pol1.get_coefs()[-1], pol2.get_coefs()[-1]).get_num()) == 2:
                return True
            else:
                return False
        return 3


# Кратные корни в простые
def NMR_P_P(pol: Polynomial):
    result = []

    # Производная многочлена
    derivative = DER_P_P(pol)
    # НОД многочлена и его производной
    gcf = GCF_PP_P(pol, derivative)
    fac = FAC_P_Q(gcf)

    # Делим многочлен на значеие НОД и возвращаем результат
    temp_res = DIV_PP_P(pol, gcf)
    temp_res = MUL_PQ_Q(temp_res, fac)

    # Сокращаем дроби
    for i in range(len(temp_res.get_coefs())):
        result.append(RED_Q_Q(temp_res.get_coefs()[i]))
    result.reverse()
    return Polynomial(result)


# Производная
def DER_P_P(pol: Polynomial):
    pol2 = []
    # если многочлен ненулевой степени, то перемножаем
    # коэффициенты с каждой степенью, иначе выводим нуль
    if pol.get_exp() != 0:
        for i in range(1, len(pol.get_coefs())):
            j = i
            j = RNumber(Integer([i], False), NNumber([1]))
            pol2.append(MUL_QQ_Q(pol.get_coefs()[i], j))
        return Polynomial(pol2[::-1])
    else:
        return Polynomial('0')
