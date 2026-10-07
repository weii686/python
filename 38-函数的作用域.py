# 局部变量
def lo():
    """
    打印num这个变量
    :return: 无
    """
    num=1314520
    print(num)
lo()
# print(num)
# cannot find 'num'

# 全局变量
num=123
def l():
    """
    打印变量num
    :return: 无
    """
    print(num)
l()
print(num)

# global关键字


