import unittest

def is_even(n):
    return n%2 == 0
       
    
class ass1_4(unittest.TestCase):
    def test_even_normal(self):
        self.assertTrue(is_even(4))
    def test_even_string(self):
        self.assertTrue(is_even('B'))
    
if __name__ == "__main__":
    unittest.main()
    