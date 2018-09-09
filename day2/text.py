import copy

persion = ['name', ['saveing', 1000]]
# 浅拷贝cl
"""
p1 = copy.copy(persion)
p2 = persion[:]
p3 = list(persion)  
"""
p1 = persion[:]
p2 = persion[:]

p1[0] = 'alex'
p2[0] = 'fengjie'
p1[1][1] = 50

print(p1)
print(p2)