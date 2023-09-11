import sys

for i in range(1, int(input()) + 1):
    text_list = list(reversed(sys.stdin.readline().rstrip().split()))
    join_text = ' '.join(text_list)
    
    print(f'Case #{i}: {join_text}')