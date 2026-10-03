# 1.使用print直接输出数据类型信息
print(type("黑马程序员"))
print(type(666))
print(type(23.5))
# 2.使用变量存储type()的结果
string_type=type("黑马程序员")
int_type=type(666)
float_type=type(34.0)
print(string_type)
print(int_type)
print(float_type)
# 3.使用type(),查看变量中存储的数据类型
name="黑"
name_type=type(name)
print(name_type)