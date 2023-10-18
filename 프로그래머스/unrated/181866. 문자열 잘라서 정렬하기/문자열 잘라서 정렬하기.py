def solution(myString):
    return sorted([s for s in myString.split('x') if len(s) != 0])