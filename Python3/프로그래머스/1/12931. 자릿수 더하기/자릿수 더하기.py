def solution(n):
    n = list(str(n))
    answer = 0

    for i in n:
        i = int(i)
        answer += i
    return answer

def solution(n):
    temp = [int(i) for i in str(n)]
    answer = sum(temp)
    return answer

def solution(n):
    temp = list(map(int, list(str(n))))
    answer = sum(temp)
    return answer
