T = int(input())
for tc in range(1,T+1):
   arr = list(input())
   brr = list(reversed(arr))
   if brr == arr:
       print(f'#{tc} {1}')
   else:
       print(f'#{tc} {0}')