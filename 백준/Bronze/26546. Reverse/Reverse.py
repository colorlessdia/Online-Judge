import sys

for _ in range(int(input())):
    word, s, e = sys.stdin.readline().rstrip().split()
    
    s, e = int(s), int(e)
    
    print(word[:s] + word[e:])