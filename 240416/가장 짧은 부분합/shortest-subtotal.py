n,s= list(map(int, input().split()))
arr= list(map(int, input().split()))

answer=987654321

# 합이 S 미만이라면 right을 늘리고 S이상이라면 left를 줄이는 방식으로 푼다.
left=0
right=0

temp=0

while right<n:
    
    if temp<s:
        temp+=arr[right]
        right+=1
    else:
        answer=min(answer,right-left)
        temp-=arr[left]
        left+=1


if temp>=s:
    answer=min(answer,right-left)

while left<n:
    if temp>=s:
        answer=min(answer,right-left)
        temp-=arr[left]
        left+=1
    else:
        break

if answer==987654321:
    print(-1)
else:
    print(answer)
"""
테케
1. 가장 짧은 구간이 1인 경우
2. 왼쪽을 줄여서 가장 짧은 구간이 되는 경우 n= 6, s=5 , arr= [1,1,1,1,1,5], 값= 1
3. 오른쪽을 전부 가는 경우 
"""