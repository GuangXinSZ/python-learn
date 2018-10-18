import time

def timer(func):
  def deco():
    start_time = time.time()
    func()
    stop_time = time.time()
    print('the func run time is %s' %(stop_time-start_time))
  
  return deco

@timer # test1 = timer(test1)
def test1():
  time.sleep(3)
  print('test1')

def test2():
  time.sleep(3)
  print('test2')

test1()