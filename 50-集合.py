# 定义集合字面量
{2,3,4,0,45}
# 定义集合变量
my_set={1,2,3,1,2,3,1,2,3}
print(my_set)
print(type(my_set))
# 定义空集合
my_set=set()
print(my_set)
print(type(my_set))
# 添加新元素
my_set={1,2,3,1,2,3,1,2,3}
my_set.add('hello')
my_set.add(89)
print(my_set)
# 移除元素
my_set.remove('hello')
print(my_set)
# 从集合中随机取出一个元素
element=my_set.pop()
print(element)
print(type(element))
print(my_set)
# 清空集合
my_set.clear()
print(my_set)
# 取出2个集合的差集
set1={1,2,3,4,5}
set2={1,2,4,6,7,8}
set3=set1.difference(set2)
print(set3)
print(set1)
print(set2)
# 删去2个集合的差集
set1.difference_update(set2)
print(set1)
print(set2)
# 将2个集合合并
set1={1,2,3,4,5}
set3=set1.union(set2)
print(set1)
print(set2)
print(set3)

# 练习
my_list=['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
set1=set()
for element in my_list:
    set1.add(element)
print(set1)
