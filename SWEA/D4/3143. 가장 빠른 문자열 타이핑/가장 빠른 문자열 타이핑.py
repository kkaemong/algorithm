T = int(input())
for tc in range(1, T + 1):
    a,b = input().split()

    d = list(a.replace(b,'c'))

    print(f'#{tc} {len(d)}')