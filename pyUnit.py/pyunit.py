import unittest
import calc
class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
    def test_Sub(self):
        self.assertEqual(calc.sub(10, 5), 5)
        self.assertNotEqual(calc.sub(10, 6), 7)
    def test_mul(self):
        self.assertEqual(calc.mul(6, 5), 30)
        self.assertEqual(calc.mul(3, 5), 15)
    def test_div(self):
        #self.assertEqual(calc.div(10, 5), 3)
        self.assertEqual(calc.div(10, 5), 2)
        self.assertEqual(calc.div(-1, 1), -1)
if __name__ == '__main__':
    unittest.main()