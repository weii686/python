"""
# eg
def add(x,y,d):
    ans=x-y+d
    return  ans
r=add(1,1,9)
print(r)


def name():
    print("hello")
i=name()
print(i)
print(type(i))
"""
def check_age(age):
    if age>=18:
        return "SUCCESS"
    else:
        return None
result=check_age(12)
print(result)
print(type(result))
if not result:
    print("未成年，不可以进入。")