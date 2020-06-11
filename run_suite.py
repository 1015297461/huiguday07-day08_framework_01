# 1.导包
import time
import unittest
from BeautifulReport import BeautifulReport

# 2.组织测试套件

suite = unittest.TestLoader().discover("script", "test*.py")

# 3.定义测试报告
# report_file = "{}-report.html". format(time.strftime("%Y%m%d%H%M%S"))

# 使用beautiful批量
BeautifulReport(suite).report(filename="report_file", description="TpshopAPI", report_dir="./report")

