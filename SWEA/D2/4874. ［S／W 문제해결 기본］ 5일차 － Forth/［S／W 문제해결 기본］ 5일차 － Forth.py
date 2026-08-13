T = int(input())
for tc in range(1, T + 1):
    forth = input().split()
    stack = []
    error = False

    for token in forth:
        if token == '.':
            break

        if token.isdigit():   # 음수도 숫자로 처리
            stack.append(int(token))
        else:
            if len(stack) < 2:
                error = True
                break
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)

    if error or len(stack) != 1:
        print(f'#{tc} error')
    else:
        print(f'#{tc} {stack.pop()}')