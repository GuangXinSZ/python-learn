# python 如果函数存在就可以调用 不存在就不能调用
def foo ():
  print('i am foo')
  bar()

def bar ():
  print('bar')

def test1 ():
  print('is test1')

def test2 (func):
  print(func)
  func()


test2(test1)