N, K = map(int, input().split())

# 2. 학생 수를 저장할 표(2차원 리스트) 만들기
# 성별 2가지(0:여, 1:남) x 학년 6가지(1~6학년)
# 인덱스를 편하게 쓰기 위해 7칸을 만듭니다 (0번 인덱스는 안 씀)
students = [[0] * 7 for _ in range(2)]

# 3. 학생 정보 입력받아 카운트하기
for _ in range(N):
    s, y = map(int, input().split())  # s: 성별, y: 학년
    students[s][y] += 1

# 4. 필요한 방의 개수 계산하기
room_count = 0

for gender in range(2):  # 성별(0, 1) 반복
    for grade in range(1, 7):  # 학년(1~6) 반복
        count = students[gender][grade]

        if count > 0:
            # 방 개수 계산 로직
            # 인원수를 K로 나눴을 때 딱 떨어지면 그 몫만큼,
            # 나머지가 있으면 몫에 +1을 해줍니다.
            if count % K == 0:
                room_count += (count // K)
            else:
                room_count += (count // K) + 1

# 5. 최종 결과 출력
print(room_count)