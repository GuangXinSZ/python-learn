
# 1: 导入包 先执行__init__.py文件
# 2: __init__文件夹里面设置 __all__ = [] 来限制包导出
# 3： import t 是导入文件
import t
from t import *
from t import *

print(ctx_1.a)
print(t.sys.path)