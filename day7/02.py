def bar():
  print('hello bar')

def test(fun):
  fun()

#嵌套函数
def foo():
  print('in the foo')
  def getContent():
    print('in the content')
  getContent()

foo()