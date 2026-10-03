"""
# 输出不换行
print("hello",end='')
print("world")

# 列表对齐(3字节可用)
print("my\tlijie")
print("hello\tworld")
"""

"""
# 九九乘法表(自己)
num1=1

while num1<=9:
    num2 = 1
    while num2<=num1:
        print(f"{num2}*{num1}={num1*num2}\t",end='')
        if num1==num2:
            print("\n")
        num2+=1
    num1+=1
"""

# (师)
num1=1

while num1<=9:
    num2 = 1
    while num2<=num1:
        print(f"{num2}*{num1}={num1*num2}\t",end='')
        num2+=1
    num1+=1
    print()