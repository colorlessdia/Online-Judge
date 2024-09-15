import sys

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = sys.stdin.readline().rstrip().split()

    if ''.join(sorted(A)) == ''.join(sorted(B)):
        print(f'{A} & {B} are anagrams.')
        continue
    
    print(f'{A} & {B} are NOT anagrams.')