f = open("yesterday.txt", 'r', encoding="utf-8")

# data1 = f.read()
# f.write('123, \n')
# # data1 = f.read()
# f.write('456')
 
# f.close()
# for i in range(5):
#     print(f.readline())

# for index, line in enumerate(f.readlines()):
#     if index == 3:
#         print('---分割线')
#         continue
#     print(line.strip())
for line in f:
    print(line)

f.close()