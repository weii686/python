# 通过下标获取特定位置字符
name='itheima'
print(name[0])
print(name[-7])

# 尝试修改字符串
name=90
print(name)

# index()
my_str=' 45itcast and itheima'
address=my_str.index('and')
print(address)
# 字符串的替换
my_new_str=my_str.replace('it','lijie')
print(my_new_str)
# 字符串的分割
my_list=my_str.split('and')
print(my_list)
# 字符串的规整操作
# 去前后空格
my_new_str=my_str.strip()
print(my_new_str)
# 去指定字符(只去头尾)
my_str=' 45itcast and itheima'
my_1new_str=my_str.strip("4")
print(my_1new_str)

# 练习
str_my='itheima itcast boxuegu'
num=str_my.count('it')
str_new_my=str_my.replace(' ','|')
list_my=str_new_my.split('|')
print(f"字符串{str_my}中有{num}个it字符。")
print(f"字符串{str_my},被替换空格后，结果：{str_new_my}")
print(f"字符串{str_new_my},按照|分割后，得到{list_my}")