
# 名字
print("你叫什么名字？")
name=input()
print(f"{name}你好！")
love=input("%s，你喜欢什么呀?:)\n" % name)
print(f"我也喜欢你，{name}，{love}喜欢你")

"""
num=input("这个数字是？")
# 不转类型
print(f"{num}的类型是{type(num)}")
# 转成整型&浮点型
num=int(num)
print(f"{num}的类型是{type(num)}")
num=float(num)
print(f"{num}的类型是{type(num)},num={num}")

# 练习
user_name=input("用户名：\n")
useer_type=input("类型：\n")
print("您好：%s，您是尊贵的：%s 用户，欢迎您的光临" % (user_name,useer_type))
"""