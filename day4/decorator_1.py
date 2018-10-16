import time

def deco(func):
  start_time = time.time()
  func()
  stop_time = time.time()
  print('the func run time is %s' %(stop_time-start_time))

def test1():
  time.sleep(3)
  print('test1')

def test2():
  time.sleep(3)
  print('test2')

