# 构造函数

class Student :
    name = ''
    age = 0
    # 构造函数的使用
    def __init__(self, name, age) :
        # 全局变量(实例变量)
        self.name = name
        self.age = age
    def do_homework(self) :
        print(self.name)

# 实例化一个类
persion = Student('小刘', 22)
persion2 = Student('小信', 11)
persion.do_homework()
persion2.do_homework()