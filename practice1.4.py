import random

guanci = ['a','the']
zhuti = ['cat','dog','man','women']
dongci = ['sang','ran','jumped']
zhuangyu = ['loudly','quietly','well']
num = 0
try:
    column = int(input('输入范围在1~10的行数'))
    if 1<= column <= 10:
        num = column
    else:
        print('数值范围')
except ValueError as err:
    print(err)

i = 0
while i < num:
    if random.randint(0,2) < 1:
        print(random.choice(guanci),random.choice(zhuti),random.choice(dongci),random.choice(zhuangyu))
    else:
        print(random.choice(guanci),random.choice(zhuti),random.choice(dongci))
    i +=1