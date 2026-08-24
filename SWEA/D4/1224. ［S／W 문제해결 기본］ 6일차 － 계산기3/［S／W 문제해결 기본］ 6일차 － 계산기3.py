T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = input()

    priority = {
        '+':1,
        '*':2,
    }

    stack = []
    result = []

    for i in arr:
        if i.isdigit():
            result.append(i)

        elif i == '(':
            stack.append(i)

        elif i == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

        else:
            while stack and stack[-1] != '(' and priority[stack[-1]] >= priority[i]:
                result.append(stack.pop())
            stack.append(i)

    while stack:
        result.append(stack.pop())

    calc = []
    for token in result:
        if token.isdigit():
            token = int(token)
            calc.append(token)
        else:
            b = calc.pop()
            a = calc.pop()
            if token == '+':
                calc.append(a + b)
            else:
                calc.append(a * b)

    print(f'#{tc} {calc[0]}')