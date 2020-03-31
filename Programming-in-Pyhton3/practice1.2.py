# Question：第一章例题2，输入数字并输出列表、均值、最小值、最大值
# Solution：
try:
    Num = []
    sum = 0
    while True:
        num = input('enter a number or Enter to finish')
        if num is not '':
            Num.append(num)
            sum += int(num)
        else:
            break
    lowest = int(Num[0])
    highest = int(Num[0])
    for c in Num:
        c = int(c)
        if c > highest:
            highest = c
        if c < lowest:
            lowest = c
    count = len(Num)
    mean = sum/count
    print('numbers:',Num)
    print(count,mean,lowest,highest)
except ValueError as err:
    print(err)