T = int(input())
for tc in range(1, T + 1):
    arr = input()

    pairs = {')': '(', '}': '{'}

    stack = []
    isvalid = True
    for brack in arr:
        if brack in '({':
            stack.append(brack)
        elif brack in ')}':
            if not stack:
                isvalid = False
                break
            else:
                top = stack.pop()
                if top != pairs[brack]:
                    isvalid = False
                    break

    if isvalid and not stack:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')