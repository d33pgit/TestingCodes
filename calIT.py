# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 14:17:24 2025

@author: SBUP
"""

import unittest
from cal import calculate

class TestCalculatorTesting(unittest.TestCase):
    def test_add(self):
        result=calculate(5,3,'add')
        self.assertEqual(result,8)
    def test_subtract(self):
        result=calculate(5,3,'sub')
        self.assertEqual(result,2)
    def test_mul(self):
        result=calculate(5,3,'mul')
        self.assertEqual(result,15)
    def test_div(self):
        res=calculate(20,5,'div')
        self.assertEqual(res,4)
    def test_invalid(self):
        with self.assertRaises(ValueError):
            calculate(4,2,'mod')
if __name__=="__main__":
    unittest.main()