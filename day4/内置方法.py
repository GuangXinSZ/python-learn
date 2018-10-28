import time

b = bytearray("abcde", encoding="utf-8")
# print(all([1, -5, 2]))
# print(any([0, 1]))
# b[0] = 98
# filter过滤您想要的数据 lambda函数

res = filter(lambda n: n > 5, range(10))
for i in res:
  print(i)