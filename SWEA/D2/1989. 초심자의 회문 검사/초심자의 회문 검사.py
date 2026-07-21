T = int(input())
for tc in range(1,T+1):
   arr = list(input())
   
   # 풀이방법 1
   brr = list(reversed(arr))
   if brr == arr:
       print(f'#{tc} {1}')
   else:
       print(f'#{tc} {0}')
      
 # 풀이방법 2
   brr = arr[:]
   brr.reverse()

   if brr == arr:
       print(f'#{tc} {1}')
   else:
       print(f'#{tc} {0}')
      
# 풀이방법 3
   if arr == arr[::-1]:
       print(f'#{tc} {1}')
   else:
       print(f'#{tc} {0}')
