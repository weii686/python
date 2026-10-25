# 自己写
num=int(input("Enter a number: "))
sum=1
for i in range(1,num+1):
    sum*=i
print(f'整数{num}的阶乘是{sum}')

# 老师写
def _sum_(n):
    sum=0
    while n>1:
        sum+=n
        n-=1
    return sum
num=int(input("Enter a number: "))
result=_sum_(num)
print(f'整数{num}的阶乘是{sum}')
