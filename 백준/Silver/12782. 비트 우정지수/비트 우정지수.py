import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = input().rstrip().split()

    n_count = [0] * 2
    m_count = [0] * 2

    for n, m in zip(N, M):
        
        if n == m:
            continue
        
        if n == '0':
            n_count[0] += 1
        elif n == '1':
            n_count[1] += 1
        
        if m == '0':
            m_count[0] += 1
        elif m == '1':
            m_count[1] += 1
    
    n_0, n_1 = n_count
    m_0, m_1 = m_count
    

    print(max(n_0, n_1))