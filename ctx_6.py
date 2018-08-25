# for x in range(0, 10, 2) :
#     print(x)
#     print(x, end='|')
# for y in range(0, 10, 3) :
#     print(y, end='|')
a = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(0, len(a), 3) :
    print(a[i])
b = a[0:len(a):2]
print(b)