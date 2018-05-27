import unittest

from Calc import Calc


class TestCalc(unittest.TestCase):
    '''计算器模块2'''
    def setUp(self):
        print("测试开始")
        self.cal = Calc()  # 在这里实例化

    def test_add(self):
        '''计算器加法模块2'''
        self.assertEqual(self.cal.add(1, 2), 3, 'test add1 failed')
        self.assertNotEquals(self.cal.add(1, 4), 4, 'test add2 failed')
        print("test_add pass")

    # @unittest.skip("暂时不测")
    def test_minus(self):
        '''计算器减法模块2'''
        self.assertEqual(self.cal.minus(1, 2), -1, 'test minus1 failed')
        self.assertEqual(self.cal.minus(3, 2), 1, 'test minus2 failed')
        print("test_minus pass")

    def test_divide(self):
        """计算器除法法模块2"""
        self.assertEqual(self.cal.divide(6, 2), 3, 'test divide1 failed')
        self.assertEqual(self.cal.divide(3, 2), 1, 'test divide2 failed')

    def test_multiple(self):
        """计算器乘法模块2"""
        self.assertEqual(self.cal.multiple(6, 2), 12, 'test multiple1 failed')
        self.assertEqual(self.cal.multiple(3, 2), 6, 'test multiple2 failed')
    def tearDown(self):
        print("测试结束")


if __name__ == '__main__':
    unittest.main()
