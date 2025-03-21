def calc_NOP_count(string):
    length = len(string)

    if length % 4 == 0:
        return 0
    
    return 4 - (length % 4)

S = input()

temp = S[0]
NOP_count = 0

for i in range(1, len(S)):
    char = S[i]

    if char.islower():
        temp += char
    else:
        NOP_count += calc_NOP_count(temp)
        temp = char

print(NOP_count)