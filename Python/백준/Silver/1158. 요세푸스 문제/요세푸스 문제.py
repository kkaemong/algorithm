from collections import deque

N, K = map(int, input().split())
queue = deque(range(1, N + 1))  # 1부터 N까지 줄 세우기
ans = []

while queue:
    # K-1번만큼 사람을 뒤로 보냅니다.
    for _ in range(K - 1):
        queue.append(queue.popleft())

    # K번째 사람은 완전히 제거해서 ans에 넣습니다.
    ans.append(str(queue.popleft()))

# 예쁘게 출력하기
print("<" + ", ".join(ans) + ">")