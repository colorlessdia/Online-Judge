import sys

code_dict_key = ['TT', 'TX', 'PR', 'RT', 'AP', 'PX']
code_dict_value = [75, 50, 80, 30, 25, 60]
code_dict = dict(zip(code_dict_key, code_dict_value))

while 1:
    w, n = map(int, sys.stdin.readline().rstrip().split())
    
    if w == 0 and n == 0: break
    
    point_dict = dict()
    
    for _ in range(n):
        name, code = sys.stdin.readline().rstrip().split()
        
        if name in point_dict:
            point_dict[name] += code_dict[code]
        else:
            point_dict[name] = code_dict[code]
    
    chk = [k for k, v in point_dict.items() if 100 <= v]
    
    if len(chk) != 0:
        chk_list = (',').join(chk)
        print(f'Week {w} {chk_list}')
    else:
        print(f'Week {w} No phones confiscated')