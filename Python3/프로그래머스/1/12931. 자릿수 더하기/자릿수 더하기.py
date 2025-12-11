def solution(n):
    n = list(str(n))
    answer = 0

    for i in n:
        i = int(i)
        answer += i
    return answer
print(solution(123))