__author__ = 'LiuGuangXin'

def test(x, y=1):
  print(x)
  print(y)

def test2(*args): #args = tupe([1, 2, 3])
  print(args)

def test3(**kwargs): #传进去的参数是一个Object
  print(kwargs['name'])

def test4(name, age=18, **kwargs):
  print(name)
  print(age)
  print(kwargs)

# test(1)
# test2(*[1, 2, 3])
# test3(name='alex')
# test3(**{'name':'alex', 'age': 8})

test4('alex', sex="m", hobby="打球", age="1")

def calc(n):
  print(n)
  if int(n/2) > 0:
    return calc(int(n/2))
calc(10)

# 高阶函数
def add(a, b ,f):
  return f(a)+f(b)

res = add(3, -6, abs)
print(res)