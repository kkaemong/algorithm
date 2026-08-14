T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = list(input())
    stack = []

    for token in arr:
        if token.isdigit():
            token = int(token)
            stack.append(token)
        elif len(stack) == 2:
            a = stack.pop()
            b = stack.pop()
            if token == '+':
                stack.append(a + b)

    print(f'#{tc} {sum(stack)}')