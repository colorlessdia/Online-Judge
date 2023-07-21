import sys

n, m = map(int, input().split())
pwd_dict = dict()

for _ in range(n):
    addr, pwd = sys.stdin.readline().rstrip().split()
    
    pwd_dict[addr] = pwd
    
for _ in range(m):
    target = sys.stdin.readline().rstrip()
    
    print(pwd_dict[target])
