import unittest
from math import gcd
from Polynomials import *


def lcm(a, b):
    return a * b // gcd(a, b)


# python Polynomials_test.py -v

Plist = ['ADD_PP_P', 'SUB_PP_P', 'MUL_PQ_Q', 'LED_P_Q', 'DEG_P_N', 'FAC_P_Q', 'DER_P_P', 'MUL_Pxk_P', 'MUL_PP_P', 'DIV_PP_P', 'MOD_PP_P', 'GCF_PP_P', 'NMR_P_P']


class TestPolynomials(unittest.TestCase):
    def test_ADD_PP_P(self):
        self.assertEqual(ADD_PP_P(Polynomial('1 1 1 1 1'), Polynomial('1 1 1 1 1')).__str__(simple=True), '2 2 2 2 2')
        self.assertEqual(ADD_PP_P(Polynomial('2 1 1 1 1'), Polynomial('-1 1 1 1 1')).__str__(simple=True), '1 2 2 2 2')
        self.assertEqual(ADD_PP_P(Polynomial('228/2 1 1 1 1'), Polynomial('-1/2 1 1 1 1')).__str__(simple=True),
                         '227/2 2 2 2 2')
        self.assertEqual(ADD_PP_P(Polynomial('228/2 1 1'), Polynomial('-1/2 1 1')).__str__(simple=True), '227/2 2 2')
        self.assertEqual(ADD_PP_P(Polynomial('0'), Polynomial('0')).__str__(simple=True), '0')

        self.assertEqual(ADD_PP_P(Polynomial('228/123 1 1'), Polynomial('-1/246 1 1')).__str__(simple=True),
                         '455/246 2 2')
        self.assertEqual(ADD_PP_P(Polynomial('1 1 1 1 1'), Polynomial('1 1 1 1')).__str__(simple=True), '1 2 2 2 2')

        self.assertEqual(ADD_PP_P(Polynomial('1 1 1 1 1'), Polynomial('1')).__str__(simple=True), '1 1 1 1 2')
        self.assertEqual(ADD_PP_P(Polynomial('-1'), Polynomial('1 1 1 1 1')).__str__(simple=True), '1 1 1 1 0')

    def test_SUB_PP_P(self):
        self.assertEqual(SUB_PP_P(Polynomial('3'), Polynomial('1')).__str__(simple=True), '2')
        self.assertEqual(SUB_PP_P(Polynomial('2 1 1 1 1'), Polynomial('1 1 1 1 1')).__str__(simple=True), '1 0 0 0 0')
        self.assertEqual(SUB_PP_P(Polynomial('1 1 1 1 1'), Polynomial('1 1 1 1 1')).__str__(simple=True), '0')

    def test_MUL_PQ_Q(self):
        self.assertEqual(MUL_PQ_Q(Polynomial('1 1 1 1'), RNumber('1')).__str__(simple=True), '1 1 1 1')
        self.assertEqual(MUL_PQ_Q(Polynomial('1 1 1 1'), RNumber('2')).__str__(simple=True), '2 2 2 2')
        self.assertEqual(MUL_PQ_Q(Polynomial('1/2 1/2 1/2 1/2'), RNumber('2')).__str__(simple=True), '1 1 1 1')
        self.assertEqual(MUL_PQ_Q(Polynomial('1 1 1 1'), RNumber('-1')).__str__(simple=True), '-1 -1 -1 -1')
        self.assertEqual(MUL_PQ_Q(Polynomial('1 1 1 1'), RNumber('0000000')).__str__(simple=True), '0')
        self.assertEqual(MUL_PQ_Q(Polynomial('9 8 7 6'), RNumber('1/10')).__str__(simple=True), '9/10 4/5 7/10 3/5')
        self.assertEqual(MUL_PQ_Q(Polynomial('1 1 1 1'), RNumber('1')).__str__(simple=True), '1 1 1 1')

    def test_LED_P_Q(self):
        self.assertEqual(LED_P_Q(Polynomial('0')).__str__(), '0')
        self.assertEqual(LED_P_Q(Polynomial('1 2 3')).__str__(), '1')
        self.assertEqual(LED_P_Q(Polynomial('-1')).__str__(), '-1')
        self.assertEqual(LED_P_Q(Polynomial('12345676543456765432345676543 0 0 0 0 0 0 0 0 0 0 0 0')).__str__(),
                         '12345676543456765432345676543')
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
        self.assertEqual(FAC_P_Q(Polynomial('12514/987654 77715/99615')).__str__(),
                         str(gcd(12514, 77715)) + '/' + str(lcm(987654, 99615)))
        self.assertEqual(FAC_P_Q(Polynomial('1 1 0 1 1')).__str__(), '1')

    def test_DER_P_P(self):
        self.assertEqual(DER_P_P(Polynomial('1 1 1')).__str__(simple=True), '2 1')
        self.assertEqual(DER_P_P(Polynomial('1 0 1')).__str__(simple=True), '2 0')
        self.assertEqual(DER_P_P(Polynomial('1 0 0')).__str__(simple=True), '2 0')
        self.assertEqual(DER_P_P(Polynomial('-12514/987654 1 1')).__str__(simple=True), '-12514/493827 1')
        self.assertEqual(DER_P_P(Polynomial('-1/12 0 0 0 0 0 0 0 0 0 0 0 0')).__str__(simple=True),
                         '-1 0 0 0 0 0 0 0 0 0 0 0')
        self.assertEqual(DER_P_P(Polynomial('228')).__str__(simple=True), '0')

    def test_MUL_Pxk_P(self):
        self.assertEqual(MUL_Pxk_P(Polynomial('1 1'), 0).__str__(simple=True), '1 1')
        self.assertEqual(MUL_Pxk_P(Polynomial('0'), 3).__str__(simple=True), '0')
        self.assertEqual(MUL_Pxk_P(Polynomial('10 1'), 2).__str__(simple=True), '10 1 0 0')
        self.assertEqual(MUL_Pxk_P(Polynomial('1 1'), 0).__str__(simple=True), '1 1')
        self.assertEqual(MUL_Pxk_P(Polynomial('0'), 0).__str__(simple=True), '0')
        self.assertEqual(MUL_Pxk_P(Polynomial('1 0 0 0 0'), 0).__str__(simple=True), '1 0 0 0 0')

    def test_MUL_PP_P(self):
        self.assertEqual(MUL_PP_P(Polynomial('1 -3 0 6 -4'), Polynomial('1')).__str__(simple=True), '1 -3 0 6 -4')
        self.assertEqual(MUL_PP_P(Polynomial('1 -3 0 6 -4'), Polynomial('-1')).__str__(simple=True), '-1 3 0 -6 4')
        self.assertEqual(MUL_PP_P(Polynomial('1 2'), Polynomial('1 2')).__str__(simple=True), '1 4 4')
        self.assertEqual(MUL_PP_P(Polynomial('2 -11 19 -13 3'), Polynomial('0')).__str__(simple=True), '0')
        self.assertEqual(MUL_PP_P(Polynomial('1 5 -2 -6'), Polynomial('1 1')).__str__(simple=True), '1 6 3 -8 -6')
        self.assertEqual(MUL_PP_P(Polynomial('1 2'), Polynomial('1 -2')).__str__(simple=True), '1 0 -4')
        self.assertEqual(MUL_PP_P(Polynomial('1 1'), Polynomial('-1 1')).__str__(simple=True), '-1 0 1')
        self.assertEqual(MUL_PP_P(Polynomial('1 0 0 0 12681 3'), Polynomial('1 213 84984 -88')).__str__(simple=True), '1 213 84984 -88 12681 2701056 1077682743 -860976 -264')

    def test_DIV_PP_P(self):
        self.assertEqual(DIV_PP_P(Polynomial('1 -3 0 6 -4'), Polynomial('1 -1')).__str__(simple=True), '1 -2 -2 4')
        self.assertEqual(DIV_PP_P(Polynomial('2 -10 23 -22 -3'), Polynomial('1 -3 5')).__str__(simple=True), '2 -4 1')
        self.assertEqual(DIV_PP_P(Polynomial('10 3 -12 25 -2 5'), Polynomial('5 -1 2')).__str__(simple=True),
                         '2 1 -3 4')
        self.assertEqual(DIV_PP_P(Polynomial('2 -11 19 -13 3'), Polynomial('2 -3 1')).__str__(simple=True), '1 -4 3')
        self.assertEqual(DIV_PP_P(Polynomial('1 5 -2 -6'), Polynomial('1 1')).__str__(simple=True), '1 4 -6')
        self.assertEqual(DIV_PP_P(Polynomial('-6 5 17 -23 7'), Polynomial('-3 -2 7')).__str__(simple=True), '2 -3 1')
        self.assertEqual(DIV_PP_P(Polynomial('-3 -2 7'), Polynomial('-6 5 17 -23 7')).__str__(simple=True), '0')
        self.assertEqual(DIV_PP_P(Polynomial('3 4 5 6 2 7 9'), Polynomial('6 5 3 1 2 4 2')).__str__(simple=True), '1/2')
        self.assertEqual(
            DIV_PP_P(Polynomial('123 512 127 1236 -23 512 421 243231'), Polynomial('12 52 123 74 123 75 324 ')).__str__(
                simple=True), '41/4 -7/4')
        self.assertEqual(
            DIV_PP_P(Polynomial('123 512 127 1236 -23 512 421 243231'), Polynomial('1')).__str__(
                simple=True), '123 512 127 1236 -23 512 421 243231')
        self.assertRaises(ZeroDivisionError, DIV_PP_P, Polynomial('123 512 127 1236 -23 512 421 243231'),
                          Polynomial('0'))

    def test_MOD_PP_P(self):
        self.assertEqual(MOD_PP_P(Polynomial('1 -3 0 6 -4'), Polynomial('1 -1')).__str__(simple=True), '0')
        self.assertEqual(MOD_PP_P(Polynomial('2 -10 23 -22 -3'), Polynomial('1 -3 5')).__str__(simple=True), '1 -8')
        self.assertEqual(MOD_PP_P(Polynomial('10 3 -12 25 -2 5'), Polynomial('5 -1 2')).__str__(simple=True), '8 -3')
        self.assertEqual(MOD_PP_P(Polynomial('2 -11 19 -13 3'), Polynomial('2 -3 1')).__str__(simple=True), '0')
        self.assertEqual(MOD_PP_P(Polynomial('1 5 -2 -6'), Polynomial('1 1')).__str__(simple=True), '0')
        self.assertEqual(MOD_PP_P(Polynomial('-6 5 17 -23 7'), Polynomial('-3 -2 7')).__str__(simple=True), '0')
        self.assertEqual(MOD_PP_P(Polynomial(' -23 7'), Polynomial('1')).__str__(simple=True), '0')
        self.assertEqual(
            MOD_PP_P(Polynomial('123 512 127 1236 -23 512 421 243231'), Polynomial('12 52 123 74 123 75 324 ')).__str__(
                simple=True), '-4171/4 2771/4 -4617/4 -83/2 -11075/4 243798')
        self.assertRaises(ZeroDivisionError, MOD_PP_P, Polynomial('123 512 127 1236 -23 512 421 243231'),
                          Polynomial('0'))

    def test_GCF_PP_P(self):
        self.assertEqual(GCF_PP_P(Polynomial('1 -5 9 -7 5 -3'), Polynomial('1 -2 2 -1 1')).__str__(simple=True), '1')
        self.assertEqual(GCF_PP_P(Polynomial('1 -1 -5 -3'), Polynomial('1 1 -12')).__str__(simple=True), '9 -27')
        self.assertEqual(GCF_PP_P(Polynomial('3 -1 2 -4'), Polynomial('1 -2 0 1')).__str__(simple=True), '59/25 -59/25')
        self.assertEqual(GCF_PP_P(Polynomial('3 -1 2 -4'), Polynomial('1 -2 1')).__str__(simple=True), '9 -9')
        self.assertEqual(GCF_PP_P(Polynomial('3 -1 2 -4'), Polynomial('1 -2 1')).__str__(simple=True), '9 -9')
        # self.assertEqual(GCF_PP_P(Polynomial(''), Polynomial('')).__str__(simple=True), '')
        # self.assertEqual(GCF_PP_P(Polynomial(''), Polynomial('')).__str__(simple=True), '')
        # self.assertEqual(GCF_PP_P(Polynomial(''), Polynomial('')).__str__(simple=True), '')

    def test_NMR_P_P(self):
        self.assertEqual(NMR_P_P(Polynomial('1 2 1')).__str__(simple=True), '1 1')
        self.assertEqual(NMR_P_P(Polynomial('4 28 49')).__str__(simple=True), '2 7')
        self.assertEqual(NMR_P_P(Polynomial('64 1536 9216')).__str__(simple=True), '64 768')
        self.assertEqual(NMR_P_P(Polynomial('1 18 108 216')).__str__(simple=True), '1 6')
        # self.assertEqual(NMR_P_P(Polynomial('')).__str__(simple=True), '')
        # self.assertEqual(NMR_P_P(Polynomial('')).__str__(simple=True), '')


def Ptest(name: list):
    suite = unittest.TestSuite()
    for i in name:
        suite.addTest(TestPolynomials('test_' + i))
    runner = unittest.TextTestRunner()
    runner.run(suite)
