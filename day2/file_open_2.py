f = open("yesterday.txt", 'wb') # r+ 读写 w+写读 a+追加读写 wb二进制
# # print(f.tell())
# f.readline()
# f.readline()
# f.readline()
# f.seek(0) # 回到那个位置
# print(f.readline())
# print(f.encoding)
 # f.truncate(10) 截取文件里面的值
f.write("-----------DOTO::------------\n".encode('utf-8'))
# f.write("-----------DOTO::------------\n")
# f.write("-----------DOTO::------------\n")
# f.seek(2)
# f.tell()
# print(f.readline())
# f.write('111111, \n')

f.close()
