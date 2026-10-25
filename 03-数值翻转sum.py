# 法1 切分
num=input()
num=num[::-1]
print(num)

# 法2 整数拆分
num=input()
count=0
weishu=1
final=0

while count<len(num):
    count+=1
    weishu*=10
weishu//=10

change=1
for element in str(num):
    while change <= weishu:
        element=int(element)
        final+=element*change
        change*=10
        break

print(final)










