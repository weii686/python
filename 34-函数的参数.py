# eg
def add(x,y,z):
    ans=x+y+z
    print(ans)

add(33,87,4)

# 练习 测核酸(自己)
def tanpreture(x):
    print(f"体温测量中，您的体温是：{x},",end='')
    if x>37.5:
        print("需要隔离！")
    else:
        print("体温正常请进！")

tanpreture(float(input("欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明！\n")))