# 遍历字符串
name="李杰"

for i in name:
    print(i)

# 练习：数一数有几个a
name="ithema is a brand of itcast"
times=0

for i in name:
    if i=='a':
        times+=1

print(f"ithema is a brand of itcast中共含有：{times}个字母a")
