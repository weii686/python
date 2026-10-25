def find(num):
    count20=num//20
    num%=20
    count10=num//10
    num%=10
    count5=num//5
    num%=5
    count1=num//1
    return count20,count10,count5,count1

num=int(input('请输入一个整数：'))
x,y,z,i=find(num)
print(f'{x}个20元，{y}个10元，{z}个5元，{i}个1元')
