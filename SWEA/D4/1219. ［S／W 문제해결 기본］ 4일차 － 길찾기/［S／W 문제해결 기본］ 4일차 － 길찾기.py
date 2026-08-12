T = 10
for _ in range(1, T + 1):
    tc, E = map(int,input().split())
    arr = list(map(int,input().split()))

    graph = [[] for _ in range(100)]

    for i in range(0,len(arr),2):
        a, b = arr[i], arr[i + 1]
        graph[a].append(b)

    visited = [False] * 100
    stack = [0]
    visited[0]  = True
    flag = False

    while stack:
        ans = stack.pop()

        if ans == 99:
            flag = True
            break

        for i in graph[ans]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
    print(f'#{tc} {1 if flag else 0}')