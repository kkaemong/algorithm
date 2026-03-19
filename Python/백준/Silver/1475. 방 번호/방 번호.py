room = list(map(int,(input())))

counts = [0] * 10

for num in room:
    if num == 9:
        counts[6] += 1  # 9가 나오면 6의 개수를 올립니다.
    else:
        counts[num] += 1  # 나머지 숫자는 자기 자리의 개수를 올립니다.

# 6과 9는 서로 호환되므로, 2개가 모여야 1세트가 더 필요합니다.
# (개수 + 1) // 2 를 해주면 홀수일 때 올림 처리가 깔끔하게 됩니다.
counts[6] = (counts[6] + 1) // 2

# 필요한 최소 세트 수는 카운트된 숫자들 중 가장 큰 값
print(max(counts))