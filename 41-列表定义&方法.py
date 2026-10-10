# 定义语法
my_list = [1,2,3,4,5,6,[3,4,56],7,8,9]
print(my_list)
print(type(my_list))
"""
# 嵌套
a=[45,'ik','fj',[45]]
print(a)

# 下标（索引）
print(my_list[6])
print(a[2])

# 反向下标（索引）
print(my_list[-1])
print(my_list[-4])
print(a[-3])

# 嵌套下标
print(my_list[-4][2])
"""

# index方法
address=my_list.index(9)
print(address)

# 修改功能
# 修改元素
my_list[2]=89
print(my_list)
my_list[-3]=38
print(my_list)
# 插入元素
my_list.insert(2,"itheima")
print(my_list)
# 追加元素1
my_list.append(0)
print(my_list)
# 追加元素2
my_list.extend([34,78])
print(my_list)
# 删除元素1pop
my_list.pop(1)
print(f"取出元素后的列表内容：{my_list}")
element=my_list.pop(1)
print(f"取出的元素：{element}")
# 删除元素2
del my_list[9]
print(my_list)
# 删除列表中的第一个匹配项
my_list.append(5)
print(my_list)
my_list.remove(5)
print(my_list)
# 统计某元素在列表中的数量
# print(my_list.count(5))
count=my_list.count(5)
print(f"count={count}")
# 清空列表
my_list.clear()
print(my_list)
# 列表的全部元素数量
counts=len(my_list)
print(f"counts={counts}")