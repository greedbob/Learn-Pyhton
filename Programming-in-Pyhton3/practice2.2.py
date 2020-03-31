# Question:第二章练习2 修改quadratic.py使得系数0.0对应项不再输出，负数系数的输出形式为‘- n’
# Solution:先确定每一项的形式，最后同一format
# Answer:判断不为零，equation加一项，再判断正负，决定加项的形式
import cmath
import math
import sys

SQUARED = "\N{SUPERSCRIPT TWO}"
ARROW = "\N{RIGHTWARDS ARROW}"

if not sys.platform.startswith("linux"):
    SQUARED = "^2"
    ARROW = "->"
def get_float(msg,allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print('zero is not allowed')
                x = None
        except ValueError as err:
            print(err)
    return x

print('ax\N{SUPERSCRIPT TWO} + bx + c = 0')
a = get_float('enter a:',False)
b = get_float('enter b:',True)
c = get_float('enter c',True)

x1 = None
x2 = None
discriminant = (b ** 2) - (4 * a * c)
if discriminant == 0:
    x1 = -(b / (2 * a))
else:
    if discriminant > 0:
        root = math.sqrt(discriminant)
    else:
        root = cmath.sqrt(discriminant)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)

if b < 0:
    text_b = ' - ' + str(abs(b)) + 'x '
elif b > 0:
    text_b = ' + ' + str(b) + 'x '
else:
    text_b = ''

if c < 0:
    text_c = ' - ' + str(abs(c)) + ' '
elif c > 0:
    text_c = ' + ' + str(c) + ' '
else:
    text_c = ''

equation = ("{0}x\N{SUPERSCRIPT TWO}{1}{2}= 0 \N{RIGHTWARDS ARROW} x = {3}").format(a, text_b, text_c, x1)
if x2 is not None:
    equation += " or x = {0}".format(x2)
print(equation)