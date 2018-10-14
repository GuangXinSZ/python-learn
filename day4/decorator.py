import time

# 装饰器
def timer(func):n 
  def wrapper(*args, **kwargs):
    start_time = time.time()
    func()
    stop_time = time.time()
    print('the func run time is %s' %(stop_time-start_time))
  return wrapper
@timer

def test1():
  time.sleep(3)
  print('in the test')

test1()