N = int(input())

for _ in range(N):
    a,b = input().split()
    if sorted(a) == sorted(b):
        print('Possible')
    else:
        print('Impossible')