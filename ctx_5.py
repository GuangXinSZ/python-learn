# 循环

# 循环语句

# while for
counter = 1
while counter < 2 :
    counter +=1
    print(counter)
else :
    print('读取完成')

# for循环
a = [['apple', 'orange', 'banana'], (1, 2, 3)]
for x in a :
    for y in x :
        print(y)
b = [1, 2, 3]
for x in b :
    if x == 2 :
        break
    print(x)
else :
    print('输出成功')