# Комментарии к оформлению:
# Пока что пишем модулями(т.е. каждый назывет модуль типа ИМЯФ.py и подключает сюда (название на инглише, прим SEVAB.py)
# В модуле ваши функции, которые вызываются через точку типа(по сути просто пишите ваши функции в :
# import SEVAB
# SEVAB.funct_name()

# Адекватно называем переменные(кроме счётчиков циклов)
# Юзаем как можно больше комментариев (чтобы было понятно, че вы там написали)
# Между логическими частями ставьте пробелы, чтобы красиво (особенно перед комментариями)
# Ну и оставшиеся правила:
# Читы - бан
# Стельба по своим - бан
# Оскорбление администрации - расстрел, а потом бан.

from Dtypes import RNumber, NNumber, Integer, Polynomial
from ALEX  import MOD_NN_N, MUL_ND_N, print_int

# показываю пример работы с типами
# Задаётся двумя числами, у какого хнак- пхуй
rnum = RNumber(111,-13)
# Я реализовал удобный вывод, так чтобы вы не парились
print(rnum)  # -111/13


# Натуральное задаётся просто массивом цифр
# Конструктор принимает в интуитивном порядке 123 = 1,2,3
nnum = NNumber([1,2,3])
# Но представляется в обратном
print(nnum.get_num())  # 3 2 1
# Вывод тоже удобный
print(nnum)  # 123


# Целое списком и знаком
# True = отрицательное
# False = положительное
inum = Integer([1,2,3],True)
# Представление тоже обратное
print(inum.get_num())  # 3 2 1
# Вывод комфортабельный
print(inum)  # -123


# Многочлен - список из элементов типа Rnumber
rli = [RNumber(i,2+i) for i in range(4)]
print([i.__str__() for i in rli])  # сам список
pol = Polynomial(rli)
# Представление тоже обратное
print([i.__str__() for i in pol.get_coefs()])  # ['3/5', '2/4', '1/3', '0']
# Вывод тож реализовал
# где коэф 0 - не выводится
print(pol)  # (3/5)x^3 (2/4)x^2 (1/3)x^1

#--------ALEX---------
#----------------------
#Object 'inst'is an instance from the 'Integer' class in file 'Dtypes.py'
#Variable 'dig' stores the digit used for multiply 'inst'
inst = Integer([1,2,4,5],True)
dig = 2
#List 'inst_r'stores the result of the operation done upon the object inst
inst_r = MUL_ND_N(inst,dig)
#function for printing out the result 
print_int(inst.get_num(),inst_r,dig)