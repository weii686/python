
# 自己
import random
total=10000

for i in range(1,21):
    jixiao = random.randint(1, 10)
    if jixiao<5:
        print(f"员工{i},绩效分{jixiao},低于5，不发工资，下一位。")
    else:
        total-=1000
        print(f"向员工{i}发放工资1000元，账户余额还剩余{total}")
        if total<=0:
            break
print("工资发完了，下个月领取吧。")


# 师
import random
money=10000

for i in range(1,21):
    score = random.randint(1, 10)
    if score<5:
        print(f"员工{i},绩效分{score},低于5，不发工资，下一位。")
        continue
    if money>1000:
        money -= 1000
        print(f"向员工{i}发放工资1000元，账户余额还剩余{money}")
    else:
        print(f"余额不足，当前余额：{money}，不足以发放工资，不发了，下个月再发。")