import sys

k = list('1234567890-=WERTYUIOP[]\\SDFGHJKL;\'XCVBNM,./')
v = list('`1234567890-QWERTYUIOP[]ASDFGHJKL;ZXCVBNM,.')

matched_key = dict(zip(k, v))

while 1:
    s = sys.stdin.readline().rstrip()

    if s == '':
        break

    new_s = ''

    for ss in s:
        if ss == ' ':
            new_s += ' '
        else:
            new_s += matched_key[ss]

    print(new_s)