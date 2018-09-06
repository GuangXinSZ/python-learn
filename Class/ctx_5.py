class Student :
    name = ''
    age = 0

    # 代码练习 初始化函数
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    def doHomeWork(self) :
        print(self.name)
    
    # 类的内部类 cls代表类student
    @classmethod
    def plusPut(cls) : 
        cls.age +=1
        print(cls.age)

    @staticmethod
    def add(x, y) :
        pass

student = Student('xin', 1)
student.doHomeWork()
Student.plusPut()
Student.plusPut()
Student.plusPut()