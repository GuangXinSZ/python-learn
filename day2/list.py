list_1 = [1, 2, 3, 4, 4, 5, 7]
list_1 = set(list_1) # 去重
list_2 = set([23, 23, 24, 5])
list_3 = set([1, 2, 3])
list_4 = set([4, 5, 6])

# 得到交集
print(list_1.intersection(list_2))

# 并集
print(list_1.union(list_2))

# 差集 in list_1 but not in list_2
print(list_1.difference(list_2))
 
# 子集
print(list_3.issubset(list_1))
print(list_1.issuperset(list_3)) # 反过来

# 反向差集 list_1 跟 list_2都没的参数进行返回
print(list_1.symmetric_difference(list_2))

# 存不存在交集 没有返回True 有返回False
print(list_3.isdisjoint(list_4))

# 交集 简写
print(list_1 & list_2)
# 并集
print(list_1 | list_2)
# 差集 in list_1 but not in list_2
print(list_1 - list_2)
# 反向差集 list_1 跟 list_2都没的参数进行返回
print(list_1 ^ list_2)