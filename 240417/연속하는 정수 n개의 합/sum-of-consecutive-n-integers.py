n,m=list(map(int,input().split()))
arr=list(map(int,input().split()))

left=0
right=0

answer=0

val=arr[right]

while right<n:
    if val<m:
        right+=1
        if right<n:
            val+=arr[right]
    else:
        if val==m:
            answer+=1
        val-=arr[left]
        left+=1

while left<n:
    if val>=m:
        if val==m:
            answer+=1
        val-=arr[left]
        left+=1
    else:
        break

print(answer)