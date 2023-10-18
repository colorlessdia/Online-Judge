def solution(common):
    c = [common[i + 1] - common[i] for i in range(len(common) - 1)]
    
    end = 0
    
    if c.count(c[0]) == len(c):
        end = common[-1] + c[-1]
    else:
        end = common[-1] * (c[1] / c[0])
    
    return end