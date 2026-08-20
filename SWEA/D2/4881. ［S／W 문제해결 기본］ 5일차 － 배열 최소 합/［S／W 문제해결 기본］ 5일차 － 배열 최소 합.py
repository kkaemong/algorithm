def backtracking(total, idx):
    global result

    if total >= result:
        return

    if idx == N:
        result = min(total, result)
        return

    for i in range(N):
        if check[i]:
            continue
        check[i] = True
        backtracking(total + arr[idx][i], idx + 1)
        check[i] = False


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    check = [False] * N
    inf = float('inf')
    result = inf
    backtracking(0, 0)

    print(f'#{tc + 1} {result}')