# Question:第三章 练习3 每行打印两列 没六十四行打印送纸符
# Solution:利用判断打印
# Answer:利用步距取奇数行和偶数行，利用序列组合字符串
# header = (headline1 + columngap + headline1 + "\n" + headline2 + columngap + headline2)
# for left, right in zip(lines[::2], lines[1::2]):
import collections
import sys


ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)

User = collections.namedtuple("User",
            "username forename middlename surname id")


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} file1 [file2 [... fileN]]".format(
              sys.argv[0]))
        sys.exit()

    usernames = set()
    users = {}
    for filename in sys.argv[1:]:
        with open(filename, encoding="utf8") as file:
            for line in file:
                line = line.rstrip()
                if line:
                    user = process_line(line, usernames)
                    users[(user.surname.lower(), user.forename.lower(),
                            user.id)] = user
    print_users(users)


def process_line(line, usernames):
    fields = line.split(":")
    username = generate_username(fields, usernames)
    user = User(username, fields[FORENAME], fields[MIDDLENAME],
                fields[SURNAME], fields[ID])
    return user


def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] +
                 fields[SURNAME]).replace("-", "").replace("'", ""))
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:
        username = "{0}{1}".format(original_name, count)
        count += 1
    usernames.add(username)
    return username


def print_users(users):
    namewidth = 17
    usernamewidth = 9


    i = 0
    for key in sorted(users):
        if i % 64 == 0:
            print("{0:<{nw}} {1:^6} {2:{uw}} {0:<{nw}} {1:^6} {2:{uw}}".format(
                "Name", "ID", "Username", nw=namewidth, uw=usernamewidth))
            print("{0:-<{nw}} {0:-<6} {0:-<{uw}} {0:-<{nw}} {0:-<6} {0:-<{uw}}".format(
                "", nw=namewidth, uw=usernamewidth))
            if i != 0:
                print('\f')
        user = users[key]
        initial = ""
        if user.middlename:
            initial = " " + user.middlename[0]
        name = "{0.surname}, {0.forename}{1}".format(user, initial)
        print("{0:.<{nw}} ({1.id:4}) {1.username:{uw}}".format(
              name, user, nw=namewidth, uw=usernamewidth),end='')
        if i % 2 == 0:
            print('',end=' ')
        else:
            print('',end='\n')
        i += 1


main()
