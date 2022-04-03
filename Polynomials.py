from Dtypes import NNumber, Integer, RNumber, Polynomial
from Naturals import *
from Integers import *
from Rationals import *

# Сложение многочленов
def ADD_PP_P(pol1: Polynomial, pol2: Polynomial):
    coef1 = pol1.get_coefs()
    coef2 = pol2.get_coefs()
    coef1.reverse()
    coef2.reverse()
    coef_sum = [RNumber('0')] * max(len(coef1), len(coef2))
    for i in range(len(coef1)):
        coef_sum[i] = ADD_QQ_Q(coef_sum[i], coef1[i])
    for i in range(len(coef2)):
        coef_sum[i] = ADD_QQ_Q(coef_sum[i], coef2[i])
    return Polynomial(coef_sum)

# Вычитание многочленов
def SUB_PP_P(pol1: Polynomial, pol2: Polynomial):
    flag = 0
    result = []
    coefs_bigger = pol1.get_coefs()
    coefs_lower = pol2.get_coefs()

    if pol1.get_exp() < pol2.get_exp():
        coefs_bigger, coefs_lower = coefs_lower, coefs_bigger
        flag = 1

    while len(coefs_bigger) > len(coefs_lower):
        coefs_lower.append(RNumber("0"))

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
def MUL_Pxk_P(poly_1: Polynomial, poly_2: Polynomial):
    p_1 = ''
    p_2_cof = 0

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
    for i in range(1, len(nums)):
        gcf = GCF_NN_N(lcm, nums[i])
    gcf = TRANS_N_Z(gcf)
    return RNumber(gcf, lcm)

# Умножение многочленов
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

# Целочисленное деление
def DIV_PP_P(n: Polynomial, m: Polynomial):
    # Считаем, что n больше m
    div = n
    while div.get_exp() >= m.get_exp():
        temp = []
        temp.append(DIV_QQ_Q(div.get_coefs()[-1], m.get_coefs()[-1]))
        res.append(DIV_QQ_Q(div.get_coefs()[-1], m.get_coefs()[-1]))
        for i in range(len(get_exp(m))-1, 0, -1):
            temp.append(SUB_QQ_Q(div[i], MUL_QQ_Q(temp[-1], m[i])))
        div = Polynomial(temp)

    return res

# Остаток от деления
# MOD_PP_P

# НОД
def GCF_PP_P(num1:Polynomial,num2:Polynomial):
    res = MOD_PP_P(num1,num2)
    while(DEG_P_N(res)!=0):
        num1 = num2
        num2=res
        res = MOD_PP_P(num1,num2)
    return num2

# Производная
def DER_P_P(pol: Polynomial):
    pol2 = []
    if pol.get_exp()!=0:
        for i in range(1,len(pol.get_coefs())):
            j = i
            j = RNumber(Integer([i],False), NNumber([1]))
            pol2.append(MUL_QQ_Q(pol.get_coefs()[i], j))
        return Polynomial(pol2[::-1])
    else:
        return Polynomial('0')

# Кратные корни в простые
def NMR_P_P(pol: Polynomial):
    derivative = DER_P_P(pol)
    gcf = GCF_PP_P(pol, derivative)
    return DIV_PP_P(pol, gcf)

