nums_str=input()
nums_list=nums_str.split(',')

sum=0
equ=0
for num in nums_list:
    sum+=int(num)
equ=sum/len(nums_list)

print(f"总和：{sum}，平均值：%.1f" % equ)
