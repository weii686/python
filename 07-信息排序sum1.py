tuple_list = [ ('Alice', 25, 165.5, 55.0), ('Bob', 30, 180.2, 80.5), ('Eve', 20, 160.0, 50.0), ('Alice', 30, 170.3, 60.2) ]
# 将列表内元组拆分，变为字典，一一对应
def _change_(first_list):
    global sec_dict
    sec_dict={}
    for key in range(len(first_list)):
        sec_dict[key]=first_list[key]
        print(sec_dict)
# sec_dict={0: ('Alice', 25, 165.5, 55.0), 1: ('Bob', 30, 180.2, 80.5), 2: ('Eve', 20, 160.0, 50.0), 3: ('Alice', 30, 170.3, 60.2)}

# 将目标元素组(所有的age/height/weight)找出，装进一个列表，保证列表内的索引与字典数据组一一对应
def _tag_(dict,suoyin):
    global tag_dict,fresh_dict,len_n,save_dict
    for key3 in dict.keys():
        tag_dict=dict[key3][suoyin]
        tag_list=tag_dict[key3]
        len_n=len(tag_list)
    save_dict=tag_dict

# 产生新的排序,即不断地找最大值——>进行新排序——>删去max
def _turn_(dict2,element_list):
    global tag_dict,fresh_dict,n,tag_list,save_list
    save_list=element_list
    for i in range(len_n):
        address = dict2.index(max(element_list))
        fresh_dict[i] = dict2[address]
        del element_list[address]

# if判断是否有相同的值，拉出来放进新列表，进行后面的2//3轮排序
def _judge_(third_dict):
    global save_list,save_dict
    for element1 in save_list:
        for element2 in save_list:
            if element1 == element2:
                same_dict=third_dict[save_list.index(element1)]
                same_dict=third_dict[save_list.index(element2)]

# 二级排序
def _turn_again_():
    global same_dict
    _turn_(same_dict,save_list)
    










# 开始
tag_dict = {}
fresh_dict = {}
tag_list = []
n = 0
address = 0

_change_(tuple_list)
_tag_(sec_dict,)
_turn_()
print(f'fresh_dict={fresh_dict},tag_list={tag_list}')
"""
# 排优先级
j=0
while j<=3:
    if j==1:
        _turn_()
    elif j==2:
"""

