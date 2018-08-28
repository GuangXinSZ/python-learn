# 定义类型
class Student() :
    name = ''
    age = 0
    sum = 0

    def __init__(self, name, age) :
        self.name = name 
        self.age = age
        # 内部变量的使用场景
        # self.__class__.sum +=1
        # 范文全局变量
        # print('当前班级学生的总数为:', str(self.__class__.sum))
    
    def do_homework(self) :
        print('homework')
    
    # 类方法, 调用类变量
    @classmethod
    def plusSum(cls) :
        cls.sum +=1
        print(cls.sum)

persion = Student('xin',12)
Student.plusSum()
persion1 = Student('liu', 4)
Student.plusSum()
# dict 字典型
# print(persion.__dict__)
# print(Student.sum)