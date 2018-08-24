# Question:第四章练习 对文件中的字符串进行维护
# Solution:
# Answer:

import os


def edit(items, filename, dirty, choice):
    if choice == 'a':
        item = input('Add item:')
        items = items.append(item)
        items = items.sort(key=str.lower)
        dirty = True
    elif choice == 'd':
        num = int(input('Delete item number (or 0 to cancel):'))
        del items[num-1]
        dirty = True
    elif choice == 's':
        fh = open(filename, "w", encoding="utf8")
        fh.write('\n'.join(items))
        fh.write('\n')
        dirty = False
        print('Saved {0} items to {1}'.format(len(items), filename))
    elif choice == 'q':
        if dirty:
            save = input('Save unsaved changes (y/n) [y]').lower()
            if save == 'y':
                fh = open(filename, "w", encoding="utf8")
                fh.write('\n'.join(items))
                fh.write('\n')
                dirty = False
                print('Saved {0} items to {1}'.format(len(items), filename))
    return dirty


def editlist(filename):
    items = []
    for item in open(filename):
        items = items.append(item)
    dirty = True
    while True:
        width = 1 if len(items) < 10 else 2 if len(items) < 100 else 3
        if not items:
            print('-- no items are in the list')
            choice = input('[A]dd [Q]uit').lower()
            if choice not in 'aq':
                print('ERROR: invalid choice--enter one of ''AaQq''')
                continue
            else:
                dirty = edit(items, filename, dirty, choice='a')
        elif dirty:
            for lino, line in enumerate(items, start=1):
                print('{0:{width} {line}}'.format(width, **locals()))
            choice = input('[A]dd [D]elete [S]ave [Q]uit [a]:').lower()
            if choice not in 'aq':
                print('ERROR: invalid choice--enter one of ''AaDdSsQq''')
                continue
            else:
                dirty = edit(items, filename, dirty, choice='a')
        elif not dirty:
            for lino, line in enumerate(items, start=1):
                print('{0:{width} {line}}'.format(width, **locals()))
            choice = input('[A]dd [D]elete [Q]uit [a]:').lower()
            if choice not in 'aq':
                print('ERROR: invalid choice--enter one of ''AaDdQq''')
                continue
            else:
                dirty = edit(items, filename, dirty, choice='a')


def mian():
    lst = []
    filename = None
    files = os.listdir('.')
    width = 1 if len(files) < 10 else 2 if len(files) < 100 else 3

    try:
        if not lst:
            filename = input('Choose filename:')
            filename = filename + '' if filename.endswith('.lst') else '.lst'
        else:

            for lino, file in enumerate(files, start=1):
                lst.append(file)
                print('{0:{width} {file}}'.format(width, **locals()))
            while True:
                index = int(input('Choose filename:'))
                if index == 0:
                    filename = input('name')
                    filename = filename + '' if filename.endswith('.lst') else '.lst'
                    break
                elif index <= len(lst):
                    filename = lst[index-1]
                    break
                else:
                    print('ERROR: invalid index')
    except ValueError as err:
        print(err)
    editlist(filename)


mian()
