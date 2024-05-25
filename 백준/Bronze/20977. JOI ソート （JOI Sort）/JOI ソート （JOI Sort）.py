N = int(input())
S = input()

sorted_S = sorted(S, key=lambda x: (x == 'J', x == 'O', x == 'I'), reverse=True)

print(''.join(sorted_S))