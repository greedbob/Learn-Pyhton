# Question:第四章练习 对文件中的字符串进行维护
# Solution:
# Answer:

import os


def main():
    lst = []
    filename = None
    files = os.listdir('.')
    width = 1 if len(files) < 10 else 2 if len(files) < 100 else 3

    try:
        if not lst:
            filename = input('Choose filename:')
            filename += '' if filename.endswith('.lst') else '.lst'
            print(filename)
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
    edit_list(filename)


def edit(items, filename, dirty, choice='a'):
    if choice == 'a':
        item = input('Add item:')
        if item:
            print()
            items.append(item)
            items.sort(key=str.lower)
            dirty = True
    elif choice == 'd':
        num = int(input('Delete item number (or 0 to cancel):'))
        if num:
            print()
            del items[num-1]
        dirty = True
    elif choice == 's':
        fh = open(filename, "w", encoding="utf8")
        fh.write('\n'.join(items))
        fh.write('\n')
        dirty = False
        print('Saved {0} items to {1}'.format(len(items), filename))
        print()
    elif choice == 'q':
        if dirty:
            save = input('Save unsaved changes (y/n) [y]').lower()
            if save == 'y':
                fh = open(filename, "w", encoding="utf8")
                fh.write('\n'.join(items))
                fh.write('\n')
                dirty = False
                print('Saved {0} items to {1}'.format(len(items), filename))
                print()
    return dirty


def edit_list(filename):
    items = []
    try:
        for line in open(filename, encoding="utf8"):
            items.append(line.rstrip())
    except EnvironmentError as err:
        print("ERROR: failed to load {0}: {1}".format(filename, err))
    dirty = True
    while True:
        width = 1 if len(items) < 10 else 2 if len(items) < 100 else 3
        if not items:
            print('-- no items are in the list')
            choice = input('[A]dd [Q]uit [a]:').lower()
            if choice not in 'aq':
                print('ERROR: invalid choice--enter one of ''AaQq''')
                continue
            else:
                dirty = edit(items, filename, dirty, choice)
                continue
        elif dirty:
            for lino, line in enumerate(items, start=1):
                print('{0:{width}} {line}'.format(lino, **locals()))
            choice = input('[A]dd [D]elete [S]ave [Q]uit [a]:').lower()
            if choice not in 'adsq':
                print('ERROR: invalid choice--enter one of ''AaDdSsQq''')
                continue
            else:
                dirty = edit(items, filename, dirty, choice)
                continue
        elif not dirty:
            for lino, line in enumerate(items, start=1):
                print('{0:{width}} {line}'.format(lino, **locals()))
            choice = input('[A]dd [D]elete [Q]uit [a]:').lower()
            if choice not in 'adq':
                print('ERROR: invalid choice--enter one of ''AaDdQq''')
                continue
            else:
                dirty = edit(items, filename, dirty, choice)
                continue


main()
