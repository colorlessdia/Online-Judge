def solution(quiz):
    answer = []
    
    for q in quiz:
        qq, aa = q.split('=')
        
        if eval(qq) == int(aa):
            answer.append('O')
        else:
            answer.append('X')
    
    return answer