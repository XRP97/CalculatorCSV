import unittest

from Calculator import Calculator
from CsvReader import Csv1


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_add = Csv1('addition.csv').data
        for row0 in test_add:
            self.result = int(row0['Result'])
            self.assertEqual(self.calculator.add(int(row0['Value 1']), int(row0['Value 2'])), int(row0['Result']))
            self.assertEqual(self.calculator.result, int(row0['Result']))

    def test_subtraction(self):
        test_sub = Csv1('subtraction.csv').data
        for row1 in test_sub:
            self.result = int(row1['Result'])
            self.assertEqual(self.calculator.subtract(int(row1['Value 1']), int(row1['Value 2'])), int(row1['Result']))
            self.assertEqual(self.calculator.result, int(row1['Result']))

    def test_division(self):
        test_div = Csv1('division.csv').data
        for row2 in test_div:
            self.result = int(float(row2['Result']))
            self.assertEqual(self.calculator.divide(int(float(row2['Value 1'])), int(float(row2['Value 2']))),
                             int(float(row2['Result'])))
            self.assertEqual(self.calculator.result, int(float(row2['Result'])))

    def test_multiplication(self):
        test_multiply = Csv1('multiplication.csv').data
        for row3 in test_multiply:
            self.result = int(float(row3['Result']))
            self.assertEqual(self.calculator.multiply(int(float(row3['Value 1'])), int(float(row3['Value 2']))),
                             int(float(row3['Result'])))
            self.assertEqual(self.calculator.result, int(float(row3['Result'])))

    def test_squareRoot(self):
        test_sqrt = Csv1('squareRoot.csv').data
        for row4 in test_sqrt:
            self.result = float(row4['Result'])
            self.assertEqual(self.calculator.square_root(float(row4['Value 1'])), float(row4['Result']))
            self.assertEqual(self.calculator.result, float(row4['Result']))

    def test_square(self):
        test_sqr = Csv1('square.csv').data
        for row5 in test_sqr:
            self.result = int(row5['Result'])
            self.assertEqual(self.calculator.square(int(row5['Value 1'])), int(row5['Result']))
            self.assertEqual(self.calculator.result, int(row5['Result']))


if __name__ == '__main__':
    unittest.main()
