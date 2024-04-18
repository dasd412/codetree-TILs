n,k=list(map(int,input().split()))

arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)

arr.sort()

# 제일 범위가 넓은 구간을 찾는다.
left=0
right=0
for i in range(len(arr)):
    if arr[left]+arr[i]<=k:
        right=i
        
answer=0
while left<right:
    # 정렬되어있으므로 맨 왼쪽 요소와 맨 오른쪽 요소를 합해서 k이하가 되면, 그 중간에 있는 것들도 모두 가능하다.
    if arr[left]+arr[right]<=k:
        answer+=(right-left)
    left+=1
    
    while left<right:
        if arr[left]+arr[right]<=k:
            break
        right-=1
    
print(answer)