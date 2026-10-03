"""
# eg
print("欢迎来到黑马动物园。")

height=int(input("请输入您的身高(cm)："))
vip_level=int(input("请输入您的vip级别(1~5)："))
day=int(input("请输入今天是几号 ："))

if height<120:
    print("您的身高未超过120cm,可以免费游玩。")
elif vip_level>3:
    print("您的VIP级别大于3，可以免费游玩。")
elif day==1:
    print("今天是1号免费日，可以免费游玩。")
else:
    print("不好意思，所有条件都不满足，游玩需要补票10元。")

print("祝您游玩愉快。")
"""

# 简洁版，节省代码量
print("欢迎来到黑马动物园。")

if int(input("请输入您的身高(cm)："))<120:
    print("您的身高未超过120cm,可以免费游玩。")
elif int(input("请输入您的vip级别(1~5)："))>3:
    print("您的VIP级别大于3，可以免费游玩。")
elif int(input("请输入今天是几号 ："))==1:
    print("今天是1号免费日，可以免费游玩。")
else:
    print("不好意思，所有条件都不满足，游玩需要购票10元。")

print("祝您游玩愉快。")

