n1 = int(input())
n2 = int(input())

sequence = [n1, n2]

while True:
    t2 = sequence[-2]
    t1 = sequence[-1]
    tn = t2 - t1

    sequence.append(tn)

    if sequence[-2] < tn:
        break

print(len(sequence))