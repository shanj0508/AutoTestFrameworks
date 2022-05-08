'''
    基于套件的形态管理测试用例
'''
import os
import time
import unittest

# 创建套件
# from HTMLTestRunner import HTMLTestRunner
from HTMLTestReportCN import HTMLTestRunner

# 定义测试用例文件的获取路径
path = '../test_cases/'
discover = unittest.defaultTestLoader.discover(start_dir=path, pattern='test*.py')

# 配置测试报告信息
# 时间戳
t = time.strftime('%Y-%m-%d_%H_%M_%S')
# 测试执行者：在HTMLTestReport报告中专属参数
report_tester = '张三'
# 保存路径
report_dir = './report/'
# 测试报告的title
report_title = '张三的测试报告'
# 描述
report_description = '这是测试报告的描述'
# 测试报告文件
report_file = report_dir + t + 'reportCN.html'
# 生成路径
if not os.path.exists(report_dir):
    os.mkdir(report_dir)

# 生成HTMLTestRunner测试报告，本质意义上就是写入一个文件
with open(report_file, 'wb') as file:
    runner = HTMLTestRunner(stream=file, title=report_title,
                            description=report_description, verbosity=2, tester=report_tester)
    runner.run(discover)

# 运行套件内的测试用例：默认运行器,verbosity是日志等级，0-1-2
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(discover)
