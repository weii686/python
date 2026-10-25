# 设一个函数，用于排序，制作优先级 (lambda)
def sort_key(t):
    return (-t[1],-t[2],-t[3])
tuple_list = [ ('Alice', 25, 165.5, 55.0),
               ('Bob', 30, 180.2, 80.5),
               ('Eve', 20, 160.0, 50.0),
               ('Alice', 30, 170.3, 60.2)
]
tuple_list=sorted(tuple_list, key=sort_key, reverse=False)
print(tuple_list)