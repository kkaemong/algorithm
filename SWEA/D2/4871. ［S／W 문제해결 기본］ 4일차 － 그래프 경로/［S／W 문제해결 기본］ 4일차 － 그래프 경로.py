T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)

    S, G = map(int, input().split())

    visited = [False] * (V + 1)
    stack = [S]
    visited[S] = True
    flag = False

    while stack:
        now = stack.pop()

        if now == G:
            flag = True
            break

        for next_v in graph[now]:
            if not visited[next_v]:
                visited[next_v] = True
                stack.append(next_v)

    print(f'#{tc} {1 if flag else 0}')