import sys

def alphabet_ord(alphabet):
    return ord(alphabet) - ord('A')

input = sys.stdin.readline

T = int(input())

alphabet_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

for _ in range(T):
    keyword, plaintext = input().rstrip().split()
    lk, lp = len(keyword), len(plaintext)

    if lk < lp:
        keyword = (keyword + (keyword * (((lp - lk) // lk) + 1)))[:lp]

    ciphertext = []
    
    for k, p in zip(keyword, plaintext):
        index = (alphabet_ord(k) + alphabet_ord(p)) % 26
        ciphertext.append(alphabet_list[index])

    print(f'Ciphertext: {''.join(ciphertext)}')