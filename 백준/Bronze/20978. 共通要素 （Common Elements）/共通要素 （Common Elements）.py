N, M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

common_element_set = sorted(set(A for A in A_list if A in B_list))

for common_element in common_element_set:
    print(common_element)