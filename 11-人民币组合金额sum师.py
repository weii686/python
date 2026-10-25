def min_combination(amount):
    twenties=amount//20
    tens=(amount%20)//10
    fives=((amount%20)%10)//5
    ones=(((amount%20)%10)%5)//1
    print('{}个20元，{}个10元，{}个5元，{}个1元'.format(twenties,tens,fives,ones))
# 调用函数进行测试
money=int(input('请输入人民币的金额：'))
min_combination(money)