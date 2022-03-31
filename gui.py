from tkinter import *
from tkinter import Menu
from Dtypes import NNumber, Integer, RNumber, Polynomial
import Naturals, Integers, Rationals, Polynomials

# NATURAL NUMBERS
# Сумма числа и 1
def ADD_1N_N():
    global frame_output, frame_input
    def RESULT():
        global frame_output
        a_val = NNumber([int(i) for i in a.get()])
        frame_input.destroy()
        frame_output = Frame(window)
        frame_output.grid()
        window.title("Результат прибавления 1 к числу")
        result = Text(frame_output)
        result.grid()
        result.insert(1.0, (str(a_val) + " + 1 = " + str(Naturals.ADD_1N_N(a_val))))
        result.configure(state='disabled')

    try:
        frame_output.destroy()
    except:
        print("none")
    try:
        frame_input.destroy()
    except:
        print("none")
    frame.destroy()
    frame_input = Frame(window)
    frame_input.grid()
    window.title("Прибавление 1 к числу")
    a_lab = Label(frame_input, text="Введите число:").grid(row=1, column=1)
    a = Entry(frame_input, width=16)
    a.grid(row=1, column=2, padx=(4, 0))
    but = Button(frame_input, text="Рассчитать", width=10, command=RESULT).grid(row=2, column=1, padx=(10, 0))

# Разность чисел
def SUB_NN_N():
    global frame_output, frame_input
    def RESULT():
        global frame_output
        a_val = NNumber([int(i) for i in a.get()])
        b_val = NNumber([int(i) for i in b.get()])
        frame_input.destroy()
        frame_output = Frame(window)
        frame_output.grid()
        window.title("Результат разности двух чисел")
        result = Text(frame_output)
        result.grid()
        result.insert(1.0, (str(a_val) + " - " + str(b_val) + " = " + str(Naturals.SUB_NN_N(a_val, b_val))))
        result.configure(state='disabled')

    try:
        frame_output.destroy()
    except:
        print("none")
    try:
        frame_input.destroy()
    except:
        print("none")
    frame.destroy()
    frame_input = Frame(window)
    frame_input.grid()
    window.title("Разность двух чисел")
    a_lab = Label(frame_input, text="Введите первое число").grid(row=1, column=1)
    a = Entry(frame_input, width=16)
    a.grid(row=1, column=2, padx=(4, 0))
    b_lab = Label(frame_input, text="Введите второе число").grid(row=2, column=1)
    b = Entry(frame_input, width=16)
    b.grid(row=2, column=2, padx=(4, 0))
    but = Button(frame_input, text="Рассчитать", width=10, command=RESULT).grid(row=3, column=1, padx=(10, 0))

# Сумма чисел
def ADD_NN_N():
    global frame_output, frame_input
    def RESULT():
        global frame_output
        a_val = NNumber([int(i) for i in a.get()])
        b_val = NNumber([int(i) for i in b.get()])
        frame_input.destroy()
        frame_output = Frame(window)
        frame_output.grid()
        window.title("Результат суммы двух чисел")
        result = Text(frame_output)
        result.grid()
        result.insert(1.0, (str(a_val) + " + " + str(b_val) + " = " + str(Naturals.ADD_NN_N(a_val, b_val))))
        result.configure(state='disabled')

    try:
        frame_output.destroy()
    except:
        print("none")
    try:
        frame_input.destroy()
    except:
        print("none")
    frame.destroy()
    frame_input = Frame(window)
    frame_input.grid()
    window.title("Сумма двух чисел")
    a_lab = Label(frame_input, text="Введите первое число:").grid(row=1, column=1)
    a = Entry(frame_input, width=16)
    a.grid(row=1, column=2, padx=(4, 0))
    b_lab = Label(frame_input, text="Введите второе число:").grid(row=2, column=1)
    b = Entry(frame_input, width=16)
    b.grid(row=2, column=2, padx=(4, 0))
    but = Button(frame_input, text="Рассчитать", width=10, command=RESULT).grid(row=3, column=1, padx=(10, 0))

# Произведение чисел
def MUL_NN_N():
    global frame_output, frame_input
    def RESULT():
        global frame_output
        a_val = NNumber([int(i) for i in a.get()])
        b_val = NNumber([int(i) for i in b.get()])
        frame_input.destroy()
        frame_output = Frame(window)
        frame_output.grid()
        window.title("Результат произведения двух чисел")
        result = Text(frame_output)
        result.grid()
        result.insert(1.0, (str(a_val) + " * " + str(b_val) + " = " + str(Naturals.MUL_NN_N(a_val, b_val))))
        result.configure(state='disabled')

    try:
        frame_output.destroy()
    except:
        print("none")
    try:
        frame_input.destroy()
    except:
        print("none")
    frame.destroy()
    frame_input = Frame(window)
    frame_input.grid()
    window.title("Произведение двух чисел")
    a_lab = Label(frame_input, text="Введите первое число:").grid(row=1, column=1)
    a = Entry(frame_input, width=16)
    a.grid(row=1, column=2, padx=(4, 0))
    b_lab = Label(frame_input, text="Введите второе число:").grid(row=2, column=1)
    b = Entry(frame_input, width=16)
    b.grid(row=2, column=2, padx=(4, 0))
    but = Button(frame_input, text="Рассчитать", width=10, command=RESULT).grid(row=3, column=1, padx=(10, 0))

# Неполное частное
def DIV_NN_N():
    global frame_output, frame_input
    def RESULT():
        global frame_output
        a_val = NNumber([int(i) for i in a.get()])
        b_val = NNumber([int(i) for i in b.get()])
        frame_input.destroy()
        frame_output = Frame(window)
        frame_output.grid()
        window.title("Неполное частное двух чисел")
        result = Text(frame_output)
        result.grid()
        result.insert(1.0, ("{0} div {1} = {2}".format(str(a_val), str(b_val), str(Naturals.DIV_NN_N(a_val, b_val)))))
        result.configure(state='disabled')

    try:
        frame_output.destroy()
    except:
        print("none")
    try:
        frame_input.destroy()
    except:
        print("none")
    frame.destroy()
    frame_input = Frame(window)
    frame_input.grid()
    window.title("Неполное частное двух чисел")
    a_lab = Label(frame_input, text="Введите первое число:").grid(row=1, column=1)
    a = Entry(frame_input, width=16)
    a.grid(row=1, column=2, padx=(4, 0))
    b_lab = Label(frame_input, text="Введите второе число:").grid(row=2, column=1)
    b = Entry(frame_input, width=16)
    b.grid(row=2, column=2, padx=(4, 0))
    but = Button(frame_input, text="Рассчитать", width=10, command=RESULT).grid(row=3, column=1, padx=(10, 0))

# Неполное частное
def MOD_NN_N():
    global frame_output, frame_input
    def RESULT():
        global frame_output
        a_val = NNumber([int(i) for i in a.get()])
        b_val = NNumber([int(i) for i in b.get()])
        frame_input.destroy()
        frame_output = Frame(window)
        frame_output.grid()
        window.title("Остаток от деления двух чисел")
        result = Text(frame_output)
        result.grid()
        result.insert(1.0, ("{0} mod {1} = {2}".format(str(a_val), str(b_val), str(Naturals.MOD_NN_N(a_val, b_val)))))
        result.configure(state='disabled')

    try:
        frame_output.destroy()
    except:
        print("none")
    try:
        frame_input.destroy()
    except:
        print("none")
    frame.destroy()
    frame_input = Frame(window)
    frame_input.grid()
    window.title("Остаток от деления двух чисел")
    a_lab = Label(frame_input, text="Введите первое число:").grid(row=1, column=1)
    a = Entry(frame_input, width=16)
    a.grid(row=1, column=2, padx=(4, 0))
    b_lab = Label(frame_input, text="Введите второе число:").grid(row=2, column=1)
    b = Entry(frame_input, width=16)
    b.grid(row=2, column=2, padx=(4, 0))
    but = Button(frame_input, text="Рассчитать", width=10, command=RESULT).grid(row=3, column=1, padx=(10, 0))

# НОД чисел
def GCF_NN_N():
    global frame_output, frame_input

    def RESULT():
        global frame_output
        a_val = NNumber([int(i) for i in a.get()])
        b_val = NNumber([int(i) for i in b.get()])
        frame_input.destroy()
        frame_output = Frame(window)
        frame_output.grid()
        window.title("НОД двух чисел")
        result = Text(frame_output)
        result.grid()
        result.insert(1.0, (
            "НОД({0}, {1}) = {2}".format(str(a_val), str(b_val), str(Naturals.GCF_NN_N(a_val, b_val))))).grid(row=1,
                                                                                                             column=1)

        result.configure(state='disabled')

    try:
        frame_output.destroy()
    except:
        print("none")
    try:
        frame_input.destroy()
    except:
        print("none")
    frame.destroy()
    frame_input = Frame(window)
    frame_input.grid()
    window.title("НОД двух чисел")
    a_lab = Label(frame_input, text="Введите первое число:").grid(row=1, column=1)
    a = Entry(frame_input, width=16)
    a.grid(row=1, column=2, padx=(4, 0))
    b_lab = Label(frame_input, text="Введите второе число:").grid(row=2, column=1)
    b = Entry(frame_input, width=16)
    b.grid(row=2, column=2, padx=(4, 0))
    but = Button(frame_input, text="Рассчитать", width=10, command=RESULT).grid(row=3, column=1, padx=(10, 0))

# НОК чисел
def LCM_NN_N():
    global frame_output, frame_input

    def RESULT():
        global frame_output
        a_val = NNumber([int(i) for i in a.get()])
        b_val = NNumber([int(i) for i in b.get()])
        frame_input.destroy()
        frame_output = Frame(window)
        frame_output.grid()
        window.title("НОК двух чисел")
        result = Text(frame_output)
        result.grid()
        result.insert(1.0, (
            "НОК({0}, {1}) = {2}".format(str(a_val), str(b_val), str(Naturals.LCM_NN_N(a_val, b_val))))).grid(row=1,
                                                                                                             column=1)
        result.configure(state='disabled')

    try:
        frame_output.destroy()
    except:
        print("none")
    try:
        frame_input.destroy()
    except:
        print("none")
    frame.destroy()
    frame_input = Frame(window)
    frame_input.grid()
    window.title("НОК двух чисел")
    a_lab = Label(frame_input, text="Введите первое число:").grid(row=1, column=1)
    a = Entry(frame_input, width=16)
    a.grid(row=1, column=2, padx=(4, 0))
    b_lab = Label(frame_input, text="Введите второе число:").grid(row=2, column=1)
    b = Entry(frame_input, width=16)
    b.grid(row=2, column=2, padx=(4, 0))
    but = Button(frame_input, text="Рассчитать", width=10, command=RESULT).grid(row=3, column=1, padx=(10, 0))


# INTEGER NUMBERS
# Сумма целых чисел
def ADD_ZZ_Z():
    global frame_output, frame_input

    def RESULT():
        global frame_output
        a_val = str(a.get())
        b_val = str(b.get())
        if a_val[0] == '-':
            a_val = Integer([int(i) for i in a_val[1:]], True)
        else:
            a_val = Integer([int(i) for i in a_val], False)
        if b_val[0] == '-':
            b_val = Integer([int(i) for i in b_val[1:]], True)
        else:
            b_val = Integer([int(i) for i in b_val], False)
        frame_input.destroy()
        frame_output = Frame(window)
        frame_output.grid()
        window.title("Результат суммы целых чисел")
        result = Text(frame_output)
        result.grid()
        result.insert(1.0, ("({0}) + ({1}) = {2}".format(str(a_val), str(b_val),
                                                        str(Integers.ADD_ZZ_Z(a_val, b_val)))))
        result.configure(state='disabled')
    try:
        frame_output.destroy()
    except:
        print("none")
    try:
        frame_input.destroy()
    except:
        print("none")
    frame.destroy()
    frame_input = Frame(window)
    frame_input.grid()
    window.title("Сумма целых чисел")
    a_lab = Label(frame_input, text="Введите первое число:").grid(row=1, column=1)
    a = Entry(frame_input, width=16)
    a.grid(row=1, column=2, padx=(4, 0))
    b_lab = Label(frame_input, text="Введите второе число:").grid(row=2, column=1)
    b = Entry(frame_input, width=16)
    b.grid(row=2, column=2, padx=(4, 0))
    but = Button(frame_input, text="Рассчитать", width=10, command=RESULT).grid(row=3, column=1, padx=(10, 0))

# Разность целых чисел
def SUB_ZZ_Z():
    global frame_output, frame_input

    def RESULT():
        global frame_output
        a_val = str(a.get())
        b_val = str(b.get())
        if a_val[0] == '-':
            a_val = Integer([int(i) for i in a_val[1:]], True)
        else:
            a_val = Integer([int(i) for i in a_val], False)
        if b_val[0] == '-':
            b_val = Integer([int(i) for i in b_val[1:]], True)
        else:
            b_val = Integer([int(i) for i in b_val], False)
        frame_input.destroy()
        frame_output = Frame(window)
        frame_output.grid()
        window.title("Результат разности целых чисел")
        result = Text(frame_output)
        result.grid(column=1, row=1)
        result.insert(1.0, "({0}) - ({1}) = {2}".format(str(a_val), str(b_val),
                                                        str(Integers.SUB_ZZ_Z(a_val, b_val))))
        result.configure(state='disabled')\

    try:
        frame_output.destroy()
    except:
        print("none")
    try:
        frame_input.destroy()
    except:
        print("none")
    frame.destroy()
    frame_input = Frame(window)
    frame_input.grid()
    window.title("Разность целых чисел")
    a_lab = Label(frame_input, text="Введите первое число:").grid(row=1, column=1)
    a = Entry(frame_input, width=16)
    a.grid(row=1, column=2, padx=(4, 0))
    b_lab = Label(frame_input, text="Введите второе число:").grid(row=2, column=1)
    b = Entry(frame_input, width=16)
    b.grid(row=2, column=2, padx=(4, 0))
    but = Button(frame_input, text="Рассчитать", width=10, command=RESULT).grid(row=3, column=1, padx=(10, 0))

# Произведение целых чисел
def MUL_ZZ_Z():
    global frame_output, frame_input

    def RESULT():
        global frame_output
        a_val = str(a.get())
        b_val = str(b.get())
        if a_val[0] == '-':
            a_val = Integer([int(i) for i in a_val[1:]], True)
        else:
            a_val = Integer([int(i) for i in a_val], False)
        if b_val[0] == '-':
            b_val = Integer([int(i) for i in b_val[1:]], True)
        else:
            b_val = Integer([int(i) for i in b_val], False)
        frame_input.destroy()
        frame_output = Frame(window)
        frame_output.grid()
        window.title("Результат произведения целых чисел")
        result = Text(frame_output)
        result.grid(column=1, row=1)
        result.insert(1.0, "({0}) * ({1}) = {2}".format(str(a_val), str(b_val),
                                                        str(Integers.MUL_ZZ_Z(a_val, b_val))))
        result.configure(state='disabled')

    try:
        frame_output.destroy()
    except:
        print("none")
    try:
        frame_input.destroy()
    except:
        print("none")
    frame.destroy()
    frame_input = Frame(window)
    frame_input.grid()
    window.title("Произведение целых чисел")
    a_lab = Label(frame_input, text="Введите первое число:").grid(row=1, column=1)
    a = Entry(frame_input, width=16)
    a.grid(row=1, column=2, padx=(4, 0))
    b_lab = Label(frame_input, text="Введите второе число:").grid(row=2, column=1)
    b = Entry(frame_input, width=16)
    b.grid(row=2, column=2, padx=(4, 0))
    but = Button(frame_input, text="Рассчитать", width=10, command=RESULT).grid(row=3, column=1, padx=(10, 0))

# Целая часть деления двух чисел
def DIV_ZZ_Z():
    global frame_output, frame_input

    def RESULT():
        global frame_output
        a_val = str(a.get())
        b_val = str(b.get())
        if a_val[0] == '-':
            a_val = Integer([int(i) for i in a_val[1:]], True)
        else:
            a_val = Integer([int(i) for i in a_val], False)
        if b_val[0] == '-':
            b_val = Integer([int(i) for i in b_val[1:]], True)
        else:
            b_val = Integer([int(i) for i in b_val], False)
        frame_input.destroy()
        frame_output = Frame(window)
        frame_output.grid()
        window.title("Неполное частное целых чисел")
        result = Text(frame_output)
        result.grid(column=1, row=1)
        result.insert(1.0, "({0}) div ({1}) = {2}".format(str(a_val), str(b_val),
                                                        str(Integers.DIV_ZZ_Z(a_val, b_val))))
        result.configure(state='disabled')

    try:
        frame_output.destroy()
    except:
        print("none")
    try:
        frame_input.destroy()
    except:
        print("none")
    frame.destroy()
    frame_input = Frame(window)
    frame_input.grid()
    window.title("Неполное частное целых чисел")
    a_lab = Label(frame_input, text="Введите первое число:").grid(row=1, column=1)
    a = Entry(frame_input, width=16)
    a.grid(row=1, column=2, padx=(4, 0))
    b_lab = Label(frame_input, text="Введите второе число:").grid(row=2, column=1)
    b = Entry(frame_input, width=16)
    b.grid(row=2, column=2, padx=(4, 0))
    but = Button(frame_input, text="Рассчитать", width=10, command=RESULT).grid(row=3, column=1, padx=(10, 0))

# Остаток от деления двух чисел
def MOD_ZZ_Z():
    global frame_output, frame_input

    def RESULT():
        global frame_output
        a_val = str(a.get())
        b_val = str(b.get())
        if a_val[0] == '-':
            a_val = Integer([int(i) for i in a_val[1:]], True)
        else:
            a_val = Integer([int(i) for i in a_val], False)
        if b_val[0] == '-':
            b_val = Integer([int(i) for i in b_val[1:]], True)
        else:
            b_val = Integer([int(i) for i in b_val], False)
        frame_input.destroy()
        frame_output = Frame(window)
        frame_output.grid()
        window.title("Остаток от деления целых чисел")
        result = Text(frame_output)
        result.grid(column=1, row=1)
        result.insert(1.0, "({0}) mod ({1}) = {2}".format(str(a_val), str(b_val),
                                                        str(Integers.MOD_ZZ_Z(a_val, b_val))))
        result.configure(state='disabled')

    try:
        frame_output.destroy()
    except:
        print("none")
    try:
        frame_input.destroy()
    except:
        print("none")
    frame.destroy()
    frame_input = Frame(window)
    frame_input.grid()
    window.title("Остаток от деления целых чисел")
    a_lab = Label(frame_input, text="Введите первое число:").grid(row=1, column=1)
    a = Entry(frame_input, width=16)
    a.grid(row=1, column=2, padx=(4, 0))
    b_lab = Label(frame_input, text="Введите второе число:").grid(row=2, column=1)
    b = Entry(frame_input, width=16)
    b.grid(row=2, column=2, padx=(4, 0))
    but = Button(frame_input, text="Рассчитать", width=10, command=RESULT).grid(row=3, column=1, padx=(10, 0))


# RATIONALS NUMBERS
# Сокращение дроби
def RED_Q_Q():
    global frame_output, frame_input

    def RESULT():
        global frame_output
        a_val = RNumber(str(a.get()))
        frame_input.destroy()
        frame_output = Frame(window)
        frame_output.grid()
        window.title("Результат сокращения дроби")
        result = Text(frame_output)
        result.grid(column=1, row=1)
        result.insert(1.0, "{0} = {1}".format(a_val, Rationals.RED_Q_Q(a_val)))
        result.configure(state='disabled')

    try:
        frame_output.destroy()
    except:
        print("none")
    try:
        frame_input.destroy()
    except:
        print("none")
    frame.destroy()
    frame_input = Frame(window)
    frame_input.grid()
    window.title("Сокращение дроби")
    a_lab = Label(frame_input, text="Введите дробь:").grid(row=1, column=1)
    a = Entry(frame_input, width=16)
    a.grid(row=1, column=2, padx=(4, 0))
    but = Button(frame_input, text="Рассчитать", width=10, command=RESULT).grid(row=3, column=1, padx=(10, 0))

# Сложение дробей
def ADD_QQ_Q():
    global frame_output, frame_input

    def RESULT():
        global frame_output
        a_val = RNumber(str(a.get()))
        b_val = RNumber(str(b.get()))
        frame_input.destroy()
        frame_output = Frame(window)
        frame_output.grid()
        window.title("Результат суммы дробей")
        result = Text(frame_output)
        result.grid(column=1, row=1)
        result.insert(1.0, "{0} + {1} = {2}".format(a_val, b_val, Rationals.ADD_QQ_Q(a_val, b_val)))
        result.configure(state='disabled')

    try:
        frame_output.destroy()
    except:
        print("none")
    try:
        frame_input.destroy()
    except:
        print("none")
    frame.destroy()
    frame_input = Frame(window)
    frame_input.grid()
    window.title("Сумма дробей")
    a_lab = Label(frame_input, text="Введите первую дробь:").grid(row=1, column=1)
    a = Entry(frame_input, width=16)
    a.grid(row=1, column=2, padx=(4, 0))
    b_lab = Label(frame_input, text="Введите вторую дробь:").grid(row=2, column=1)
    b = Entry(frame_input, width=16)
    b.grid(row=2, column=2, padx=(4, 0))
    but = Button(frame_input, text="Рассчитать", width=10, command=RESULT).grid(row=3, column=1, padx=(10, 0))

# Вычетание дробей
def SUB_QQ_Q():
    global frame_output, frame_input

    def RESULT():
        global frame_output
        a_val = RNumber(str(a.get()))
        b_val = RNumber(str(b.get()))
        frame_input.destroy()
        frame_output = Frame(window)
        frame_output.grid()
        window.title("Результат разности дробей")
        result = Text(frame_output)
        result.grid(column=1, row=1)
        result.insert(1.0, "{0} + {1} = {2}".format(a_val, b_val, Rationals.SUB_QQ_Q(a_val, b_val)))
        result.configure(state='disabled')

    try:
        frame_output.destroy()
    except:
        print("none")
    try:
        frame_input.destroy()
    except:
        print("none")
    frame.destroy()
    frame_input = Frame(window)
    frame_input.grid()
    window.title("Разность дробей")
    a_lab = Label(frame_input, text="Введите первую дробь:").grid(row=1, column=1)
    a = Entry(frame_input, width=16)
    a.grid(row=1, column=2, padx=(4, 0))
    b_lab = Label(frame_input, text="Введите вторую дробь:").grid(row=2, column=1)
    b = Entry(frame_input, width=16)
    b.grid(row=2, column=2, padx=(4, 0))
    but = Button(frame_input, text="Рассчитать", width=10, command=RESULT).grid(row=3, column=1, padx=(10, 0))

# Умножение дробей
def MUL_QQ_Q():
    global frame_output, frame_input

    def RESULT():
        global frame_output
        a_val = RNumber(str(a.get()))
        b_val = RNumber(str(b.get()))
        frame_input.destroy()
        frame_output = Frame(window)
        frame_output.grid()
        window.title("Результат произведения дробей")
        result = Text(frame_output)
        result.grid(column=1, row=1)
        result.insert(1.0, "{0} + {1} = {2}".format(a_val, b_val, Rationals.MUL_QQ_Q(a_val, b_val)))
        result.configure(state='disabled')

    try:
        frame_output.destroy()
    except:
        print("none")
    try:
        frame_input.destroy()
    except:
        print("none")
    frame.destroy()
    frame_input = Frame(window)
    frame_input.grid()
    window.title("Произведение дробей")
    a_lab = Label(frame_input, text="Введите первую дробь:").grid(row=1, column=1)
    a = Entry(frame_input, width=16)
    a.grid(row=1, column=2, padx=(4, 0))
    b_lab = Label(frame_input, text="Введите вторую дробь:").grid(row=2, column=1)
    b = Entry(frame_input, width=16)
    b.grid(row=2, column=2, padx=(4, 0))
    but = Button(frame_input, text="Рассчитать", width=10, command=RESULT).grid(row=3, column=1, padx=(10, 0))

# Деление дробей
def DIV_QQ_Q():
    global frame_output, frame_input

    def RESULT():
        global frame_output
        a_val = RNumber(str(a.get()))
        b_val = RNumber(str(b.get()))
        frame_input.destroy()
        frame_output = Frame(window)
        frame_output.grid()
        window.title("Результат частного дробей")
        result = Text(frame_output)
        result.grid(column=1, row=1)
        result.insert(1.0, "{0} + {1} = {2}".format(a_val, b_val, Rationals.DIV_QQ_Q(a_val, b_val)))
        result.configure(state='disabled')

    try:
        frame_output.destroy()
    except:
        print("none")
    try:
        frame_input.destroy()
    except:
        print("none")
    frame.destroy()
    frame_input = Frame(window)
    frame_input.grid()
    window.title("Частное дробей")
    a_lab = Label(frame_input, text="Введите первую дробь:").grid(row=1, column=1)
    a = Entry(frame_input, width=16)
    a.grid(row=1, column=2, padx=(4, 0))
    b_lab = Label(frame_input, text="Введите вторую дробь:").grid(row=2, column=1)
    b = Entry(frame_input, width=16)
    b.grid(row=2, column=2, padx=(4, 0))
    but = Button(frame_input, text="Рассчитать", width=10, command=RESULT).grid(row=3, column=1, padx=(10, 0))


window = Tk()
window.option_add("*Label.Font", "helvetica 20 bold")
window.option_add("*Text.Font", "helvetica 20 bold")
window.title("Коллоквиум ДМ - 2022")
window.geometry("800x500")
menu = Menu(window)
natural = Menu(menu, tearoff=0)
integer = Menu(menu, tearoff=0)
rational = Menu(menu, tearoff=0)
polynomials = Menu(menu, tearoff=0)
natural.add_command(label="Прибавление 1 к числу", command=ADD_1N_N)
natural.add_command(label="Сложение чисел", command=ADD_NN_N)
natural.add_command(label="Вычитание чисел", command=SUB_NN_N)
natural.add_command(label="Умножение чисел", command=MUL_NN_N)
natural.add_command(label="Неполное частное", command=DIV_NN_N)
natural.add_command(label="Остаток от деления", command=MOD_NN_N)
natural.add_command(label="НОД", command=GCF_NN_N)
natural.add_command(label="НОК", command=LCM_NN_N)

integer.add_command(label="Сумма чисел", command=ADD_ZZ_Z)
integer.add_command(label="Разность чисел", command=SUB_ZZ_Z)
integer.add_command(label="Произведение чисел", command=MUL_ZZ_Z)
integer.add_command(label="Неполное частное", command=DIV_ZZ_Z)
integer.add_command(label="Остаток от деления", command=MOD_ZZ_Z)

rational.add_command(label="Сокращение дроби", command=RED_Q_Q)
rational.add_command(label="Сложение дробей", command=ADD_QQ_Q)
rational.add_command(label="Вычитание дробей", command=SUB_QQ_Q)
rational.add_command(label="Умножение дробей", command=MUL_QQ_Q)
rational.add_command(label="Деление дробей", command=DIV_QQ_Q)

polynomials.add_command(label="Сложение многочленов")
polynomials.add_command(label="Вычитание многочленов")
polynomials.add_command(label="Вынесение НОК знаменателей и НОД числителей")
polynomials.add_command(label="Умножение многочленов")
polynomials.add_command(label="Неполное частное")
polynomials.add_command(label="Остаток от деления")
polynomials.add_command(label="НОД многочленов")
polynomials.add_command(label="Производная многочлена")
polynomials.add_command(label="Кратные корни в простые")

menu.add_cascade(label="Натуральные числа", menu=natural)
menu.add_cascade(label="Целые числа", menu=integer)
menu.add_cascade(label="Рациональные числа", menu=rational)
menu.add_cascade(label="Многочлен с рациональными коэффициентами", menu=polynomials)
frame = Frame(window)
frame.grid()
hello = Label(frame, text="Выберите в меню необходимую Вам функцию!")
hello.grid(column=1, row=1)
window.config(menu=menu)
window.mainloop()
