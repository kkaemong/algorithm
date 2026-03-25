N = int(input())
cnt = 0

while N >= 0:
    # 1. 일단 5로 나누어떨어지는지 확인!
    if N % 5 == 0:
        cnt += (N // 5)  # 5로 다 나눠버리고
        print(cnt)  # 정답 출력 후 종료
        break

    # 2. 5로 안 나눠지면 3kg 봉지 하나를 쓴다
    N -= 3
    cnt += 1
else:
    # 3. N이 0보다 작아질 때까지 5의 배수를 못 만났다면 실패
    print(-1)