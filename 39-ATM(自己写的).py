# 自己1
# 函数定义
def main():
    """
    主页
    :return: 无
    """
    global chose
    global name
    name="嘉溦"
    print("-------------------主菜单--------------------")
    print(f"{name}先生/女士您好，欢迎来到黑马银行ATM，请选择操作：")
    print("查询余额\t【输入1】")
    print("存款  \t【输入2】")
    print("取款  \t【输入3】")
    print("退出  \t【输入4】")
    chose=int(input("请输入您的选择："))


def check_last():
    """
    余额查询
    :param ans:剩余金额
    :return: 无
    """
    global ans
    ans=ans+save1-pay1
    if chose==1:
        print("------------------余额查询------------------")
    print(f"您的余额还剩{ans}元。")

def save():
    """
    存款
    :param save1:存入的金额
    :return: 无
    """
    global save1
    save1=int(input("请输入您存款的金额："))
    print(f"{name}先生/女士您好，您存款{save1}元成功。")
    check_last()
    save1=0

def pay():
    """
    取款
    :param pay1:取出的金额
    :return: 无
    """
    global pay1
    pay1=int(input("请输入您的取款金额："))
    print(f"{name}先生/女士您好，您取款{pay1}成功。")
    check_last()
    pay1=0

def test():
    """
    退出&其他办理
    :param isprime:判断是否还有其他业务需要办理(是扣1/否扣0)
    :return: 无
    """
    global isprime
    isprime==0
    if isprime==1:
        isprime=int(input("请问还需要办理其他业务吗？(是扣1/否扣0)\n"))
    if isprime==0:
        print("服务结束，祝您生活愉快。")

# 正文
ans=5000000
save1=0
pay1=0
chose=0
isprime=1

while isprime==1:
    main()
    if chose==1:
        check_last()
    elif chose==2:
        save()
    elif chose==3:
        pay()
    test()

"""
# 师要
while isprime==1:
    main()
    if chose==1:
        check_last()
    elif chose==2:
        save()
    elif chose==3:
        pay()
    else:
        test()
"""