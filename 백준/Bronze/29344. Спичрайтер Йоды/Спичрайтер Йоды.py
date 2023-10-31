import sys

s = sys.stdin.read().split('.')[:-1]

ss = [ss.split() for ss in s]

ssss = ''

for sss in ss:
    l = list(reversed(sss))
    
    l[-1] += '.'
    ll = ' '.join(l)
    
    ssss += ll
    ssss += ' '

print(ssss[:-1])