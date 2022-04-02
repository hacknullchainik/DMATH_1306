import unittest
from Dtypes import *
from math import gcd, lcm
from Integers import *
# python Integers_test.py -v


class TestIntegers(unittest.TestCase):
    # python -m unittest Integers_test.TestIntegers.test_ABS_Z_N
    def test_ABS_Z_N(self):
        self.assertEqual(ABS_Z_N(Integer('-'+'9'*1000)).__str__(),'9'*1000)
        self.assertEqual(ABS_Z_N(Integer('-'+'0' * 1000)).__str__(), '0')
        self.assertEqual(ABS_Z_N(Integer('1' * 1000)).__str__(), '1' * 1000)
        self.assertEqual(ABS_Z_N(Integer('-'+'1' * 1000)).__str__(), '1' * 1000)
        self.assertEqual(ABS_Z_N(Integer('-1000000')).__str__(), '1000000')

    # python -m unittest Integers_test.TestIntegers.test_POZ_Z_D
    def test_POZ_Z_D(self):
        self.assertEqual(POZ_Z_D(Integer('-'+'1'*100)),1)
        self.assertEqual(POZ_Z_D(Integer('1'*100)),2)
        self.assertEqual(POZ_Z_D(Integer('12333333'*10)),2)
        self.assertEqual(POZ_Z_D(Integer('-'+'12333333'*10)),1)
        self.assertEqual(POZ_Z_D(Integer('0'*10)),0)
        self.assertEqual(POZ_Z_D(Integer('0')),0)

    # python -m unittest Integers_test.TestIntegers.test_MUL_ZM_Z
    def test_MUL_ZM_Z(self):
        self.assertEqual(MUL_ZM_Z(Integer('-1')).__str__(),'1')
        self.assertEqual(MUL_ZM_Z(Integer('1')).__str__(),'-1')
        self.assertEqual(MUL_ZM_Z(Integer('-11111111111111111111111111111111')).__str__(),'11111111111111111111111111111111')
        self.assertEqual(MUL_ZM_Z(Integer('0')).__str__(),'0')
        self.assertEqual(MUL_ZM_Z(Integer('123123123123123')).__str__(),'-123123123123123')
        self.assertEqual(MUL_ZM_Z(Integer('999999')).__str__(),'-999999')

    # python -m unittest Integers_test.TestIntegers.test_TRANS_N_Z
    def test_TRANS_N_Z(self):
        self.assertEqual(TRANS_N_Z(NNumber('123')).__str__(), '123')
        self.assertEqual(TRANS_N_Z(NNumber('9'*1000)).__str__(), '9'*1000)
        self.assertEqual(TRANS_N_Z(NNumber('0')).__str__(), '0')
        self.assertEqual(TRANS_N_Z(NNumber('123')).__str__(), '123')

    # python -m unittest Integers_test.TestIntegers.test_TRANS_Z_N
    def test_TRANS_Z_N(self):
        self.assertEqual(TRANS_Z_N(Integer('123')).__str__(), '123')
        self.assertEqual(TRANS_Z_N(Integer('-123')).__str__(), '123')
        self.assertEqual(TRANS_Z_N(Integer('-0')).__str__(), '0')

    # python -m unittest Integers_test.TestIntegers.test_ADD_ZZ_Z
    def test_ADD_ZZ_Z(self):
        self.assertEqual(ADD_ZZ_Z(Integer('1'*100),Integer('1'*100)).__str__(),'2'*100)
        self.assertEqual(ADD_ZZ_Z(Integer('-'+'1'*100),Integer('1'*100)).__str__(),'0')
        self.assertEqual(ADD_ZZ_Z(Integer('1'*100),Integer('-'+'1'*100)).__str__(),'0')
        self.assertEqual(ADD_ZZ_Z(Integer('2'*100),Integer('-'+'1'*100)).__str__(),'1'*100)
        self.assertEqual(ADD_ZZ_Z(Integer('0'*100),Integer('1'*100)).__str__(),'1'*100)
        self.assertEqual(ADD_ZZ_Z(Integer('0'*100),Integer('-'+'1'*100)).__str__(),'-'+'1'*100)
        self.assertEqual(ADD_ZZ_Z(Integer('-'+'1'*100),Integer('-'+'1'*100)).__str__(),'-'+'2'*100)
        self.assertEqual(ADD_ZZ_Z(Integer('-' + '1' * 100), Integer('0')).__str__(), '-' + '1' * 100)
        a, b = '987'*10, '-'+'1'*10
        self.assertEqual(ADD_ZZ_Z(Integer(a), Integer(b)).__str__(), str(int(a)+int(b)))
        a, b = b,a
        self.assertEqual(ADD_ZZ_Z(Integer(a), Integer(b)).__str__(), str(int(a) + int(b)))

    # python -m unittest Integers_test.TestIntegers.test_SUB_ZZ_Z
    def test_SUB_ZZ_Z(self):
        self.assertEqual(ADD_ZZ_Z(Integer('-' + '1' * 100), Integer('1' * 100)).__str__(), '-'+'2'*100)
        self.assertEqual(ADD_ZZ_Z(Integer('1' * 100), Integer('-' + '1' * 100)).__str__(), '2'*100)
        self.assertEqual(ADD_ZZ_Z(Integer('2' * 100), Integer('-' + '1' * 100)).__str__(), '3' * 100)
        self.assertEqual(ADD_ZZ_Z(Integer('0' * 100), Integer('1' * 100)).__str__(), '-' + '1' * 100)
        self.assertEqual(ADD_ZZ_Z(Integer('0' * 100), Integer('-' + '1' * 100)).__str__(), '1' * 100)
        self.assertEqual(ADD_ZZ_Z(Integer('1' * 100), Integer('1' * 100)).__str__(), '0')
        self.assertEqual(ADD_ZZ_Z(Integer('-' + '1' * 100), Integer('-' + '1' * 100)).__str__(), '0')
        self.assertEqual(ADD_ZZ_Z(Integer('-' + '1' * 100), Integer('0')).__str__(), '-' + '1' * 100)
        a, b = '987' * 10, '-' + '1' * 10
        self.assertEqual(ADD_ZZ_Z(Integer(a), Integer(b)).__str__(), str(int(a) - int(b)))
        a, b = b, a
        self.assertEqual(ADD_ZZ_Z(Integer(a), Integer(b)).__str__(), str(int(a) - int(b)))

    # python -m unittest Integers_test.TestIntegers.test_MUL_ZZ_Z
    def test_MUL_ZZ_Z(self):
        self.assertEqual(MUL_ZZ_Z(Integer('0'),Integer('1'*100)).__str__(),'0')
        self.assertEqual(MUL_ZZ_Z(Integer('0'),Integer('0')).__str__(),'0')
        self.assertEqual(MUL_ZZ_Z(Integer('1'*100),Integer('0')).__str__(),'0')
        a, b = '987' * 10, '-' + '123' * 10
        self.assertEqual(MUL_ZZ_Z(Integer(a),Integer(b)).__str__(),str(int(a) * int(b)))
        a, b = '-'+'987' * 10, '-' + '123' * 10
        self.assertEqual(MUL_ZZ_Z(Integer(a),Integer(b)).__str__(),str(int(a) * int(b)))
        a, b = '987' * 10, '' + '123' * 10
        self.assertEqual(MUL_ZZ_Z(Integer(a),Integer(b)).__str__(),str(int(a) * int(b)))

    # python -m unittest Integers_test.TestIntegers.test_DIV_ZZ_Z
    def test_DIV_ZZ_Z(self):
        self.assertEqual(DIV_ZZ_Z(Integer('0'), Integer('1' * 100)).__str__(), '0')
        self.assertEqual(DIV_ZZ_Z(Integer('1'), Integer('1' * 100)).__str__(), '0')
        self.assertEqual(DIV_ZZ_Z(Integer('1'), Integer('1')).__str__(), '1')
        self.assertEqual(DIV_ZZ_Z(Integer('-1'), Integer('1')).__str__(), '-1')
        self.assertEqual(DIV_ZZ_Z(Integer('-1'), Integer('-1')).__str__(), '1')
        self.assertEqual(DIV_ZZ_Z(Integer('1'), Integer('-1')).__str__(), '-1')

        a,b = '123','9'
        self.assertEqual(DIV_ZZ_Z(Integer(a), Integer(b)).__str__(), str(int(a) // int(b)))
        a, b = '-123', '-9'
        self.assertEqual(DIV_ZZ_Z(Integer(a), Integer(b)).__str__(), str(int(a) // int(b)))
        a, b = '123', '-9'
        self.assertEqual(DIV_ZZ_Z(Integer(a), Integer(b)).__str__(), str(int(a) // int(b)))
        a, b = '987' * 10, '-' + '123' * 10
        self.assertEqual(DIV_ZZ_Z(Integer(a), Integer(b)).__str__(), str(int(a) // int(b)))

        self.assertRaises(ZeroDivisionError,DIV_ZZ_Z,Integer('1'), Integer('0' * 100))

    # python -m unittest Integers_test.TestIntegers.test_MOD_ZZ_Z
    def test_MOD_ZZ_Z(self):
        self.assertEqual(MOD_ZZ_Z(Integer('1'),Integer('1')).__str__(),str(1%1))
        # self.assertEqual(MOD_ZZ_Z(Integer('1'),Integer('-1')).__str__(),str(1%-1))
        # self.assertEqual(MOD_ZZ_Z(Integer('-1'),Integer('1')).__str__(),str(-1%1))
        self.assertEqual(MOD_ZZ_Z(Integer('-1'),Integer('-1')).__str__(),str(-1%-1))
        a, b = '-123', '-9'
        self.assertEqual(MOD_ZZ_Z(Integer(a),Integer(b)).__str__(),str(int(a)%int(b)))
        a, b = '123', '-9'
        self.assertEqual(MOD_ZZ_Z(Integer('1'),Integer('1')).__str__(),str(int(a)%int(b)))
        a, b = '-123', '9'
        self.assertEqual(MOD_ZZ_Z(Integer('1'),Integer('1')).__str__(),str(int(a)%int(b)))

        a, b = '-123', '0'
        self.assertEqual(MOD_ZZ_Z(Integer(a), Integer(b)).__str__(), str(int(a) % int(b)))
        a, b = '0', '-9'
        self.assertEqual(MOD_ZZ_Z(Integer('1'), Integer('1')).__str__(), str(int(a) % int(b)))
        a, b = '0', '0'
        self.assertEqual(MOD_ZZ_Z(Integer('1'), Integer('1')).__str__(), str(int(a) % int(b)))


if __name__ == "__main__":
    unittest.main()