info=input()
info_list=info.split('，')

if int(info_list[1])>=18:
    print(f'你好，{info_list[0]}！你已成年。')
else:
    print(f'你好，{info_list[0]}！你尚未成年。')