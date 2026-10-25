class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def is_pass(self):
        if self.score >= 60:
            return True
        else:
            return False
stu=Student('张三', 75)
print(f'{stu.name} 是否及格:',stu.is_pass())