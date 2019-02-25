__author__ = "xin"
# 引入全部*  单个引入
# from module_alex import *
# import module_alex

# def logger():
#   print('123')

# logger()
# module_alex.logger()
import sys, os
# 获取文件路径名
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 导入优化
from module_alex import logger

# module_alex.say_hello()

logger()