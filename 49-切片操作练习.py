# 练习 (自己)5种方法将“黑马程序员”打印出来
Inn='万过薪月，员序程马黑来，nohtyP学'

heima=Inn[-10:-15:-1]
print(heima)

heima2=Inn[5:10:]
heima2=heima2[::-1]
print(heima2)

heima3=Inn.split('，')
print(heima3[1][-2::-1])

heima4=Inn.strip('万过薪月，nohtyP学')
print(heima4[-2::-1])

heima5=Inn.replace('，nohtyP学','')
heima5=heima5.replace('万过薪月，','')
print(heima5[-2::-1])
# (师) 3种方法
result1=Inn[::-1][9:14]
print(result1)

result2=Inn[5:10:][::-1]
print(result2)

# 用split分割成列表，再用replace替换
hei=Inn.split('，')

print(hei[1][-2::-1])

result3=hei[1].replace('来','')
print(result3[::-1])