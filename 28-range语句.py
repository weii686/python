# range语法1
for i in range(5):
    print(i)

# range语法2
for j in range(67,78):
    if j%3==0:
        print(j)

# range语法3
for k in range(67,78,3):
    print(f"{k}\t",end='')
    if k%2==0:
        print()
        print(k+1,k)

# 练习 数偶数的个数
num=100
count=0

for i in range(1,num):
    if i%2==0:
        count+=1

print(f"从1到{num}，一共有{count}个偶数。")