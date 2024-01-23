while True:
    try:
        N, K = map(int, input().split())

        chicken = N

        while True:
            if N // K == 0:
                break
            
            chicken += N // K
            N = (N // K) + N % K

        print(chicken)
    except:
        break