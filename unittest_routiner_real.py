# тестирование модуля routiner_real.py 
# предназначен для работы с:
#     - числами с плавающей точкой;
#     - с дробями вида   x a/b (х - целая часть, a - числитель, b - знаменатель)

import unittest
from routiner_real import calc

class test_Real_Numbers(unittest.TestCase):

    # целое число и число с плавающей точкой
    def test_1(self):
        print('.test_1     ::  целое число и число с плавающей точкой')
        result_sum = calc('1.2', '2', '+')
        result_diff = calc('1.2', '2', '-')
        result_mult = calc('1.2', '2', '*')
        result_divide = calc('1.2', '2', '/')
        self.assertEqual(result_sum, "3.2")
        self.assertEqual(result_diff, "-0.8")
        self.assertEqual(result_mult, "2.4")
        self.assertEqual(result_divide, "0.6")

    # число с плавающей точкой и целое число
    def test_2(self):
        print('test_2     ::  число с плавающей точкой и целое число')
        result_sum = calc('2', '1.2', '+')
        result_diff = calc('2', '1.2', '-')
        result_mult = calc('2', '1.2', '*')
        result_divide = calc('2', '1.2', '/')
        self.assertEqual(result_sum, "3.2")
        self.assertEqual(result_diff, "0.8")
        self.assertEqual(result_mult, "2.4")
        self.assertEqual(result_divide, "1.7")

    # два числа с плавающей точкой
    def test_3(self):
        print('test_3     ::  два числа с плавающей точкой')
        result_sum = calc('2.3', '1.2', '+')
        result_diff = calc('2.3', '1.2', '-')
        result_mult = calc('2.3', '1.2', '*')
        result_divide = calc('2.3', '1.2', '/')
        self.assertEqual(result_sum, "3.5")
        self.assertEqual(result_diff, "1.1")
        self.assertEqual(result_mult, "2.8")
        self.assertEqual(result_divide, "1.9")

      # целое число и отрицательное число с плавающей точкой
    def test_4(self):
        print('test_4     ::  целое число и отрицательное число с плавающей точкой')
        result_sum = calc('-1.2', '2', '+')
        result_diff = calc('-1.2', '2', '-')
        result_mult = calc('-1.2', '2', '*')
        result_divide = calc('-1.2', '2', '/')
        self.assertEqual(result_sum, "0.8")
        self.assertEqual(result_diff, "-3.2")
        self.assertEqual(result_mult, "-2.4")
        self.assertEqual(result_divide, "-0.6")

    # число с плавающей точкой и отрицательное целое число
    def test_5(self):
        print('test_5     ::  число с плавающей точкой и отрицательное целое число')
        result_sum = calc('-2', '1.2', '+')
        result_diff = calc('-2', '1.2', '-')
        result_mult = calc('-2', '1.2', '*')
        result_divide = calc('-2', '1.2', '/')
        self.assertEqual(result_sum, "-0.8")
        self.assertEqual(result_diff, "-3.2")
        self.assertEqual(result_mult, "-2.4")
        self.assertEqual(result_divide, "-1.7")

    # два числа с плавающей точкой, одно отрицательное
    def test_6(self):
        print('test_6     ::  два числа с плавающей точкой, одно отрицательное')
        result_sum = calc('-2.3', '1.2', '+')
        result_diff = calc('-2.3', '1.2', '-')
        result_mult = calc('-2.3', '1.2', '*')
        result_divide = calc('-2.3', '1.2', '/')
        self.assertEqual(result_sum, "-1.1")
        self.assertEqual(result_diff, "-3.5")
        self.assertEqual(result_mult, "-2.8")
        self.assertEqual(result_divide, "-1.9")  

    # число с плавающей точкой и ноль
    def test_7(self):
        print('test_7     ::  число с плавающей точкой и ноль')
        result_sum = calc('0', '1.2', '+')
        result_diff = calc('-2.3', '0', '-')
        result_mult = calc('0', '1.2', '*')
        result_divide = calc('-2.3', '0', '/')
        self.assertEqual(result_sum, "1.2")
        self.assertEqual(result_diff, "-2.3")
        self.assertEqual(result_mult, "0.0")
        self.assertEqual(result_divide, "Error!!! Division by zero.")

    # обыкновенная дробь с целой частью и обыкновенная дробь
    def test_8(self):
        print('test_8     ::  обыкновенная дробь с целой частью и обыкновенная дробь')
        result_sum = calc('4 3/5', '1/5', '+')
        result_diff = calc('4 3/5', '1/5', '-')
        result_mult = calc('4 3/5', '1/5', '*')
        result_divide = calc('4 3/5', '1/5', '/')
        self.assertEqual(result_sum, "4 4/5")
        self.assertEqual(result_diff, "4 2/5")
        self.assertEqual(result_mult, "23/25")
        self.assertEqual(result_divide, "23")

    # обыкновенная дробь с целой частью и отрицательная обыкновенная дробь
    def test_9(self):
        print('test_9     ::  обыкновенная дробь с целой частью и отрицательная обыкновенная дробь')
        result_sum = calc('4 3/5', '-1/5', '+')
        result_diff = calc('4 3/5', '-1/5', '-')
        result_mult = calc('4 3/5', '-1/5', '*')
        result_divide = calc('4 3/5', '-1/5', '/')
        self.assertEqual(result_sum, "4 2/5")
        self.assertEqual(result_diff, "4 4/5")
        self.assertEqual(result_mult, "-23/25")
        self.assertEqual(result_divide, "-23")

    # обыкновенная дробь и целое число
    def test_10(self):
        print('test_10    ::  обыкновенная дробь и целое число')
        result_sum = calc('4', '1/5', '+')
        result_diff = calc('4', '1/5', '-')
        result_mult = calc('4', '1/5', '*')
        result_divide = calc('4', '1/5', '/')
        self.assertEqual(result_sum, "4 1/5")
        self.assertEqual(result_diff, "3 4/5")
        self.assertEqual(result_mult, "4/5")
        self.assertEqual(result_divide, "20")

    # обыкновенная дробь и обыкновенная дробь с нулевым знаменателем
    def test_zero(self):
        print('test_zero  ::  обыкновенная дробь и обыкновенная дробь с нулевым знаменателем')
        result_sum = calc('3/5', '1/0', '+')
        result_diff = calc('3/0', '1/5', '-')
        result_mult = calc('3/0', '1/0', '*')
        result_divide = calc('3/4', '0/2', '/')
        self.assertEqual(result_sum, "Error! Division by zero.")
        self.assertEqual(result_diff, "Error! Division by zero.")
        self.assertEqual(result_mult, "Error! Division by zero.")
        self.assertEqual(result_divide, "Error! Division by zero.")


if __name__ == '__main__':
    unittest.main()