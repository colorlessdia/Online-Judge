import sys

score_dict = dict(zip('A+ A0 A- B+ B0 B- C+ C0 C- D+ D0 D- F'.split(), map(float, '4.3 4.0 3.7 3.3 3.0 2.7 2.3 2.0 1.7 1.3 1.0 0.7 0.0'.split())))

total = 0
credit = 0

for _ in range(int(input())):
    a, b, c = sys.stdin.readline().rstrip().split()
    
    credit += float(b)
    total += float(b) * float(score_dict[c])
    
score = total / credit

if len(str(score).split('.')) == 2:
    d, f = str(score).split('.')
    
    if len(f) == 3 and 4 < int(f[2]):
        print(float(d + '.' + str(int(f[:2]) + 1)))
    else:
        print(f'{score:.2f}')
else:
    print(f'{score:.2f}')