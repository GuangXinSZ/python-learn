import time

username = 'liu'
password = '123'

def auth(func):
  def outer_wrapper():
     def wrapper(*args, **kwargs):
      Username = input("please input Username:").strip()
      Password = input("please input Password:").strip()

      if Username == username and Password == password:
        print("welcome")
        res = func(*args, **kwargs)
        return res
      else:
        exit("账号或者密码错误") 

    return wrapper
  return outer_wrapper
 
@auth
def test1(auth_type="ldap"):
  print("登录成功")
  return 'hello world'

ret = test1()
print(ret)