T = 10
for tc in range(1, T + 1):
    N = int(input())
    tokens = list(input())

    stack = []
    result = []

    for token in tokens:
        if token.isdigit():
            result.append(token)
        else:
            while stack and stack[-1] == '+':
                result.append(stack.pop())
            stack.append(token)
    while stack:
        result.append(stack.pop())

    for i in result:
        if i.isdigit():
            i = int(i)
            stack.append(i)
        else:
            if i == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)

    print(f'#{tc} {stack.pop()}')