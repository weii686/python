# 对list进行切片，从1开始，4结束，步长1
my_list=[0,1,2,3,4,5,6,7,8,9]
innt=my_list[0:3:1]
print(innt)
# 对tuple进行切片，从头开始，到最后结束，步长1
my_tuple=(0,1,2,3,4,5,6,7,8,9)
inu=my_tuple[0:10:1]
print(inu)
# 对str进行切片，从头开始，到最后结束，步长2
my_str="0123456789"
ine=my_str[0:11:2]
print(ine)

# 对list进行切片，从1开始，4结束，步长-1
nint=my_list[-7:-10:-1]
print(nint)
# 逆回变正序
nnit=nint[-1:-4:-1]
print(nnit)
# 对tuple进行切片，从头开始，到最后结束，步长-2
uni=my_tuple[-1:-10:-2]
print(uni)
uniturn=uni[-1:-6:-1]
print(uniturn)
# 对str进行切片，从3开始，到1结束，步长-1
eni=my_str[-7:-10:-1]
print(eni)
eniturn=eni[-1::-1]
print(eniturn)