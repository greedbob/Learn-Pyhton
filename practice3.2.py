# Question:第三章 练习2 按照字典的频率排序而非字母序
# Solution:
# Answer:key函数只返回字典的值，不管字典的键，setdef by_value(item):   return item[1]
import collections
import string
import sys

def swap(t):
    return t[1],t[0]


words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    with open(filename) as file:
        for line in file:
            for word in line.lower().split():
                word = word.strip(strip)
                if len(word) > 2:
                    words[word] += 1
for word in sorted(words,key=swap):
    print("'{0}' occurs {1} times".format(word, words[word]))