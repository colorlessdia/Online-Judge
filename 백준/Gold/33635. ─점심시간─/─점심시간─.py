import sys

def calc_bit(li, matched_dict):
    bit = 0
    
    for element in li:
        position = matched_dict[element]

        bit |= (1 << position)
    
    return bit

input = sys.stdin.readline

N = int(input())

genres = dict(zip(input().rstrip().split(), range(N)))

M = int(input())

books = dict()

for _ in range(M):
    line = input().rstrip().split()
    k, n, b_list = int(line[0]), line[1], line[2:]
    
    books[n] = calc_bit(b_list, genres)

Q = int(input())

values = books.values()

for _ in range(Q):
    line = input().rstrip().split()
    x, c_list = int(line[0]), line[1:]

    bit = calc_bit(c_list, genres)
    count = 0
    
    for value in values:
        
        if bit == (value & bit):
            count += 1
    
    print(count)