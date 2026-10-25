"""
[20,50] false
[50,40,30,20,10] false
5

None  false
{"a":3,"b":2}

6
12
# y为缺省参数，2为其默认值。调用该函数时，若没有给出y对应的实际参数，则y直接使用默认值2

P
o false
6
PYTHON

15
[2,4,6,8] false


1.true
return total/(len(scores)+1)
此处无需len()+1。
len()函数计算的是目标数据容器中的元素总数。
即len(scores)已经计算出了scores中的元素总数，此处不用"+1"
修复：
    return total/len(scores)
2.true
if s>60:
此处想执行的是：判断分数是否及格。及格包含60分。而此处仅为："s>60",即大于60才及格。将60划定在了不及格里，不符合题意。
修复：
    if s>=60:
3. false
print("平均分：",average(scores))
print("及格人数：",count_pass(scores))
average(scores),count_pass(scores)两个返回值都是int整型，而整型不可直接与字符串做拼接。
需要将整型转成字符串，或用%f,%d,帮整型数据提前在字符串中占位。
修复：
3.1占位
print("平均分：%f" % average(scores))
print("及格人数：%d" % count_pass(scores))
3.2转型
print("平均分：",str(average(scores)))
print("及格人数：",str(count_pass(scores)))
"""