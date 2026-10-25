num=int(input("Enter a number: "))

for i in range(num,0,-2):
    for j in range(i):
        # print((num-i)//2,end='')
        print('*', end='')
        if j==i-1 :
            print()
            if j!=0:
                for k in range((num - (i-2))//2):
                    print(' ',end='')

for i in range(1,num+1,2):
    if i!=1:
        if i==3:
            for j in range((num - i) // 2):
                print(' ',end='')
        for j in range(i):
            print('*',end='')
            if j==i-1 :
                print('\n',end='')
                for k in range(((num - i) // 2)-1):
                    print(' ',end='')



