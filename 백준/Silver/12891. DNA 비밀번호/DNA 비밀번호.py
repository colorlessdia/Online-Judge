S, P = map(int, input().split())
DNA = input()
A, C, G, T = map(int, input().split())

DNA_count = dict(zip(['A', 'C', 'G', 'T'], [0] * 4))

for char in DNA[:P]:
    DNA_count[char] += 1

count = 0

start = 0
end = P - 1

while True:
    if all([
        A <= DNA_count['A'],
        C <= DNA_count['C'],
        G <= DNA_count['G'],
        T <= DNA_count['T'],
    ]):
        count += 1

    if 0 < DNA_count[DNA[start]]:
        DNA_count[DNA[start]] -= 1

    start += 1
    end += 1

    if S <= end:
        break
    
    DNA_count[DNA[end]] += 1

print(count)