def solution(s):
    sort_list = list(map(str, sorted(list(map(int, s.split())))))
    
    return ' '.join([sort_list[0], sort_list[-1]])