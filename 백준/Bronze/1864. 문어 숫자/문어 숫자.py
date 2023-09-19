import sys

octo_dict = dict(zip('- \ ( @ ? > & % /'.split(), '0 1 2 3 4 5 6 7 -1'.split()))

while 1:
    s = sys.stdin.readline().rstrip()
    
    if s == '#': break
    
    octo_num = 0
    
    for i, o in enumerate([octo_dict[ss] for ss in s][::-1]):
        octo_num += int(o) * (8 ** i)
    
    print(octo_num)