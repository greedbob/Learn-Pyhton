# Question：第一章例题5，输入数字并输出列表、均值、最小值、最大值；新增了排序和计算中位数
# Solution：冒泡排序
try:
    Num = []
    sum = 0
    while True:
        num = input('enter a number or Enter to finish')
        if num is not '':
            Num.append(num)
            i = len(Num)
            while i < len(Num) and len(Num) > 1:
                if Num[i] < Num[i-1]:
                    temp = Num[i]
                    Num[i] = Num[i-2]
                    Num[i-1] = temp
                    i += 1
            sum += int(num)
        else:
            break
    if len(Num) % 2 == 0:
        zhong = (int(Num[int(len(Num)/2)]) + int(Num[int(len(Num)/2-1)])) / 2
    else:
        zhong = Num[int((len(Num)-1)/2)]
    lowest = int(Num[0])
    highest = int(Num[len(Num)-1])
    count = len(Num)
    mean = sum/count
    print('numbers:',Num)
    print(count,mean,zhong,lowest,highest)
except ValueError as err:
    print(err)