def solution(num):
    answer = 0
    if num == 1:
        return answer
    while True:
        if answer == 500:
            answer = -1
            return answer
        if num % 2 == 0:
            num = num // 2
            answer += 1
            if num == 1:
                break
        elif num % 2 == 1:
            num = (num * 3) + 1
            answer += 1
            if num == 1:
                break
    return answer
print(solution(6))
