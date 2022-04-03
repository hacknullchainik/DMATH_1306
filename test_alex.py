from random import randint
import unittest
from ALEX import SUB_QQ_Q, MOD_ZZ_Z
from Dtypes import Integer, RNumber
from fractions import Fraction

class test_rational(unittest.TestCase):

    def test_sub_qq_q(self):
        '''for i in range(100):
            val_num = randint(1,1000)
            val_den = randint(1,1000)

            val_num_1 = randint(1,1000)
            val_den_1 = randint(1,1000)

            res = Fraction(str(val_num)+'/'+str(val_den)) - Fraction(str(val_num_1)+'/'+str(val_den_1))

            print(f"({val_num}/{val_den}) - ({val_num_1} / {val_den_1})")
            print("res:",res,"sub:",SUB_QQ_Q(RNumber(str(val_num)+"/"+str(val_den)),RNumber(str(val_num_1)+"/"+str(val_den_1))))

            self.assertEqual(str(SUB_QQ_Q(RNumber(str(val_num)+"/"+str(val_den)),RNumber(str(val_num_1)+"/"+str(val_den_1)))),str(RNumber(str(res))))'''
        pass
    
    def test_mod_zz_z(self):
        for i in range(100):
            val_num_1 = randint(1,1000)
            val_num_2 = randint(1,100)
            res = MOD_ZZ_Z(Integer(str(val_num_1),False),Integer(str(val_num_2),False))
            check = val_num_1 % val_num_2
            print("Expected quotient: ",val_num_1 // val_num_2)
            print(f'{val_num_1} % {val_num_2} = {res} || excpected:  {check} \n-----------')
            
            self.assertEqual(str(res),str(check))
if __name__ == '__main__':
    unittest.main()