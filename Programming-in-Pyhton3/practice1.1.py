# Question：第一章例题1，bigdigits.py 程序的变形，不再打印*，而是打印具体的数字
# Solution：替换*为相应数字
# 范例例的for c in digit;if c=='*';c=str(num)非常简洁

Zero = ["  ***  ", " *   * ", "*     *", "*     *", "*     *",
        " *   * ", "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ",
        "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = input('输入')
    column = 0
    while column < 7:
        line = ''
        i = 0
        while i < len(digits):
            num = int(digits[i])
            newline = ''
            j = 0
            while j < len(Digits[num][column]):
                if Digits[num][column][j] == '*':
                    newline += str(num)
                else:
                    newline += ' '
                j += 1
            line += newline + ' '
            i +=1
        print(line)
        column +=1
except ValueError as err:
    print(err)