class Student() :
    name = ''
    age = 0

    def __init__(self, name, age) :
        self.name = name
        self.age = age
    
    def do_homework(self) :
        print('homework')

persion = Student('xin',12)

# dict 字典型
print(persion.__dict__)