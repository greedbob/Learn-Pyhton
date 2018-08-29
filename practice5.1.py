# Question:第五章 模块 5.4 练习 展示目录列表 相当于 dir/ls
# Solution:创建组合数据，存储filename、size、modified，利用dict.item()函数将dict转化为set并sorted利用key函数排序
# Answer:参考代码排序方法：
# 获取所有文件名和目录名filenames、dirs
# for name in filenames: 获取size modified
# 构造元组，第一项为排序参照项，第二项为字符串filename、size、modified
import locale
import optparse
import os
import datetime
locale.setlocale(locale.LC_ALL, '')


def main():
    options, args = get_info()
    get_files(options, args)


def get_info():
    usage = """ls.py [options] [path1 [path2 [... pathN]]]

    The paths are optional; if not given . is used."""
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('-H', '--hidden', dest='hidden', action='store_true',
                      help='show hidden files [default:off]')
    parser.add_option('-m', '--modified', dest='modified', action='store_true',
                      help='show last modified date/time [default:off]')
    parser.add_option('-o', '--oder', dest='order', action='store',  type='string',
                      help='order by (''name'', ''n'', ''modified'', ''m'', ''size'', ''s'') [default:name]')
    parser.add_option('-r', '--recursive', dest='recursive', action='store_true',
                      help='recurse into subdirectories [default:off]')
    parser.add_option('-s', '--sizes', dest='sizes',  action='store_true',
                      help='show sizes [default:off]')
    parser.set_defaults(order='name')
    options, args = parser.parse_args()
    if not args:
        args = ["."]
    return options, args


def get_files(options, args):
    num_dirs = 0
    num_total = 0
    if not options.recursive:
        data = {}
        ordered_data = {}
        for path in args:
            num_dirs += 1
            data[path] = {}
            for filename in os.listdir(path):
                if not filename.startswith('.') or not options.hidden:
                    num_total += 1
                    fullname = os.path.join(path, filename)
                    time = datetime.datetime.fromtimestamp(os.path.getmtime(fullname))
                    size = os.path.getsize(fullname)
                    data[path][fullname] = time.strftime('%Y-%m-%d %H:%M:%S'), size
            ordered_data[path] = order_data(options.order, data[path])
            print_path(ordered_data[path], options)
    if options.recursive:
        data = {}
        ordered_data = {}
        for path in args:
            num_dirs += 1
            data[path] = {}
            for root, dirs, files in os.walk(path):
                for filename in files:
                    if not filename.startswith('.') or not options.hidden:
                        fullname = os.path.join(root, filename)
                        num_total += 1
                        time = datetime.datetime.fromtimestamp(os.path.getmtime(fullname))
                        size = os.path.getsize(fullname)
                        data[path][fullname] = time.strftime('%Y-%m-%d %H:%M:%S'), size
            ordered_data[path] = order_data(options.order, data[path])
            print_path(ordered_data[path], options)
    print('{0} file{1}, {2} director{3}'.format(str(num_total-num_dirs) if num_total-num_dirs else 'no',
                                                's' if num_total-num_dirs != 1 else '',
                                                str(num_dirs) if num_dirs else 'no',
                                                'ies' if num_dirs != 1 else 'y'))


def print_path(ordered_data, options):
    for item in ordered_data:
        line = ''
        line += ('{0:>19} '.format(str(item[1][0]))) if options.modified else ''
        line += ('{0:>15} '.format(str(item[1][1]))) if options.sizes else ''
        line += str(item[0])
        print(line)


def order_data(order, data):
    if order == 'size' or order == 's':
        ordered_data = sorted(data.items(), key=lambda x: x[1][1])
    elif order == 'modified' or order == 'm':
        ordered_data = sorted(data.items(), key=lambda x: x[1][0])
    else:
        ordered_data = sorted(data.items(), key=lambda x: x[0])
    return ordered_data


main()
