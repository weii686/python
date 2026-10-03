"""
# 猜数游戏 1~100 （自己写的）
import random
num=random.randint(1,100)
i=1

print("随机产生一个数字(1~100)，请你进行猜测。")

guess=int(input("请输入你的猜测结果："))
while guess!=num:
    if guess>num:
        print("你猜的大了")
    else:
        print("你猜的小了")
    i+=1
    guess = int(input("请输入你的猜测结果："))

print(f"你猜中了！一共用了{i}次！")
"""

# 猜数游戏 1~100 （老师写的）
"""
利用设置判断的本质:进行布尔->比较运算->直接对变量进行赋值判断(True/False)->放入循环内部if中
->成为完成if判断后的执行内容
"""

import random
num=random.randint(1,100)
flag=True
count=1

print("随机产生一个数字(1~100)，请你进行猜测。")

while flag==True:
    guess=int(input("请输入你的猜测结果："))
    count += 1
    if guess==num:
        flag=False
    elif guess>num:
        print("你猜的大了")
    else:
        print("你猜的小了")

print(f"你猜对了！一共用了{count}次！")
