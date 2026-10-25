a=[10,20,30,40,50]
#1
print(a[1:4])
#2
print(a[-1])
print(len(a))

d={"a":1,"b":2}
# 3
print(d.get("c",0))
d["a"]=3
print(d)

def multiply(x,y=2):
    return x*y
print(multiply(3))
print(multiply(3,4))

s="Python"
print(s[0])
# 4
print(s[-2:])
print(len(s))
print(s.upper())

total=0
for i in range(1,6):
    total+=i
print(total)
#5
print(list(range(2,10,3)))