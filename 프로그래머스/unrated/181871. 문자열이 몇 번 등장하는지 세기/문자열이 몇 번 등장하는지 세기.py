def solution(myString, pat):
    cnt = 0
    
    for i in range(len(myString) - 1):
        if pat == myString[i:i + len(pat)]:
            cnt += 1
    
    return cnt