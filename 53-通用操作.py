my_list=[1,2,3,4,5]
my_tuple=(1,2,3,4,5)
my_str='abcdrfg'
my_set={1,2,3,4,5}
my_dict={'key':1,'c':3,'b':2,'e':5,'d':4}

# len()
print(f"列表中元素个数为{len(my_list)}")
print(f"元组中元素个数为{len(my_tuple)}")
print(f"字符串中元素个数为{len(my_str)}")
print(f"集合中元素个数为{len(my_set)}")
print(f"字典中元素个数为{len(my_dict)}")

# max()
print(f"列表中最大的元素为{max(my_list)}")
print(f"元组中最大的元素为{max(my_tuple)}")
print(f"字符串中最大的元素为{max(my_str)}")
print(f"集合中最大的元素为{max(my_set) }")
print(f"字典中最大的元素为{max(my_dict)}")

# min()
print(f"列表中最小的元素为{min(my_list) }")
print(f"元组中最小的元素为{min(my_tuple)}")
print(f"字符串中最小的元素为{min(my_str)}")
print(f"集合中最小的元素为{min(my_set) }")
print(f"字典中最小的元素为{min(my_dict)}")

# 转成列表
print(f"列表转列表为{list(my_list) }")
print(f"元组转列表为{list(my_tuple)}")
print(f"字符串转列表为{list(my_str)}")
print(f"集合转列表为{list(my_set) }")
print(f"字典转列表为{list(my_dict)}")

# 转元组
print(f"列表转元组为{tuple(my_list) }")
print(f"元组转元组为{tuple(my_tuple)}")
print(f"字符串转元组为{tuple(my_str)}")
print(f"集合转元组为{tuple(my_set) }")
print(f"字典转元组为{tuple(my_dict)}")

# 转字符串
print(f"列表转字符串为{str(my_list) }")
print(f"元组转字符串为{str(my_tuple)}")
print(f"字符串转字符串为{str(my_str)}")
print(f"集合转字符串为{str(my_set) }")
print(f"字典转字符串为{str(my_dict)}")

# 转集合
print(f"列表转集合为{set(my_list) }")
print(f"元组转集合为{set(my_tuple)}")
print(f"字符串转集合为{set(my_str)}")
print(f"集合转集合为{set(my_set) }")
print(f"字典转集合为{set(my_dict)}")

"""
# 转字典
print(f"列表转字典为{dict(my_list) }")
print(f"元组转字典为{dict(my_tuple)}")
print(f"字符串转字典为{dict(my_str)}")
print(f"集合转字典为{dict(my_set) }")
print(f"字典转字典为{dict(my_dict)}")
"""

# 容器的通用功能
my_list=[1,4,2,3,6]
my_tuple=(1,0,8,7,4)
my_str='qkcdrge'
my_set={1,0,2,6,5}
my_dict={'key':1,'c':3,'b':2,'e':5,'d':4}

print(f"正序排列表：{sorted(my_list)}")
print(f"正序排元组：{sorted(my_tuple)}")
print(f"正序排字符串：{sorted(my_str)}")
print(f"正序排集合：{sorted(my_set)}")
print(f"正序排字典：{sorted(my_dict)}")

print(f"逆序排列表：{sorted(my_list,reverse=True)}")
print(f"逆序排元组：{sorted(my_tuple,reverse=True)}")
print(f"逆序排字符串：{sorted(my_str,reverse=True)}")
print(f"逆序排集合：{sorted(my_set,reverse=True)}")
print(f"逆序排字典：{sorted(my_dict,reverse=True)}")


