import sys

N, M = map(int, sys.stdin.readline().split())

DNA_list = [0] * N
nucleotide_count = [[0] * 4 for _ in range(M)]
matched_index = dict(zip(list('ACGT'), range(4)))
matched_nucleotide = dict(zip(range(4), list('ACGT')))

for i in range(N):
    DNA = sys.stdin.readline().rstrip()

    DNA_list[i] = DNA

    for order, nucleotide in enumerate(DNA):
        index = matched_index[nucleotide]

        nucleotide_count[order][index] += 1

optimized_DNA = ''

for count_list in nucleotide_count:
    maximum_count = -1
    nucleotide_index = -1

    for j in range(4):
        
        if maximum_count < count_list[j]:
            maximum_count = count_list[j]
            nucleotide_index = j

    optimized_DNA += matched_nucleotide[nucleotide_index]

hamming_distance = 0

for DNA in DNA_list:
    
    for k in range(M):
        
        if DNA[k] != optimized_DNA[k]:
            hamming_distance += 1

print(optimized_DNA)
print(hamming_distance)