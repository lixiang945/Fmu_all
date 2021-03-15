#BeautifulReport的使用
# coding:utf-8

import os
import time
import unittest

from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    # unittest.main()
    #默认读取路径及读取的文件
    discover = unittest.defaultTestLoader.discover(os.path.dirname(__file__), pattern='test_case.py')
    #设置时间格式
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    #报告名称、报告报错的文件名及保存位置
    BeautifulReport(discover).report(description='TestReport', filename=f'{now}_PaaSTest.html', report_dir=r'./TestReport')