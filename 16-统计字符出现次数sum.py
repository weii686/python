str_1=input()
str_dict={}

for element in str_1:
    count1=0
    if element in str_dict:
        continue
    count1=str_1.count(element)
    print(f'element:{element},count1:{count1}')
    str_dict[element]=count1
    str_1=str_1.replace(element,'')

print(str_dict)