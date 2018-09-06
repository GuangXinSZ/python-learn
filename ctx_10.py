import sys
import os

# print(sys.path) 打印环境变量
# print(sys.argv) 文件绝对路径
# print(os.system('dir'))  输出目录文件夹不会赋值
# os.mkdir() 创建文件夹
cmd_res = os.popen("dir").read() # 必须通过read()去读取才能赋值
print(cmd_res)

