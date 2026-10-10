my_list=[1,2,3,4,5,6,7,8,9,10]
index=0
new_list=[]
# while
while index<len(my_list):
    element=my_list[index]
    if element%2==0:
        new_list.append(element)
    index+=1
print(new_list)

# for
new_list2=[]
for element2 in my_list:
    if element2%2==0:
        new_list2.append(element2)
print(new_list2)