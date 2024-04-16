n=int(input())
arr = list(map(int, input().split()))

counts=[0]*(100001)

left=0
right=0

answer=0

while right<n:
    if counts[arr[right]]==0:
        counts[arr[right]]+=1
        answer=max(answer,right-left+1)
        right+=1
    else:
        counts[arr[left]]-=1
        left+=1

print(answer)