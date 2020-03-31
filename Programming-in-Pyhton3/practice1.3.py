# Question：第一章例题3
# Solution：
import random

guanci = ['a','the']
zhuti = ['cat','dog','man','women']
dongci = ['sang','ran','jumped']
zhuangyu = ['loudly','quietly','well']

if random.randint(0,2) < 1:
    print(random.choice(guanci),random.choice(zhuti),random.choice(dongci),random.choice(zhuangyu))
else:
    print(random.choice(guanci),random.choice(zhuti),random.choice(dongci))