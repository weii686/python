# 定义全局变量
name=None
money=5000000

# 要求输入客户姓名
name=input("请输入您的姓名：")

# 定义查询余额函数
def query(check):
    """
    利用布尔类型对输出的内容进行分类->完成查询余额工作
    :param check: 对是否为直接查询余额进行判断
    :return: 无
    """
    if check:
        print("------------------余额查询------------------")
    print(f"您的余额还剩{money}元。")

# 定义存款函数
def saving(num):
    """
    :param num: 存入金额
    :return: 无
    """
    global money
    money += num
    print(f"{name}先生/女士您好，您存款{num}元成功。")
    query(False)

# 定义取款函数
def get_money(num):
    """
    :param num: 取出金额
    :return: 无
    """
    global money
    money -= num
    print(f"{name}先生/女士您好，您取款{num}成功。")
    query(False)

# 定义主菜单
def main():
    """
    主页
    :return: 选择 执行任务的序号
    """
    print("-------------------主菜单--------------------")
    print(f"{name}先生/女士您好，欢迎来到黑马银行ATM，请选择操作：")
    print("查询余额\t【输入1】")
    print("存款\t\t【输入2】")
    print("取款\t\t【输入3】")
    print("退出\t\t【输入4】")
    return int(input("请输入您的选择："))

# 正文
while True:
    chose = main()
    if chose==1:
        print(f"chose={chose}")
        query(True)
        continue
    elif chose==2:
        num = int(input("请输入您存款的金额："))
        saving(num)
    elif chose==3:
        num = int(input("请输入您的取款金额："))
        get_money(num)
    else:
        print("服务结束，祝您生活愉快。")
        break