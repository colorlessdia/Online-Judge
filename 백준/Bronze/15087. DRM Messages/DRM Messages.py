def calc_ord(char):
    return ord(char) - ord('A')

def rotate_ord(char, value):
    return (calc_ord(char) + value) % 26

S = input()

U_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

L = len(S)
H = L // 2

FS = S[:H]
BS = S[H:]

F_N = sum([calc_ord(f) for f in FS])
B_N = sum([calc_ord(b) for b in BS])

F_list = [U_list[rotate_ord(f, F_N)] for f in FS]
B_list = [U_list[rotate_ord(b, B_N)] for b in BS]

DRM_message = []

for F, B in zip(F_list, B_list):
    DRM_message.append(U_list[rotate_ord(F, calc_ord(B))])

print(''.join(DRM_message))