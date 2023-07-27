import sys

mirror_dict = dict(zip('bdpqiovwx', 'dbqpiovwx'))

while 1:
    s = sys.stdin.readline().rstrip()
    
    if s == '#': break
    
    rs = s[::-1]
    mirror_char = ''
    
    for c in rs:
        if c in mirror_dict:
            mirror_char += mirror_dict[c]

    if len(mirror_char) != len(s):
        print('INVALID')
        continue

    print(mirror_char)