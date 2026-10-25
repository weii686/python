# 做列表切割   !!!!!
import sys
def create_list():
    str_list=[]
    for line in open(r'D:\code\dairy.txt','r',encoding='utf-8'):
        list=line.strip().split(' ')
        print(f'line={line}')
        str_list.extend(list)
    print(f'str_list={str_list}')
    return str_list

# 做字典数日志个数
def create_dict(list):
    list_keys=list[0::2]
    list_values=list[1::2]
    diaries=len(list_keys)
    print(f'list_keys={list_keys}, list_values={list_values}, diaries={diaries}')
    return diaries,list_keys,list_values

# 判断d/w,并做加减，得剩余
def _result_(diaries,keys,values):
    result=0
    for i in range(0,diaries):
        money = int(values[i])
        print(f'money={money}')
        if keys[i]=='D':
            result+=money
        else:
            result-=money
    print(f'result={result}')
    return result

# 多行输入
# AI加了 break & if not line
def _write_():
    while True:
        try:
            line=sys.stdin.readline()
            if not line:
                break
            f.write(line)
        except EOFError:
            f.flush()
            break

# begin
f=open(r'D:\code\dairy.txt','w',encoding='utf-8')
_write_()

str_list=create_list()
diaries,list_keys,list_values=create_dict(str_list)
result=_result_(diaries,list_keys,list_values)
print(result)
f.close()