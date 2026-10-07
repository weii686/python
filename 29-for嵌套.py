# eg
i=0
j=1
love=input("你喜欢的人是：")
for i in range(1,101):
    print(f"今天是和{love}表白的第{i}天，坚持。")
    while j<=10:
        print(f"送给{love}的第{j}朵玫瑰花。")
        j+=1
    print(f"{love},我喜欢你！")
print(f"第{i}天，表白成功。")