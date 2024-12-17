S, K = input().split()
S = S.lower()
K = int(K)

string_range_list = []

s = 0
e = 0

while True:

    if s == e:
        e += 1
    
    if len(S) <= e:
        string_range_list.append(S[s:e])
        break
    
    if S[s] == S[e]:
        e += 1
        continue
    
    string_range_list.append(S[s:e])

    s = e
    e = s + 1

alphabat_count = dict()

ciphertext = ''

for string_range in string_range_list:
    alphabat = string_range[0]

    if alphabat in alphabat_count:
        continue
    
    alphabat_count[alphabat] = 1
    
    if K <= len(string_range):
        ciphertext += '1'
    else:
        ciphertext += '0'

print(ciphertext)