data = {
"key1": "abc123def456",
"key2": "1234567890",
"key3": "foo",
"key4": "1a2b3c4d"
}

# 计算每个键值对中数字的个数
times=dict()
for key in data.keys():
    element=data[key]
    # element_list=list(element)
    # print(element_list)
    count = 0
    for i in element:
        if ord(i)<58 and ord(i)>47:
            count+=1
        # print(f'i={i},count={count}')
    times[key]=count
# print(times)

# 作比较
for key2 in times.keys():
    element2=times[key2]
    # print(f'key2={key2}, element2={element2}')
    if element2!=0:
        for key3 in times.keys():
            # print(f'key3={key3}, element3={times[key3]}')
            if key2 != key3:
                element3=times[key3]
                if element2<element3:
                    times[key2]=0
                    # print(f'times[key2]={times[key2]}')
                else:
                    times[key3]=0
                    # print(f'times[key3]={times[key3]}')
# print(f'times={times}')

# 打印目标键名
for key in times.keys():
    if times[key]!=0:
        print(f'各值中含有数字最多的键名为：{key}')
