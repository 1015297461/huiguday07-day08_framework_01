# 1.导包
import os
import time
import unittest
from BeautifulReport import BeautifulReport

# 2.组织测试套件
run_path = os.path.dirname(os.path.abspath(__file__))

suite = unittest.TestLoader().discover(run_path + "/script", "test*.py")

# 3.定义测试报告
# report_file = "{}-report.html". format(time.strftime("%Y%m%d%H%M%S"))


# 使用beautiful批量
file = "report.html"
BeautifulReport(suite).report(filename=file, description="TpshopAPI", report_dir=run_path + "/report")

