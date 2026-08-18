T = 10
for tc in range(1, T + 1):
    N = int(input())
    tokens = list(input())

    priority = {
        '+': 1,
        '*': 2,
    }

    stack = []
    result = []

    for token in tokens:
        if token.isdigit():
            result.append(token)
        else:
            while stack and priority[stack[-1]] >= priority[token]:
                result.append(stack.pop())
            stack.append(token)
    while stack:
        result.append(stack.pop())

    for i in result:
        if i.isdigit():
            i = int(i)
            stack.append(i)
        else:
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a + b)
            elif i == '*':
                stack.append(a * b)

    print(f'#{tc} {stack.pop()}')