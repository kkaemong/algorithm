def solution(s):
    target = s.lower()
    a = target.count("y")
    b = target.count("p")
    if a == b or a == b == 0:
        return True
    else:
        return False