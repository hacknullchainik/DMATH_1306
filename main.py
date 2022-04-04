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
from Naturals_test import Ntest,Nlist
from Integers_test import Itest,Ilist
from Rationals_test import Rtest,Rlist
from Polynomials_test import Ptest,Plist
Ntest(Nlist) #............EF
Itest(Ilist) #......F.FF
Rtest(Rlist) # E...FE.F
Ptest(Plist)