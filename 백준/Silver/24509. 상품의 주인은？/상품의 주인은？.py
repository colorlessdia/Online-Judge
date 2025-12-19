import sys
from heapq import heappush, heappop

def find_student(pq):

    while True:
        _, student = heappop(pq)

        if student in student_set:
            continue

        student_set.add(student)

        return student

input = sys.stdin.readline

N = int(input())

A_heap = []
B_heap = []
C_heap = []
D_heap = []

for _ in range(N):
    X, A, B, C, D = map(int, input().split())

    heappush(A_heap, (-A, X))
    heappush(B_heap, (-B, X))
    heappush(C_heap, (-C, X))
    heappush(D_heap, (-D, X))

student_set = set()
student_list = [find_student(pq) for pq in [A_heap, B_heap, C_heap, D_heap]]

print(*student_list)