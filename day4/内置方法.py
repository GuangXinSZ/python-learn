import time

b = bytearray("abcde", encoding="utf-8")
# print(all([1, -5, 2]))
# print(any([0, 1]))
b[0] = 98
print(b)