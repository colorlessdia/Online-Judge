def solution(n):
    is_odd = True if n % 2 == 1 else False

    if is_odd:
        return sum([i for i in range(1, n + 1) if i % 2 == 1])
    else:
        return sum([i ** 2 for i in range(1, n + 1) if i % 2 == 0])