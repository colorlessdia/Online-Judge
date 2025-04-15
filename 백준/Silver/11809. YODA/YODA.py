N = input()
M = input()

maximum_length = max(len(N), len(M))

if len(N) == len(M):
    pass
elif len(N) < maximum_length:
    N = N.rjust(maximum_length, '0')
elif len(M) < maximum_length:
    M = M.rjust(maximum_length, '0')

n_list = list(map(int, list(N)))
m_list = list(map(int, list(M)))

n_count = maximum_length
m_count = maximum_length

for i in range(maximum_length):
    n = n_list[i]
    m = m_list[i]

    if n == m:
        continue
    
    if m < n:
        m_list[i] = -1
        m_count -= 1
        continue

    if n < m:
        n_list[i] = -1
        n_count -= 1
        continue

n_result = 'YODA' if n_count == 0 else int(''.join([str(n) for n in n_list if 0 <= n]))
m_result = 'YODA' if m_count == 0 else int(''.join([str(m) for m in m_list if 0 <= m]))

print(n_result)
print(m_result)