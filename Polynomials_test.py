import unittest
from Dtypes import *
from math import gcd
from Polynomials import *
def lcm(a, b):
    return a*b//gcd(a, b)
# python Polynomials_test.py -v

Plist = ['ADD_PP_P','SUB_PP_P','MUL_PQ_Q','LED_P_Q','DEG_P_N','FAC_P_Q','DER_P_P','MUL_Pxk_P']


class TestPolynomials(unittest.TestCase):
    def test_ADD_PP_P(self):
        self.assertEqual(ADD_PP_P(Polynomial('1 1 1 1 1'), Polynomial('1 1 1 1 1')).__str__(simple=True), '2 2 2 2 2')
        self.assertEqual(ADD_PP_P(Polynomial('2 1 1 1 1'), Polynomial('-1 1 1 1 1')).__str__(simple=True), '1 2 2 2 2')
        self.assertEqual(ADD_PP_P(Polynomial('228/2 1 1 1 1'), Polynomial('-1/2 1 1 1 1')).__str__(simple=True),
                         '227/2 2 2 2 2')
        self.assertEqual(ADD_PP_P(Polynomial('228/2 1 1'), Polynomial('-1/2 1 1')).__str__(simple=True), '227/2 2 2')
        self.assertEqual(ADD_PP_P(Polynomial('0'), Polynomial('0')).__str__(simple=True), '0')

        self.assertEqual(ADD_PP_P(Polynomial('228/123 1 1'), Polynomial('-1/246 1 1')).__str__(simple=True), '455/246 2 2')
        self.assertEqual(ADD_PP_P(Polynomial('1 1 1 1 1'), Polynomial('1 1 1 1')).__str__(simple=True), '1 2 2 2 2')

        self.assertEqual(ADD_PP_P(Polynomial('1 1 1 1 1'), Polynomial('1')).__str__(simple=True), '1 1 1 1 2')
        self.assertEqual(ADD_PP_P(Polynomial('-1'), Polynomial('1 1 1 1 1')).__str__(simple=True), '1 1 1 1 0')

    def test_SUB_PP_P(self):
        self.assertEqual(SUB_PP_P(Polynomial('3'), Polynomial('1')).__str__(simple=True), '2')
        self.assertEqual(SUB_PP_P(Polynomial('2 1 1 1 1'), Polynomial('1 1 1 1 1')).__str__(simple=True), '1 0 0 0 0')
        self.assertEqual(SUB_PP_P(Polynomial('1 1 1 1 1'),Polynomial('1 1 1 1 1')).__str__(simple=True),'0')

    def test_MUL_PQ_Q(self):
        self.assertEqual(MUL_PQ_Q(Polynomial('1 1 1 1'), RNumber('1')).__str__(simple=True), '1 1 1 1')
        self.assertEqual(MUL_PQ_Q(Polynomial('1 1 1 1'), RNumber('2')).__str__(simple=True), '2 2 2 2')
        self.assertEqual(MUL_PQ_Q(Polynomial('1/2 1/2 1/2 1/2'), RNumber('2')).__str__(simple=True), '2/2 2/2 2/2 2/2')
        self.assertEqual(MUL_PQ_Q(Polynomial('1 1 1 1'), RNumber('-1')).__str__(simple=True), '-1 -1 -1 -1')
        self.assertEqual(MUL_PQ_Q(Polynomial('1 1 1 1'), RNumber('0000000')).__str__(simple=True), '0')
        self.assertEqual(MUL_PQ_Q(Polynomial('9 8 7 6'), RNumber('1/10')).__str__(simple=True), '9/10 8/10 7/10 6/10')
        self.assertEqual(MUL_PQ_Q(Polynomial('1 1 1 1'), RNumber('1')).__str__(simple=True), '1 1 1 1')

    def test_LED_P_Q(self):
        self.assertEqual(LED_P_Q(Polynomial('0')).__str__(),'0')
        self.assertEqual(LED_P_Q(Polynomial('1 2 3')).__str__(), '1')
        self.assertEqual(LED_P_Q(Polynomial('-1')).__str__(), '-1')
        self.assertEqual(LED_P_Q(Polynomial('12345676543456765432345676543 0 0 0 0 0 0 0 0 0 0 0 0')).__str__(), '12345676543456765432345676543')
        self.assertEqual(LED_P_Q(Polynomial('0 0 0 -12415637165 0 0 0 0 0 ')).__str__(), '-12415637165')
        self.assertEqual(LED_P_Q(Polynomial('1 1/56748574854345456787654 1 1 1 1 ')).__str__(), '1')
        self.assertEqual(LED_P_Q(Polynomial('1/56748574854345456787654')).__str__(), '1/56748574854345456787654')

    def test_DEG_P_N(self):
        self.assertEqual(DEG_P_N(Polynomial('1 1 1 1')), 3)
        self.assertEqual(DEG_P_N(Polynomial('1 2 3 5 1')), 4)
        self.assertEqual(DEG_P_N(Polynomial('0')), 0)
        self.assertEqual(DEG_P_N(Polynomial('11231 1')), 1)
        self.assertEqual(DEG_P_N(Polynomial('-1/2 1/2 1/2 1')), 3)

    def test_FAC_P_Q(self):
        self.assertEqual(FAC_P_Q(Polynomial('1 1 1 1 1')).__str__(), '1')
        self.assertEqual(FAC_P_Q(Polynomial('1/2 1/2 1/2')).__str__(), '1/2')
        self.assertEqual(FAC_P_Q(Polynomial('1 1/2 1/3')).__str__(), '1/6')
        self.assertEqual(FAC_P_Q(Polynomial('1 -1/2 1/4')).__str__(), '1/4')
        self.assertEqual(FAC_P_Q(Polynomial('12514/987654 77715/99615')).__str__(), str(gcd(12514,77715))+'/'+str(lcm(987654,99615)))
        self.assertEqual(FAC_P_Q(Polynomial('1 1 0 1 1')).__str__(), '1')

    def test_DER_P_P(self):
        self.assertEqual(DER_P_P(Polynomial('1 1 1')).__str__(simple=True),'2 1')
        self.assertEqual(DER_P_P(Polynomial('1 0 1')).__str__(simple=True),'2 0')
        self.assertEqual(DER_P_P(Polynomial('1 0 0')).__str__(simple=True),'2 0')
        self.assertEqual(DER_P_P(Polynomial('-12514/987654 1 1')).__str__(simple=True),'-25028/987654 1')
        self.assertEqual(DER_P_P(Polynomial('-1/12 0 0 0 0 0 0 0 0 0 0 0 0')).__str__(simple=True),'-12/12 0 0 0 0 0 0 0 0 0 0 0')
        self.assertEqual(DER_P_P(Polynomial('228')).__str__(simple=True), '0')

    def test_MUL_Pxk_P(self):
        self.assertEqual(MUL_Pxk_P(Polynomial('1 1'), 0).__str__(simple=True),'1 1')
        self.assertEqual(MUL_Pxk_P(Polynomial('0'), 3).__str__(simple=True),'0')
        self.assertEqual(MUL_Pxk_P(Polynomial('10 1'), 2).__str__(simple=True),'10 1 0 0')
        self.assertEqual(MUL_Pxk_P(Polynomial('1 1'), 0).__str__(simple=True),'1 1')
        self.assertEqual(MUL_Pxk_P(Polynomial('0'), 0).__str__(simple=True), '0')
        self.assertEqual(MUL_Pxk_P(Polynomial('1 0 0 0 0'), 0).__str__(simple=True), '1 0 0 0 0')

def Ptest(name:list):
    suite = unittest.TestSuite()
    for i in name:
        suite.addTest(TestPolynomials('test_'+i))
    runner = unittest.TextTestRunner()
    runner.run(suite)
