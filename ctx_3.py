ACCOUNT = 'liu'
PASSWORD = '1234'

print('please input account')
user_account = input()

print('please input password')
user_password = input()

if ACCOUNT == user_account and PASSWORD == user_password : 
    print('登录成功')
else :
    print('失败')