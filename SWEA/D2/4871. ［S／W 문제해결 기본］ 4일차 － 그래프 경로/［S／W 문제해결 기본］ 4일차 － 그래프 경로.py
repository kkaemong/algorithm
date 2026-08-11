T = int(input())
for tc in range(1, T + 1):
    V, E = map(int,input().split())

    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)

    S,G = map(int,input().split())

    visited = [False] * (V+1)
    stack = [S]
    ans = []
    flag = False

    while stack:
        now = stack.pop()
        if now == G:
            flag = True
            break
        if visited[now]:
            continue
        visited[now] = True
        ans.append(now)

        for next_v in graph[now]:
            if not visited[next_v]:
                stack.append(next_v)
    if flag:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')