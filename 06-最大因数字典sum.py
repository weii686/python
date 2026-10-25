# 自己写

num=int(input('请输入一个整数：'))
num_dict=dict()
for key in range(1,num+1):
    # print(f'key1={key}')
    j=1
    if key==1:
        num_dict[key]=j
    while j<key:
        # print(f'j2={j},key2={key}')
        if key%j==0:
            num_dict[key]=j
            # print(f'key3={key},num_dict={num_dict}')
        j+=1
print(num_dict)


# 数模答案
'''
对1的最大因数判断，即不让1进入下一循环，直接跳出，对字典进行新增。
用此方法，需将字典新增放在一层循环（外层），才可使1完成新增。
同时，内层循环不能再在成功判断j为最大因数之后，直接新增字典的值，而是用统一的变量储存最大因数（即判断成功后的指令为，对统一变量重新赋值）。
实现此操作，则最好用for循环（max_factor + j自带）。while需另外设置统一变量，代码多
通过不进入循环来完成判断，节省代码量。
'''

num=int(input('请输入一个整数n:\n'))
result={}
for i in range(1,num+1):
    max_factor=1
    for j in range(2,i):
        if i % j == 0:
            max_factor=j
    result[i]=max_factor
print(result)

