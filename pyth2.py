#Разинков Даниил Николаевич Группа 44-22-114 Вариант 19 Задание 2
import unittest

class CalculationTest(unittest.TestCase):
    def test_case_x_less_than_1(self):
        result = calculate_value(0.5)
        self.assertEqual(result, math.sin(0.5 + 0.5 ** 2))

    def test_case_x_greater_than_or_equal_to_1(self):
        result = calculate_value(1.5)
        self.assertEqual(result, 1.5 * math.sqrt(1.5 + 0.3))

if __name__ == '__main__':
    unittest.main()
