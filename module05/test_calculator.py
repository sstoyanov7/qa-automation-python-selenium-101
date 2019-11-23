import unittest
from datetime import datetime

import calculator


class CalculatorTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass executes only once. CREATE DATABASE;")
        print("")

    def setUp(self):
        print("    setUp executes before every test method!")

    def tearDown(self):
        print("    tearDown executes after every test method!")

    @classmethod
    def tearDownClass(cls):
        print("")
        print("tearDownClass executes only once. DROP DATABASE;")

    def test_add(self):
        self.assertEqual(calculator.add(4, 4), 8)
    def test_add_positive_to_negative(self):
        self.assertEqual(calculator.add(4, -4), 0)
    def test_add_not_equal(self):
        self.assertNotEqual(calculator.add(4, 4), 10)
    def test_add_positive_to_zero(self):
        self.assertEqual(calculator.add(42, 0), 42)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(4, 3), 1)
    def test_subtract_positive_to_negative(self):
        self.assertEqual(calculator.subtract(4, -4), 8)
    def test_subtract_not_equal(self):
        self.assertNotEqual(calculator.subtract(4, 4), 2)
    def test_subtract_positive_to_zero(self):
        self.assertEqual(calculator.subtract(42, 0), 42)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(5, 5), 25)
    def test_multiply_by_zero(self):
        self.assertEqual(calculator.multiply(5, 0), 0)
    def test_multiply_positive_to_negative(self):
        self.assertEqual(calculator.multiply(3, -5), -15)
    def test_multiply_negative_to_negative(self):
        self.assertEqual(calculator.multiply(-3, -5), 15)

    def test_divide(self):
        self.assertEqual(calculator.divide(5, 5), 1)
    def test_divide_by_one(self):
        self.assertEqual(calculator.divide(5, 1), 5)
    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, calculator.divide, 5, 0)
    def test_divide_positive_to_negative(self):
        self.assertEqual(calculator.divide(15, -5), -3)
    def test_divide_negative_to_negative(self):
        self.assertEqual(calculator.divide(-15, -3), 5)


class FlakyTest(unittest.TestCase):
    '''
        Execute this several times quickly to make it fail!
    '''

    def do_fail(self):
        if datetime.now().second % 3 == 0:
            raise Exception('I am a flaky test')

    def test_myself(self):
        self.do_fail()


if __name__ == "__main__":
    unittest.main()
