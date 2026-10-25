tuple_list=[ ('Alice', 25, 165.5, 55.0), ('Bob', 30, 180.2, 80.5), ('Eve', 20, 160.0, 50.0), ('Alice', 30, 170.3, 60.2) ]
tuple_list=sorted(tuple_list,key=lambda x:(x[1],x[2],x[3]),reverse=True)
print(tuple_list)