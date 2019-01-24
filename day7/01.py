import time

def timmer(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    func()
    stop_time = time.time()
    print('the fun run time is %s' %(start_time - stop_time))
  return wrapper

@timmer
def test1():
  time.sleep(3)
  print('123')

# test1()
def bar():
  print('bar')

def foo():
  print('foo')
  bar()
foo()