
import unittest


from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    test_dir=r'D:\HTMLTestRunner_PY3\test_case' # 测试用例的路径，改成自己的即可
    suite = unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='Test_*.py') #查找上面路径里所有以Test_开头的文件作为测试集
    f = open('testresult.html', 'wb')

    runner = HTMLTestRunner(
            stream=f,
            title='测试报告',
            description='计算器demo'
    )
    runner.run(discover)
