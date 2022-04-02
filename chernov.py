from Dtypes import NNumber, Integer, RNumber, Polynomial
import Naturals, Integers, Rationals, Polynomials


def ADD_1N_N(num: NNumber):
    num = num.get_num()
    int_part = 1
    for ind in range(len(num)):
        num[ind] += int_part
        int_part = num[ind] // 10
        num[ind] %= 10
    if (int_part):
        num.append(int_part)
    num.reverse()
    return NNumber(num)


def SUB_NDN_N(num1: NNumber, digit: int, num2: NNumber):
    num2 = MUL_ND_N(num2, digit)
    if (COM_NN_D(num1, num2) in [2, 0]):
        return SUB_NN_N(num1, num2)
    else:
        print("Negative result")

def ABS_Z_N(num: Integer):
    num = num.get_num()
    num.reverse()
    return NNumber(num)


def TRANS_Z_Q(num: Integer):
    return RNumber(num, 1)


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


def NMR_P_P(pol: Polynomial):
    derivative = DER_P_P(pol)
    gcf = GCF_PP_P(pol, derivative)
    return DIV_PP_P(pol, gcf)
