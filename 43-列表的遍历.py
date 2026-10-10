"""
# while
def while_list():
    name=['heima',"jennifer",34,90,3]
    index=0
    while index<len(name):
        # 将元素取出来，并赋值给a这个变量
        element=name[index]
        print(element)
        index+=1
while_list()
"""
# for
def for_list():
    my_list=[23,21,44,'i',89,38]
    for element in my_list:
        if element=='i':
            print("。。。")
for_list()