T = int(input())
for tc in range(T):
    N = int(input())
    cnts = [0]*5001
    for _ in range(N):
        S,E = map(int,input().split())
        for i in range(S,E+1):
            cnts[i] +=1

    P = int(input())
    sols = []
    for _ in range(P):
        t = int(input())
        sols.append(cnts[t])


    print(f'#{tc+1}', *sols)