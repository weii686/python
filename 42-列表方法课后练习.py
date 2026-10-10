age=[21,25,21,23,22,20]
# 追加
age.append(31)
age.extend([29,33,30])
print(age)

# 取出21  ***
element=age.pop(0)
print(f"age={age}")
print(f"element={element}")
age.pop(-1)
print(age)

# 查找
address=age.index(31)
print(address)
print(age)
