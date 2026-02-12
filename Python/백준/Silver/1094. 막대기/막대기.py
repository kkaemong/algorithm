X = int(input())
sticks = [64]  # 처음엔 64cm 막대 하나만 있음

while sum(sticks) > X:
    # 1. 가장 짧은 것을 꺼내서 반으로 자른다
    sticks.sort()  # 가장 짧은 걸 찾기 위해 정렬
    shortest = sticks.pop(0)
    half = shortest // 2

    # 2. 자른 것 중 하나(half)와 나머지의 합을 비교한다
    # sum(sticks)는 이미 shortest가 빠진 상태이므로 남은 것들의 합임
    if sum(sticks) + half >= X:
        # 합이 X보다 크거나 같으면, 나머지 반쪽은 버리고 하나만 다시 넣음
        sticks.append(half)
    else:
        # 합이 X보다 작으면, 자른 두 개를 모두 다시 넣음
        sticks.append(half)
        sticks.append(half)

print(len(sticks))  # 남은 막대 개수 출력