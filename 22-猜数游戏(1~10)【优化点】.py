"""
# 1用循环写的
import random
num=random.randint(1,10)
isprime=0

print("随机产生一个数字(1~10)，你有3次机会进行猜测。")
for i in range(3):
    first=int(input("请输入猜测结果："))
    if first>num&i!=2:
        print("有点大，再试一次吧！")
        i+=1
    elif first<num&i!=2:
        print("有点小，再试一次吧！")
        i+=1
    else:
        isprime=1
        break
if isprime==1:
    i+=1
    print(f"哇！{i}次就猜中了!")
else:
    i+=1
    print(f"{i}次都没猜中，下次再接再厉！")
"""

"""
# 2 if嵌套循环（自己写的）
import random
num=random.randint(1,10)

print("随机产生一个数字(1~10)，你有3次机会进行猜测。")
fir=int(input("请输入猜测结果："))
if fir>num:
    print("大了")
    sec=int(input("请输入猜测结果："))
    if sec>num:
        print("大了")
        thi=int(input("请输入猜测结果："))
        if thi!=num:
            print("三次都没猜中，下次再接再厉！")
        else:
            print("终于猜中了！")
    elif sec<num:
        print("小了")
        thi = int(input("请输入猜测结果："))
        if thi != num:
            print("三次都没猜中，下次再接再厉！")
        else:
            print("终于猜中了！")
    else:
        print("第二次猜中了！")
elif fir<num:
    print("小了")
    sec = int(input("请输入猜测结果："))
    if sec > num:
        print("大了")
        thi = int(input("请输入猜测结果："))
        if thi != num:
            print("三次都没猜中，下次再接再厉！")
        else:
            print("终于猜中了！")
    elif sec < num:
        print("小了")
        thi = int(input("请输入猜测结果："))
        if thi != num:
            print("三次都没猜中，下次再接再厉！")
        else:
            print("终于猜中了！")
    else:
        print("第二次猜中了！")
else:
    print("哇！第一次就猜中了！")
"""

# 3 if嵌套（老师写的）
"""
^^^错点【优化点】(if嵌套  自己写vs老师写  对比)：
   做嵌套if的时候，先讨论无需展开的情况（eg.猜中数字 —> 程序运行结束）,将剩余情况放入
   else中即可
   
   {剩余情况用二层if讨论，(eg.每次共3种情况“情况1：发生及结束，放入最外层if判断并成为第
   一个判断；情况2&3一起放入最外层if判断的else部分，在else中开一个if将2&3分类。)}
   
   减少在第一次if判断时一起行展开多个讨论（即在最外层使用if elif语句）
"""
import random
num=random.randint(1,10)

print("随机产生一个数字(1~10)，你有3次机会进行猜测。")
guess=int(input("请输入第一次猜测结果："))

if guess==num:
    print("恭喜！第一次就猜中了！")
else:
    if guess>num:
        print("大了")
    else:
        print("小了")
    guess = int(input("请输入第二次猜测结果："))
    if guess==num:
        print("恭喜！第二次猜中了。")
    else:
        if guess > num:
            print("大了")
        else:
            print("小了")
        guess = int(input("请输入最后一次的猜测结果："))
        if guess==num:
            print("恭喜！第三次猜中了。")
        else:
            print("三次都没有猜中。下次再接再厉！")