T = 10
for tc in range(1, 11):
    N= int(input())
    arr = input()

    pair = {')': '(', ']': '[', '}': '{', '>': '<'}

    flag = True
    stack = []
    for ch in arr:
        if ch in '({[<':
            stack.append(ch)
        elif ch in ')}]>':
            if not stack or stack[-1] != pair[ch]:
                flag = False
                break
            else:
                stack.pop()

    if not stack and flag:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')