import unittest
from Dtypes import *
from math import gcd, lcm
from Rationals import *

# python Rationals_test.py -v

Rlist = ['RED_Q_Q', 'INT_Q_B', 'TRANS_Z_Q', 'TRANS_Q_Z', 'ADD_QQ_Q', 'SUB_QQ_Q', 'MUL_QQ_Q', 'DIV_QQ_Q']


class TestRationals(unittest.TestCase):
    def test_RED_Q_Q(self):
        self.assertEqual(RED_Q_Q(RNumber('123/123')).__str__(), '1')
        self.assertEqual(RED_Q_Q(RNumber('0/123')).__str__(), '0')
        self.assertEqual(RED_Q_Q(RNumber('1/123')).__str__(), '1/123')
        self.assertEqual(RED_Q_Q(RNumber('-1/123')).__str__(), '-1/123')
        self.assertEqual(RED_Q_Q(RNumber('-1/1')).__str__(), '-1')
        self.assertEqual(
            RED_Q_Q(RNumber('6726762439834275649822587948797802587/862536767676790869428574869848935876')).__str__(),
            '6726762439834275649822587948797802587/862536767676790869428574869848935876')
        self.assertEqual(RED_Q_Q(RNumber('-987654321234567890/228')).__str__(), '-493827160617283945/114')

    def test_INT_Q_B(self):
        self.assertEqual(INT_Q_B(RNumber('123/123')), True)
        self.assertEqual(INT_Q_B(RNumber('246/123')), True)
        self.assertEqual(INT_Q_B(RNumber('-1/1')), True)
        self.assertEqual(INT_Q_B(RNumber('0/123')), True)
        self.assertEqual(INT_Q_B(RNumber('2' * 100 + '/' + '1' * 100)), True)
        self.assertEqual(INT_Q_B(RNumber('124/123')), False)
        self.assertEqual(INT_Q_B(RNumber('124/123')), False)
        self.assertEqual(INT_Q_B(RNumber('122/123')), False)
        self.assertEqual(INT_Q_B(RNumber('1/12')), False)
        self.assertEqual(INT_Q_B(RNumber('-124/123')), False)
        self.assertEqual(INT_Q_B(RNumber('12312312213131/123')), False)

    def test_TRANS_Z_Q(self):
        self.assertEqual(TRANS_Z_Q(Integer('-123')).__str__(), '-123')
        self.assertEqual(TRANS_Z_Q(Integer('-1')).__str__(), '-1')
        self.assertEqual(TRANS_Z_Q(Integer('123')).__str__(), '123')
        self.assertEqual(TRANS_Z_Q(Integer('-0')).__str__(), '0')
        self.assertEqual(TRANS_Z_Q(Integer('8')).__str__(), '8')

    def test_TRANS_Q_Z(self):
        self.assertEqual(TRANS_Q_Z(RNumber('123/1')).__str__(), '123')
        self.assertEqual(TRANS_Q_Z(RNumber('-123/1')).__str__(), '-123')
        self.assertEqual(TRANS_Q_Z(RNumber('-121/11')).__str__(), '-121/11')
        self.assertEqual(TRANS_Q_Z(RNumber('-123/123')).__str__(), '-123/123')
        self.assertEqual(TRANS_Q_Z(RNumber('123/123')).__str__(), '123/123')
        self.assertEqual(TRANS_Q_Z(RNumber('-246/123')).__str__(), '-246/123')
        self.assertEqual(TRANS_Q_Z(RNumber('124/123')).__str__(), '124/123')
        self.assertEqual(TRANS_Q_Z(RNumber('11111111/11')).__str__(), '11111111/11')
        self.assertEqual(TRANS_Q_Z(RNumber('2222/3')).__str__(), '2222/3')

    def test_ADD_QQ_Q(self):
        self.assertEqual(ADD_QQ_Q(RNumber('1'), RNumber('1')).__str__(), '2')
        self.assertEqual(ADD_QQ_Q(RNumber('1/2'), RNumber('1')).__str__(), '3/2')
        self.assertEqual(ADD_QQ_Q(RNumber('-1/2'), RNumber('1')).__str__(), '1/2')
        self.assertEqual(ADD_QQ_Q(RNumber('3/3'), RNumber('9/3')).__str__(), '4')
        self.assertEqual(ADD_QQ_Q(RNumber('1/2'), RNumber('4/3')).__str__(), '11/6')
        self.assertEqual(ADD_QQ_Q(RNumber('0'), RNumber('1')).__str__(), '1')
        self.assertEqual(ADD_QQ_Q(RNumber('17/13'), RNumber('19/113')).__str__(), '2168/1469')
        self.assertEqual(ADD_QQ_Q(RNumber('17/13'), RNumber('-19/113')).__str__(), '1674/1469')
        self.assertEqual(
            ADD_QQ_Q(RNumber('125558563222564588/224571828157826397658257'), RNumber('40987654/30987654')).__str__(),
            '511370904524764425402194097535/386608561616787877927804342171')
        self.assertEqual(ADD_QQ_Q(RNumber('0'), RNumber('0')).__str__(), '0')

    def test_SUB_QQ_Q(self):
        self.assertEqual(SUB_QQ_Q(RNumber('1/2'), RNumber('1')).__str__(), '-1/2')
        self.assertEqual(
            SUB_QQ_Q(RNumber('125558563222564588/224571828157826397658257'), RNumber('40987654/30987654123')).__str__(),
            '-1022309069483458235506786240306/773217126302724074012569452338179')
        self.assertEqual(SUB_QQ_Q(RNumber('-1/2'), RNumber('1')).__str__(), '-3/2')
        self.assertEqual(SUB_QQ_Q(RNumber('3/3'), RNumber('9/3')).__str__(), '-2')
        self.assertEqual(SUB_QQ_Q(RNumber('1/2'), RNumber('4/3')).__str__(), '-5/6')
        self.assertEqual(SUB_QQ_Q(RNumber('0'), RNumber('1')).__str__(), '-1')
        self.assertEqual(SUB_QQ_Q(RNumber('1'), RNumber('1')).__str__(), '0')
        self.assertEqual(SUB_QQ_Q(RNumber('19/113'), RNumber('17/13')).__str__(), '-1674/1469')
        self.assertEqual(SUB_QQ_Q(RNumber('-17/13'), RNumber('19/113')).__str__(), '-2168/1469')
        self.assertEqual(SUB_QQ_Q(RNumber('0'), RNumber('0')).__str__(), '0')

    def test_MUL_QQ_Q(self):
        self.assertEqual(MUL_QQ_Q(RNumber('0'), RNumber('1')).__str__(), '0')
        self.assertEqual(MUL_QQ_Q(RNumber('1'), RNumber('0')).__str__(), '0')
        self.assertEqual(MUL_QQ_Q(RNumber('0'), RNumber('0')).__str__(), '0')
        self.assertEqual(MUL_QQ_Q(RNumber('0'), RNumber('11231221/1231231')).__str__(), '0')
        self.assertEqual(MUL_QQ_Q(RNumber('123/123'), RNumber('123/123')).__str__(), '15129/15129')
        self.assertEqual(MUL_QQ_Q(RNumber('246/123'), RNumber('123/123')).__str__(), '30258/15129')
        self.assertEqual(MUL_QQ_Q(RNumber('-246/123'), RNumber('123/123')).__str__(), '-30258/15129')
        self.assertEqual(MUL_QQ_Q(RNumber('-246/123'), RNumber('-123/123')).__str__(), '30258/15129')
        self.assertEqual(MUL_QQ_Q(RNumber('2'), RNumber('123/123')).__str__(), '246/123')
        self.assertEqual(MUL_QQ_Q(RNumber('3/2'), RNumber('2/3')).__str__(), '6/6')
        self.assertEqual(MUL_QQ_Q(RNumber('-3/2'), RNumber('2/3')).__str__(), '-6/6')
        self.assertEqual(MUL_QQ_Q(RNumber('13/17'), RNumber('19/3')).__str__(), '247/51')
        self.assertEqual(MUL_QQ_Q(RNumber('-1231312/124211'), RNumber('19876543/565')).__str__(),
                         '-24474225914416/70179215')

    def test_DIV_QQ_Q(self):
        self.assertEqual(DIV_QQ_Q(RNumber('1'), RNumber('1')).__str__(), '1')
        self.assertEqual(DIV_QQ_Q(RNumber('2'), RNumber('1')).__str__(), '2')
        self.assertEqual(DIV_QQ_Q(RNumber('-1'), RNumber('1')).__str__(), '-1')
        self.assertEqual(DIV_QQ_Q(RNumber('1'), RNumber('1123125/15165')).__str__(), '1011/74875')
        self.assertEqual(DIV_QQ_Q(RNumber('123516456/123516665'), RNumber('1')).__str__(), '123516456/123516665')
        self.assertEqual(DIV_QQ_Q(RNumber('0'), RNumber('1123/33215')).__str__(), '0')


def Rtest(name: list):
    suite = unittest.TestSuite()
    for i in name:
        suite.addTest(TestRationals('test_' + i))
    runner = unittest.TextTestRunner()
    runner.run(suite)
