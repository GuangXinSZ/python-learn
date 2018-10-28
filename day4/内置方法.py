import time

b = bytearray("abcde", encoding="utf-8")
# print(all([1, -5, 2]))
# print(any([0, 1]))
# b[0] = 98
# filter过滤您想要的数据 lambda函数
# sorted 排序 根据item or  key = lambda x: x[1]
res = filter(lambda n: n > 5, range(10))

# def test():
#   local_var = 333
#   print(locals())
# test()

a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']
# zip合并两数组
for i in zip(a, b):
  print(i)