j = map(int, input().split())
s = map(int, input().split())

j_score = 0
s_score = 0

is_lead = []

for jj, ss in zip(j, s):
    j_score += jj
    
    if s_score < j_score:
        is_lead.append('1')
    elif j_score < s_score:
        is_lead.append('0')

    s_score += ss

if s_score < j_score:
    is_lead.append('1')
elif j_score < s_score:
    is_lead.append('0')
    
lead_list = ''.join(is_lead)

if j_score < s_score:
    if '10' in lead_list:
        print('Yes')
    else:
        print('No')
else:
    print('No')