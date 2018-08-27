# 类，对象，实例化一个类
# 类最基本的作用封装使用

class Student() :
    name = ''
    age = 0
    # 行为 与 特征
    def print_file(self) :
        print('name:' + self.name )
        print('age: ' + str(self.age))
    def print_profile(self) :
        print(self.name)

class StudentHomeWork() :
    name = ''
    def doHomeWork(self) : 
        print(self.name)

# 实例化一个类
# student = Student()
# student.print_file()