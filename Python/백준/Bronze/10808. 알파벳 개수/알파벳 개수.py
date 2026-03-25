S = input()

# 2. 결과 저장용 리스트 (26개)
arr = [0] * 26

# 3. 문자열을 돌며 즉시 인덱스 계산
for char in S:
    # ord(char) - ord('a')를 하면
    # 'a'는 0, 'b'는 1, 'c'는 2... 가 나옵니다.
    idx = ord(char) - ord('a')
    arr[idx] += 1

# 4. 결과 출력
print(*arr)