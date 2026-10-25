num=int(input())

for i in range(1,num+1):
    if i%2==0:
        if i!=num:
            print(str(i)+' ',end='')
        else:
            print(str(i),end='')

