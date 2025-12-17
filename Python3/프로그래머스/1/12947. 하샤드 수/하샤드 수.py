def solution(x):
    number = str(x)
    nb = int(number)
    t = sum(list(map(int, list(str(x)))))
    if nb % t == 0:
        return True
    else:
        return False
print(solution(11))