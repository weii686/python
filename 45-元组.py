"""
# 定义元组字面量
(6,89,"itheima",23.90)
# 定义元组变量
my_tuple=(56,90,34.09,"89","heima")
print(my_tuple)
print(type(my_tuple))
# 定义空元组
ji=()
juu=tuple()
print(ji,juu)
# 只定义一个元素的元组
t2=('hello',)
print(t2)
# 嵌套元组
t3=(23,89,(78,0,3),('heima',True))
print(t3[0])
print(t3[2][1])
print(t3[3][0])
print(type(t3[3][1]))
print(type(t3[0]))


# 元组的相关操作
t1=(2,'heima',34,8.98,'ji',2,'erf','heima',2)
# index()查找元素位置（下标）
in1=t1.index('heima')
print(in1)
# count()数某一元素的个数
co1=t1.count(2)
print(co1)
co2=t1.count('heima')
print(co2)
# len(元组)计算元组内元素的个数
le1=len(t1)
print(le1)

# while循环 遍历
index=0
while index<len(t1):
    print(t1[index])
    print(type(t1[index]))
    # 防止进入死循环，index+=1推动循环前进
    index+=1

# for循环
for element in t1:
    # for自动推进element被赋值的进度
    print(element)
    if element=='heima':
        name=input("请输入您喜欢的物品：")
        print(f"来学编程，我给您买{name}")
    else:
        print("您自己买!┒┎")
"""

# 修改元组内部的列表
t1=(1,2,8,['itheima','jennifer'])
t1[3][0]='l'
print(t1)


