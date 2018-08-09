import sys
import unicodedata

def print_unicode_table(words):
    print("decimal   hex   chr  {0:^40}".format("name"))
    print("-------  -----  ---  {0:-<40}".format(""))

    code = ord(' ')
    end = sys.maxunicode

    while code < end:
        c = chr(code)
        name = unicodedata.name(c,'***unknown***')
        if word is None or word in name.lower():
            print("{0:7}  {0:5X}  {0:^3c}  {1}".format(code, name.title()))
        code +=1

words = []
if len(sys.argv) >1:
    if sys.argv[1] in ('-h','--help'):
        print('usage:{0}[string]'.format(sys.argv[0]))
        words = None
    else:
        for word in sys.argv[1]:
            words.append(word.lower())
if words is not None:
    i = 0
    while i < len(words):
        print_unicode_table(words[i])
        i +=1