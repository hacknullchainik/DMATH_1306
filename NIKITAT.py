from Dtypes import Integer, NNumber, RNumber, Polynomial
import Naturals, Integers

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
    if Naturals.COM_NN_D(n, m)==2:
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
    elif Naturals.COM_NN_D(n, m) == 1:
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


def DIV_ZZ_Z(n: Integer, m: Integer):
    res = []
    # Проверяем числа на знаки (узнаём, в результате будет положительное число или отрицательное)
    if (Integers.POZ_Z_D(n) + Integers.POZ_Z_D(m)) == 4:
        sign = False
    elif (Integers.POZ_Z_D(n) + Integers.POZ_Z_D(m)) == 3:
        sign = True
    else:
        sign = False

    # Берём абсолютные значения (знак уже запомнили) и применяем обычное деление натуральных чисел
    # В результате всё равно целое
    n = Integers.ABS_Z_N(n)
    m = Integers.ABS_Z_N(m)
    res = Naturals.DIV_NN_N(n, m).get_num()

    return Integer(res, sign)

def MUL_PQ_Q(n: Polynomial, m: RNumber):
    res = []
    # Берём массив коэффициентов
    work = n.get_coefs()
    # И каждый коэффициент умножаем на число m
    for i in range(len(work)):
        res.append(MUL_QQ_Q(work[i], m))
    return Polynomial(res)

def DIV_PP_P(n: Polynomial, m: Polynomial):
    # Считаем, что n больше m
    div = n
    while get_exp(div) >= get_exp(m):
        temp = []
        temp.append(DIV_QQ_Q(div.get_coefs()[-1], m.get_coefs()[-1]))
        res.append(DIV_QQ_Q(div.get_coefs()[-1], m.get_coefs()[-1]))
        for i in range(len(get_exp(m))-1, 0, -1):
            temp.append(SUB_QQ_Q(div[i], MUL_QQ_Q(temp[-1], m[i])))
        div = Polynomial(temp)

    return res