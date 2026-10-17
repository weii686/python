# 字典定义
{'ke':78,89:23.3}
# 定义字典变量
my_dict={'ke':78,89:23.3}
print(my_dict)
print(type(my_dict['ke']))
# 定义空字典
my_dict={}
print(my_dict)
my_dict=dict()
print(my_dict)
# 字典的嵌套
my_dict={'jiawei':{'age':20,'hobby':'running'},'li':{'age':21,'hobby':'running'}}
print(my_dict['li']['hobby'])
stu_score={'jiawei':{'高数':100,'线代':100},'li':{'硕士':'硕士：华南理工大学','age':21}}
print(stu_score['li']['硕士'])
# 更新字典
my_dict['li']['age']=18
print(my_dict)
# 新增元素
my_dict['li']['ai']='weiii686'
print(my_dict)
# 删除元素
cancel=my_dict.pop('li')
print(cancel)
print(my_dict)
# 清空字典
my_dict.clear()
print(my_dict)
# 获取全部的key
my_dict={'jiawei':{'age':20,'hobby':'running'},'li':{'age':21,'hobby':'running'}}
keys=my_dict.keys()
print(keys)
# 遍历字典
for key in keys:
    element=my_dict[key]['hobby']
    print(element)