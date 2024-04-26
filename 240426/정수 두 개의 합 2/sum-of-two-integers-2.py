n,k=list(map(int, input().split()))

arr=[]

for i in range(n):
    num=int(input())
    arr.append(num)

arr.sort()

answer=0

for left in range(n):

    right=left+1

    while right<n:
        if arr[left]+arr[right]<=k:
            answer+=1
        else:
            break
        right+=1
    
print(answer)