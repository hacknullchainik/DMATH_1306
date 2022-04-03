import unittest
from Dtypes import *
from math import gcd, lcm
from Polynomials import *
# python Polynomials_test.py -v

Plist = ['ADD_PP_P']


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



def Ptest(name:list):
    suite = unittest.TestSuite()
    for i in name:
        suite.addTest(TestPolynomials('test_'+i))
    runner = unittest.TextTestRunner()
    runner.run(suite)
