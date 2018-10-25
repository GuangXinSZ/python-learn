 
import time

def consumer(name):
  print("%s准备吃包子" %name)
  while True:
    baozi = yield
    print("包子[%s]来了" %name)
res = consumer('刘')

res.__next__()
# res.__next__()
