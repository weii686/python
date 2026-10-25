scores=[80,60,90,45]

def average(scores):
    total=0
    for s in scores:
        total+=s
    return total/(len(scores))

def count_pass(scores):
    count=0
    for s in scores:
        if s>=60:
            count+=1
    return count

print("平均分：",average(scores))
print("及格人数：",count_pass(scores))