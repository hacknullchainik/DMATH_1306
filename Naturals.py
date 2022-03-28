from Dtypes import NNumber

# Сравнение чисел
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

# Проверка на нуль
# NZER_N_B

# Прибавление 1 к числу
def ADD_1N_N(num: NNumber):
    num = num.get_num()
    int_part = 1
    for ind in range(len(num)):
        num[ind] += int_part
        int_part = num[ind] // 10
        num[ind] %= 10
    if int_part:
        num.append(int_part)
    num.reverse()
    return NNumber(num)

# Сумма двух чисел
def ADD_NN_N(number1: NNumber, number2: NNumber):
    # Создаем дубликаты наших цифровых массивов (по факту - чисел) для более удобной работы
    bigger_num = number1.get_num()
    lower_num = number2.get_num()
    result = []

    # Если числа были введены не так, что сначала большее, меняем их местами, дабы избежать возможных ошибок

    if COM_NN_D(number1, number2) == 1:
        bigger_num, lower_num = lower_num, bigger_num

    # Сначала просто складываем поразрядно все числа, на сколько хватит разрядов в меньшем числе
    # и заносим в результирующий массив
    for i in range(len(lower_num)):
        result.append(bigger_num[i] + lower_num[i])

    # Добавляем числа, которые в большем числе были в больших разрядах, чем в меньшем
    for j in range(i + 1, len(bigger_num)):
        result.append(bigger_num[j])

    # Переносим в следующие разряды десятки, которые могли получиться в результате сложения
    # При необходимости,, добавляем еще один разряд в конце
    for i in range(len(result)):
        if result[i] > 9:
            result[i] -= 10
            if i == len(result)-1:
                result.append(1)
            else:
                result[i + 1] += 1
    # Переворачиваем массив, так как работали с обратным порядком цифр
    result.reverse()

    return NNumber(result)

# Разность двух чисел
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

# Произведение числа на цифру
def MUL_ND_N(num: object, num_2: int):
    # local variables storing the value from arugments
    # avoiding changes to the original data
    list_num = num.get_num()
    length = num.get_rank()

    # 'results' will store the end result provided by the current function
    # 'keeper' is used to store the first digit if during the multiplication of two digits the product is a two digit number.
    results = []
    keeper = 0

    for i in range(length + 1):
        # 'value' stores the result of multiplication between 1 digit contained in the list and the chosen digit by the user.
        value = list_num[i] * num_2
        # When value is greater or equal to 10 it means that it contains a two digit number.
        if value < 10:
            if keeper == 0:
                results.insert(0, value)
            else:
                # the first digit of the resulting number of the multilpication is stored inside keeper
                # the value of keeper is then added to the result of the next multiplication
                value = value + keeper
                results.insert(0, value)
                keeper = 0
        elif keeper != 0:
            # in case the next resulting number of the multiplication also exceeds or is equal to 10
            results.insert(0, (value + keeper) % 10)
            keeper = value // 10
            if i == length:
                results.insert(0, keeper)
        else:
            # the second digit of the resulting number of the multiplication is stored inside of the list results
            keeper = value // 10
            results.insert(0, value % 10)

    new_obj = NNumber(results)

    return new_obj

# Произведение числа на 10 в степени к
# MUL_Nk_N

# Произведение двух чисел
# MUL_NN_N

# Разность числа и числа, умноженного на цифру
def SUB_NDN_N(num1: NNumber, digit: int, num2: NNumber):
    num2 = MUL_ND_N(num2, digit)
    if (COM_NN_D(num1, num2) in [2, 0]):
        return SUB_NN_N(num1, num2)
    else:
        print("Negative result")

# Первая цифра неполного частного, умноженная на 10 в степени к, где к - порядок цифры
def DIV_NN_Dk(num1: NNumber, num2: NNumber):
    # Этот алгоритм полностью повторяет деление в столбик, если с комментариями будет
    # что-то непонятно, распишите деление 2-х рандомных чисел и смотря на вашу запись и алгоритм, все поймете

    # Заносим значения чисел в числовой массив
    curr_num = 0
    count = 0
    template_value = []
    lower_num = num1.get_num()
    bigger_num = num2.get_num()

    lower_num.reverse()
    bigger_num.reverse()

    # Проверяем, действительно ли в переменной, обозначающей большее число
    # находится большее исло, при необзодимости меняем местами

    if COM_NN_D(num1, num2) == 2:
        lower_num, bigger_num = bigger_num, lower_num

    # Берем из большего числа столько цифр, сколько их в меньшем и заносим
    # в массив с временным значением

    for i in range(len(lower_num)):
        template_value.append(bigger_num[i])
        curr_num = i

    # Если так получилось, что число, получившееся на предыдущем шаге меньше
    # числа, на которое делим, берем ещё одну цифру

    if COM_NN_D(NNumber(lower_num), NNumber(template_value)) == 2:
        template_value.append(bigger_num[curr_num + 1])

    # k - переменная, обозначающая степень десятки и она разности длин
    # начального большего числа и получившегося из последних шагов

    k = len(bigger_num) - len(template_value)

    # Пока получившееся число больше меньшего числа, отнимаем от него меньшее
    # при этом на каждом шаге прибаляем к переменной count 1, эта переменная показывает
    # на сколько мы "умножили" меьншее число

    while COM_NN_D(NNumber(template_value), NNumber(lower_num)) == 2:
        sub = SUB_NN_N(NNumber(template_value), NNumber(lower_num))
        template_value = sub.get_num()
        template_value.reverse()
        count += 1

    count = count * pow(10, k)

    return count

# Целая часть деления двух чисел
# DIV_NN_N

# Остаток от деления двух чисел
# MOD_NN_N

# НОД чисел
# GCF_NN_N

# НОК чисел
def LCM_NN_N(num1: NNumber, num2: NNumber):
    #найдем произведение двух чисел:
    mult = MUL_NN_N(num1, num2)
    #найдем НОД двух чисел и НОК разделим на НОД
    #НОК(a,b)=a*b/НОД(a,b)
    return DIV_NN_N(mult, GCF_NN_N(num1, num2))
