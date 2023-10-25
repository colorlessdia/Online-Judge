a = input().split()
b = input()

print(len([aa for aa in a if aa[:len(b)] == b and aa != b]))