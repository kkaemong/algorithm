def solution(s):
    s = list(map(int,s.split()))
    a = max(s)
    b = min(s)
    return str(b) + " " +str(a)