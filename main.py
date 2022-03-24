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

from Dtypes import Integer
from ALEX  import MOD_NN_N, MUL_ND_N, print_int

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

