ans=10

if int(input("请输入第一次猜想的数字："))==ans:
    print("猜对了！")
elif int(input("猜错了，再猜一次："))==ans:
    print("猜对了！")
elif int(input("猜错了，最后猜一次："))==ans:
    print("猜对了！")
else:
    print(f"Sorry,全都猜错啦，我想的是{ans}")