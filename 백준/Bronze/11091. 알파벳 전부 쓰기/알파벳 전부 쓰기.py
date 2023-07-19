import sys
import string

for _ in range(int(input())):
    alpha_lower = string.ascii_lowercase
    alpha_dict = dict(zip(alpha_lower, [0] * len(alpha_lower)))
    
    s = sys.stdin.readline().rstrip().lower()
    
    for ss in s:
        if ss in alpha_dict:
            alpha_dict[ss] += 1
    
    result = sorted([k for k, v in alpha_dict.items() if v == 0])
    
    if len(result) == 0:
        print('pangram')
    else:
        print(f'missing {"".join(result)}')