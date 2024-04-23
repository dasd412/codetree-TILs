n,m=list(map(int,input().split()))

arr=[]

for i in range(n):
    num=int(input())
    arr.append(num)

start=1
end=max(arr)

answer=0

#그래프를 그려보면 단조 감소 형태를 띈다.
while start<=end:
    mid=(start+end)//2

    count=0
    for elem in arr:
        count+=(elem//mid)

    if count>=m:
        answer=max(answer,mid)
        start=mid+1
    else:
        end=mid-1

print(answer)