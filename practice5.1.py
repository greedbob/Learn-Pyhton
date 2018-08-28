# Question:第五章 模块 5.4 练习 展示目录列表
# Solution:
# Answer:
import optparse
import os
import locale


def main():
    options, args= get_info()
    get_files(options, args)


def get_info():
    parser = optparse.OptionParser()
    parser.add_option('-H', '--hidden', dest='hidden', action='store_true',
                      help=('show hidden files [default:off]'))
    parser.add_option('-m', '--modified', dest='modified', action='store_true',
                      help=('show last modified date/time [default:off]'))
    parser.add_option('-o', '--oder', dest='oder', action='store',
                      help=('order by (''name'', ''n'', ''modified'', ''m'', ''size'', ''s'') default:name]'))
    parser.add_option('-r', '--recursive', dest='recursive', action='store_true',
                      help=('recurse into subdirectories [default:off]'))
    parser.add_option('-s', '--sizes', dest='sizes',  action='store_true',
                      help=('show sizes [default:off]'))
    parser.set_defaults(hidden=False, modified=False, order='name', recursive=False, sizes=False)
    options, args = parser.parse_args()
    return options, args


def get_files(options, args):
    num_dirs = 0
    num_files = 0
    if not options.recursive:
        data = {}
        for path in args:
            num_dirs += 1
            data[path] = {}
            for filename in os.listdir(path):
                if not filename.startswith('.') or not options.hidden:
                    num_files += 1
                    fullname = os.path.join(path, filename)
                    if os.path.isfile(fullname):
                        data[path][fullname] = os.path.getmtime(fullname), os.path.getsize(fullname)
                        print_line(fullname, data[path][fullname], options)
    if options.recursive:
        data = {}
        for path in args:
            num_dirs += 1
            data[path] = {}
            for root, dirs, files in os.walk(path):
                for filename in files:
                    fullname = os.path.join(root, filename)
                    if not fullname.startswith('.') or not options.hidden:
                        num_files += 1
                        data[path][fullname] = os.path.getmtime(fullname), os.path.getsize(fullname)
                        print_line(fullname, data[path][fullname], options)
    print('{0} files, {1} directory'.format(str(num_files), str(num_dirs)))


def print_line(fullname, msg, options):
    line = ''
    line += str(msg[0]) if options.modified else ''
    line += str(msg[1]) if options.sizes else ''
    line += fullname
    print(line)


main()