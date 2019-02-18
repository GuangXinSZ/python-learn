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
      res = fun(*args, **kwargs)
      return res
    else:
      exit('验证失败')
  
  return wrapper

@auth
def test1():
  print('进入1')
  return 'form home'

@auth
def test2():
  print('进入2')

value = test1()
print(value)
test2()
