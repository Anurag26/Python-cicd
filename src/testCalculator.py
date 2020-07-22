# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 18:22:59 2020

@author: sanur
"""


import unittest
from calculator import calculator

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(5, calculator("+",2,3))
        self.assertEqual(4, calculator("+",2,2))
    
    def test1(self):
        self.assertEqual(5, calculator("+",2,3))
        self.assertEqual(7, calculator("+",5,2))
        
    def test2(self):
        self.assertEqual(9, calculator("+",8,1))
        self.assertEqual(3, calculator("-",7,4))
        
if __name__ == '__main__':
    unittest.main()        
        