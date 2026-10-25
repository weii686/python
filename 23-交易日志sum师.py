def dairy():
    result=0
    while True:
        str=input('请输入交易日志（退出按f）：\n')
        if str=='f':
            break
        str_list=str.split(' ')
        if str_list[0]=='D':
            result+=int(str_list[1])
        else:
            result-=int(str_list[1])
    return result

print(f'银行账户的净金额为：',dairy())