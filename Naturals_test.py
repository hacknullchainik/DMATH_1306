import unittest
from Dtypes import *
from math import gcd, lcm
from Naturals import *
# python Naturals_test.py -v

Nlist = ['COM_NN_D','NZER_N_B','ADD_1N_N','ADD_NN_N','SUB_NN_N','MUL_ND_N','MUL_Nk_N','MUL_NN_N','SUB_NDN_N']

class TestNaturals(unittest.TestCase):
    # python -m unittest Naturals_test.TestNaturals.test_COM_NN_D
    def test_COM_NN_D(self):
        self.assertEqual(COM_NN_D(NNumber('9'*100), NNumber('0'*100)), 2)
        self.assertEqual(COM_NN_D(NNumber('0'*100), NNumber('0'*100)), 0)
        self.assertEqual(COM_NN_D(NNumber('1' * 100), NNumber('1' * 100)), 0)
        self.assertEqual(COM_NN_D(NNumber('1'*99+'0'), NNumber('1'*100)), 1)

    # python -m unittest Naturals_test.TestNaturals.test_NZER_N_B
    def test_NZER_N_B(self):
        self.assertEqual(NZER_N_B(NNumber('1'*100)), 1)
        self.assertEqual(NZER_N_B(NNumber('0' * 100)), 0)
        self.assertEqual(NZER_N_B(NNumber('786587612418' * 10)), 1)

    # python -m unittest Naturals_test.TestNaturals.test_ADD_1N_N
    def test_ADD_1N_N(self):
        self.assertEqual(ADD_1N_N(NNumber('111' * 11 + '1')).__str__(), '111' * 11 + '2')
        self.assertEqual(ADD_1N_N(NNumber('0'*1000)).__str__(), '1')
        self.assertEqual(ADD_1N_N(NNumber('999' * 11)).__str__(), '1' + '000' * 11)

    # python -m unittest Naturals_test.TestNaturals.test_ADD_NN_N
    def test_ADD_NN_N(self):
        self.assertEqual(ADD_NN_N(NNumber('123'*10), NNumber('123'*10)).__str__(), str(int('123'*10)*2))
        self.assertEqual(ADD_NN_N(NNumber('0' * 10), NNumber('123' * 10)).__str__(), str(int('123' * 10)))
        self.assertEqual(ADD_NN_N(NNumber('999' * 10), NNumber('999' * 10)).__str__(), str(int('999' * 10) * 2))
        self.assertEqual(ADD_NN_N(NNumber('777' * 10), NNumber('111' * 10)).__str__(), str(int('888' * 10)))
        self.assertEqual(ADD_NN_N(NNumber('999' * 10), NNumber('1')).__str__(), str(int('999'*10)+1))

    def test_SUB_NN_N(self):
        self.assertEqual(SUB_NN_N(NNumber('123'), NNumber('123123')).__str__(), '0')
        self.assertEqual(SUB_NN_N(NNumber('123'), NNumber('122')).__str__(), '1')
        self.assertEqual(SUB_NN_N(NNumber('223'*100), NNumber('123'*100)).__str__(), '100'*100)
        self.assertEqual(SUB_NN_N(NNumber('0' * 100), NNumber('0' * 100)).__str__(), '0')
        self.assertEqual(SUB_NN_N(NNumber('999' * 100), NNumber('188' * 100)).__str__(), '811'*100)

    def test_MUL_ND_N(self):
        self.assertEqual(MUL_ND_N(NNumber('9876543'), 5).__str__(), str(9876543 * 5))
        self.assertEqual(MUL_ND_N(NNumber('111' * 9), 9).__str__(), str(int('999'*9)))
        self.assertEqual(MUL_ND_N(NNumber('123'), 1).__str__(), str(123))
        self.assertEqual(MUL_ND_N(NNumber('0'), 6).__str__(), '0')
        self.assertEqual(MUL_ND_N(NNumber('123'), 9).__str__(), str(123*9))

    def test_MUL_Nk_N(self):
        self.assertEqual(MUL_Nk_N(NNumber('123'),10).__str__(),'123'+'0'*10)
        self.assertEqual(MUL_Nk_N(NNumber('123'), -1).__str__(), '123')
        self.assertEqual(MUL_Nk_N(NNumber('123'), 0).__str__(), '123')
        self.assertEqual(MUL_Nk_N(NNumber('123'), 1).__str__(), '1230')
        self.assertEqual(MUL_Nk_N(NNumber('1'+'0'*100),100).__str__(),'1'+'0'*200)

    def test_MUL_NN_N(self):
        self.assertEqual(MUL_NN_N(NNumber('123'),NNumber('123')).__str__(),str(123*123))
        self.assertEqual(MUL_NN_N(NNumber('123'), NNumber('9')).__str__(), str(123 * 9))
        self.assertEqual(MUL_NN_N(NNumber('123'), NNumber('0')).__str__(), '0')
        self.assertEqual(MUL_NN_N(NNumber('999'), NNumber('999')).__str__(), str(999 * 999))
        self.assertEqual(MUL_NN_N(NNumber('1'), NNumber('123')).__str__(), str(123))
        self.assertEqual(MUL_NN_N(NNumber('123'), NNumber('111')).__str__(), str(111 * 123))
        self.assertEqual(MUL_NN_N(NNumber('100'), NNumber('123')).__str__(), str(123 * 100))
        self.assertEqual(MUL_NN_N(NNumber('765433123'), NNumber('123')).__str__(), str(765433123 * 123))

    def test_SUB_NDN_N(self):
        self.assertEqual(SUB_NDN_N(NNumber('745386'),9,NNumber('123')).__str__(),str(745386-(9*123)))
        self.assertEqual(SUB_NDN_N(NNumber('9999999'), 9, NNumber('11111')).__str__(),'0')
        self.assertEqual(SUB_NDN_N(NNumber('0'), 0, NNumber('0')).__str__(), '0')
        self.assertEqual(SUB_NDN_N(NNumber('1'), 1, NNumber('1')).__str__(), '0')
        self.assertEqual(SUB_NDN_N(NNumber('2'), 2, NNumber('2')).__str__(), '0')
        self.assertEqual(SUB_NDN_N(NNumber('10'), 9, NNumber('1')).__str__(), '1')
        self.assertEqual(SUB_NDN_N(NNumber('9'*100), 9, NNumber('1'+'0'*99)).__str__(),'9'*99)

    # python -m unittest Naturals_test.TestNaturals.test_DIV_NN_Dk
    def test_DIV_NN_Dk(self):
        self.assertEqual(DIV_NN_Dk(NNumber('123123'),NNumber('123123')).__str__(),'1')
        self.assertEqual(DIV_NN_Dk(NNumber('123123'), NNumber('123')).__str__(), '1000')
        self.assertEqual(DIV_NN_Dk(NNumber('999999'), NNumber('1')).__str__(), '900000')
        self.assertEqual(DIV_NN_Dk(NNumber('0'), NNumber('0')).__str__(), '0')
        self.assertRaises(ZeroDivisionError, DIV_NN_Dk, NNumber('0'), NNumber('0'))
        self.assertRaises(ZeroDivisionError, DIV_NN_Dk, NNumber('123123'), NNumber('0'))

    # python -m unittest Naturals_test.TestNaturals.test_DIV_NN_N
    def test_DIV_NN_N(self):
        self.assertEqual(DIV_NN_N(NNumber('123123'), NNumber('123123')).__str__(), '1')
        self.assertEqual(DIV_NN_N(NNumber('999999'), NNumber('1')).__str__(), '999999')
        self.assertEqual(DIV_NN_N(NNumber('123'*12),NNumber('7'*10)).__str__(), str(int('123'*12)//int('7'*10)))
        self.assertEqual(DIV_NN_N(NNumber('1107'), NNumber('9')).__str__(), '123')
        self.assertEqual(DIV_NN_N(NNumber('0'), NNumber('1111111')).__str__(), '0')
        self.assertRaises(ZeroDivisionError, DIV_NN_Dk, NNumber('0'), NNumber('0'))
        self.assertRaises(ZeroDivisionError, DIV_NN_Dk, NNumber('123123'), NNumber('0'))

    # python -m unittest Naturals_test.TestNaturals.test_MOD_NN_N
    def test_MOD_NN_N(self):
        self.assertEqual(MOD_NN_N(NNumber('100'), NNumber('100')).__str__(),'0')
        self.assertEqual(MOD_NN_N(NNumber('1000'), NNumber('100')).__str__(),'0')
        self.assertEqual(MOD_NN_N(NNumber('101'), NNumber('100')).__str__(),'1')
        self.assertEqual(MOD_NN_N(NNumber('0'), NNumber('0')).__str__(),'0')
        self.assertEqual(MOD_NN_N(NNumber('777'), NNumber('100')).__str__(),'77')
        self.assertEqual(MOD_NN_N(NNumber('123'*9), NNumber('99'*9)).__str__(), str(int('123'*9) % int('99'*9)))
        self.assertEqual(MOD_NN_N(NNumber('0'), NNumber('1000000')).__str__(),'0')
        self.assertEqual(MOD_NN_N(NNumber('10'), NNumber('7')).__str__(),'3')
        self.assertEqual(MOD_NN_N(NNumber('10'),NNumber('0')).__str__(),0)

    # python -m unittest Naturals_test.TestNaturals.test_GCF_NN_N
    def test_GCF_NN_N(self):
        self.assertEqual(GCF_NN_N(NNumber('0'),NNumber('0')).__str__(), str(gcd(0,0)))
        self.assertEqual(GCF_NN_N(NNumber('100'),NNumber('10')).__str__(), str(gcd(100,10)))
        self.assertEqual(GCF_NN_N(NNumber('111'),NNumber('4')).__str__(), str(gcd(111,4)))
        self.assertEqual(GCF_NN_N(NNumber('123123123123'),NNumber('99999999')).__str__(),str(gcd(123123123123, 99999999)))
        self.assertEqual(GCF_NN_N(NNumber('1'),NNumber('0')).__str__(), str(gcd(1,0)))
        self.assertEqual(GCF_NN_N(NNumber('0'), NNumber('1')).__str__(), str(gcd(0, 1)))

    # python -m unittest Naturals_test.TestNaturals.test_LCM_NN_N
    def test_LCM_NN_N(self):
        self.assertEqual(LCM_NN_N(NNumber('123'),NNumber('123')).__str__(),'123')
        self.assertEqual(LCM_NN_N(NNumber('0'),NNumber('123')).__str__(),'0')
        self.assertEqual(LCM_NN_N(NNumber('123'),NNumber('0')).__str__(),'0')
        self.assertEqual(LCM_NN_N(NNumber('1'),NNumber('123')).__str__(),'123')
        self.assertEqual(LCM_NN_N(NNumber('246'),NNumber('123')).__str__(),'246')
        self.assertEqual(LCM_NN_N(NNumber('99999'),NNumber('123')).__str__(),str(lcm(99999,123)))
        self.assertEqual(LCM_NN_N(NNumber('1111111111111111111111'),NNumber('123')).__str__(),str(lcm(1111111111111111111111,123)))
        a, b = '1122211111111', '121157'
        self.assertEqual(LCM_NN_N(NNumber(a), NNumber(b)).__str__(), str(lcm(int(a), int(b))))
        a, b = '1122211111111', '121199'
        self.assertEqual(LCM_NN_N(NNumber(a), NNumber(b)).__str__(), str(lcm(int(a), int(b))))
        a, b = '1122211111111', '99999999999999999999999999999999999999999999'
        self.assertEqual(LCM_NN_N(NNumber(a), NNumber(b)).__str__(), str(lcm(int(a), int(b))))
        a, b = '1122211111111', '100000000000000000000000000000000000'
        self.assertEqual(LCM_NN_N(NNumber(a), NNumber(b)).__str__(), str(lcm(int(a), int(b))))
        a,b = '1122211111111156756575671222111356736711', '1211578190987654'
        self.assertEqual(LCM_NN_N(NNumber(a),NNumber(b)).__str__(),str(lcm(int(a), int(b))))


def Ntest(name:list):
    suite = unittest.TestSuite()
    for i in name:
        suite.addTest(TestNaturals('test_'+i))
    runner = unittest.TextTestRunner()
    runner.run(suite)
