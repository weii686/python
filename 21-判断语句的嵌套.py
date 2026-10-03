"""
# eg
print("欢迎来到黑马动物园！")

height=120

if int(input("请输入您的身高(cm)："))>height:
    print("您的身高大于120CM，不可以免费游玩。")
    print("不过，如果您的VIP等级大于3的话，可以免费游玩。")

    if int(input("请告诉我您的VIP等级(1~5):"))<=3:
        print("Sorry,游玩需要购票10元。")
    else:
        print("您的VIP等级大于3，可以免费游玩。")
else:
    print("欢迎你小朋友，可以免费游玩。")
"""


# 练习 发礼物(自己写
age=int(input("请输入年龄："))
if age>=18:
    print("你是成年人了")
    if age<30:
        print("你的年龄达标了")
        if int(input("请输入入职时长："))>2:
            print("你的入职时长达标了，获得礼物！")
        elif int(input("请输入级别："))>3:
            print("获得礼物！")
        else:
            print("入职时长和级别都不达标，无法获得礼物。")
    else:
        print("年龄太大了，无法获得礼物。")
else:
    print("Sorry,未成年不可以领礼物。")

