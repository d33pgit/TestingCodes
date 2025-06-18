import unittest

def Sorted_list(list):
    return sorted(list)
class ass1_3(unittest.TestCase):
    def sorting_equal(self):
        self.assertEqual(Sorted_list([25,1,0,2]),[0,1,2,25])
if __name__== '__main__':
    unittest.main()



