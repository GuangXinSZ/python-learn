import time

# 需求：写一个装饰器计算test1&test2的运行时间且不能改变运行方法
def timmer(func):
    def bear(*args, **kwargs):
      start_time = time.time()
      # 接受参数
      func(*args, **kwargs)
      stop_time = time.time()
      print('the fun run time is %s' %(start_time - stop_time))
    return bear

# @timmer = test1 = timmer(test1)
@timmer
def test1():
  time.sleep(3)
  print('in the test1')

@timmer
def test2(a, b):
  time.sleep(3)
  print('in the test2', a, b)

# test1 = timmer(test1)
test1()
test2('name','22')