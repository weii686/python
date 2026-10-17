
student=('jiawei',20,['running','music'])
print(f"年龄是{student[1]}岁")
print(f"学生的名字是：{student[0]}")
cancel=student[2].pop(0)
print(student)
student[2].append('jogging')
print(student)
print(cancel)
