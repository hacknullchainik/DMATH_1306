from Dtypes import Integer, NNumber, RNumber, Polynomial

def MUL_ZM_Z(num: Integer):
    if num.get_sign():
        result = Integer(num.get_num(), False)
    else:
        result = Integer(num.get_num(), True)
    return result



def COM_NN_D(num1: NNumber, num2: NNumber):
    # Берём числа в нормальном порядке
    num1 = num1.get_num()
    num2 = num2.get_num()
    num2.reverse()
    num1.reverse()
    # Сравниваем по цифрам, если длины чисел равны
    if len(num1) == len(num2):
        for i in range(len(num1)):
            if num1[i] > num2[i]:
                return 2
            if num2[i] > num1[i]:
                return 1
        return 0
    elif len(num1) > len(num2):
        return 2
    else:
        return 1

def SUB_NN_N(n: NNumber, m: NNumber):
    # Результирующий массив
    res = []
    # Если n больше
    if COM_NN_D(n, m)==2:
        n = n.get_num()
        m = m.get_num()
        # Заполняем "пустые" (недостающие) разряды нулями (чтобы длины чисел совпадали)
        while len(m) < len(n):
            m.append(0)
        while len(n) < len(m):
            n.append(0)

        # Поциферно вычитаем, занимая единицу, где это нужно
        for i in range(len(m)):
            if n[i]-m[i] < 0:
                res.append(10+n[i]-m[i])
                n[i+1] -= 1
            else:
                res.append(n[i]-m[i])

    # Аналогично, если m больше
    elif COM_NN_D(n, m) == 1:
        n = n.get_num()
        m = m.get_num()
        while len(m) < len(n):
            m.append(0)
        while len(n) < len(m):
            n.append(0)

        for i in range(len(n)):
            if m[i] - n[i] < 0:
                res.append(10 + m[i] - n[i])
                m[i + 1] -= 1
            else:
                res.append(m[i] - n[i])
    else:
        res.append(0)

    # Чистим от лишних нулей
    while res[-1]==0 and len(res)>1:
        res.pop()
    result = NNumber(res[::-1])
    return result

def DIV_NN_N(n: NNumber, m: NNumber):
    res = []
    if COM_NN_D(n, m) == 2:
        n = n.get_num()[::-1]
        m = m.get_num()[::-1]
        div = n
        while COM_NN_D(div, m)==2:
            res.append(DIV_NN_Dk(div, m))
            div = SUB_NDN_N(div, m, DIV_NN_Dk(div, m))
    elif COM_NN_D(n, m) == 1:
        n = n.get_num()[::-1]
        m = m.get_num()[::-1]
        div = m
        while COM_NN_D(div, n) == 2:
            res.append(DIV_NN_Dk(div, n))
            div = SUB_NDN_N(div, n, DIV_NN_Dk(div, n))
    else:
        res.append(1)
    return NNumber(res)