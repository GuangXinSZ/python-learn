import time

username = 'liu'
passwd = '123'

# 实现权限验证
def auth(fun):
  def wrapper(*args, **kwargs):
    user = input('Username: ').strip()
    password = input('Password: ').strip()

    if user == username and password == passwd:
      print('验证成功!')
      fun(*args, **kwargs)
    else:
      exit('验证失败')
  
  return wrapper

@auth
def test1():
  print('进入1')

@auth
def test2():
  print('进入2')

test1()
test2()
