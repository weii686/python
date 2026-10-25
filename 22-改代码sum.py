numbers=[3,8,5,12,7]

def total(numbers):
    result=0
    for n in numbers:
        result+=n
    return result

# 找最大值的逻辑 false
def find_max(numbers):
    max_value=numbers[0]
    for n in numbers:
        if n>max_value:
            max_value=n
    return max_value

def count_even(numbers):
    count=0
    for n in numbers:
        if n%2==0: #逻辑错误①
            count+=1
    return count
def show_greater_than(numbers,limit):
    for n in numbers:
        if n>limit: #逻辑错误②
            print(n,end="")
    print()

print("总和：",total(numbers))
print("最大值：",find_max(numbers))
print("偶数个数：",count_even(numbers))
show_greater_than(numbers,5)