T = int(input())
for tc in range(T):
    K, N, M, = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    brr = [1] + [0] * N

    for i in arr:
        brr[i] += 1

    cnt = 0
    current = 0

    while current + K < N:
        flag = False  # 이번에 충전소를 찾았는지 체크할 신호등

        for step in range(K, 0, -1):
            if brr[current + step] == 1:
                current += step
                cnt += 1
                flag = True  # 충전소 찾음!
                break

        # for문을 다 돌았는데도 flag가 False라면?
        if not flag:
            cnt = 0  # 종점까지 못 가니까 0 처리
            break  # 탈출!

    print(f'#{tc + 1} {cnt}')