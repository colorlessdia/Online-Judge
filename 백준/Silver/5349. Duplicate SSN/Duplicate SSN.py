import sys

cnt_dict = dict()

while 1:
    ssn = sys.stdin.readline().rstrip()
    
    if ssn == '000-00-0000': break
    
    if ssn in cnt_dict:
        cnt_dict[ssn] += 1
    else:
        cnt_dict[ssn] = 1
    
for data in sorted([k for k, v in cnt_dict.items() if 1 < v]):
    print(data)