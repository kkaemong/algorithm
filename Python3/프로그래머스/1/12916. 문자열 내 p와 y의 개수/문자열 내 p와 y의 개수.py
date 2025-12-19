def solution(s):
    target = s.lower()
    a = target.count("y")
    b = target.count("p")
    if a == b:
        return True
    else:
        return False
print(solution("Pyy"))