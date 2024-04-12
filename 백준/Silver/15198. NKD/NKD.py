import sys
from collections import deque

k = int(sys.stdin.readline())
n = int(sys.stdin.readline())

NKD = deque()

for _ in range(n):
    document_name = sys.stdin.readline().rstrip()

    if document_name in NKD:
        NKD.remove(document_name)
        NKD.append(document_name)
    else:
        NKD.append(document_name)

        if k < len(NKD):
            NKD.popleft()

for document_name in reversed(NKD):
    print(document_name)