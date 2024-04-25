n,m = list(map(int, input().split()))

# 최소 소요 시간 1초 ~ 최대 소요 시간 n * 모든 통로 소요 시간
start=1
end=0

arr=[]
for i in range(m):
    num=int(input())
    arr.append(num)

    end+=(num*n)

answer=end

while start<=end:
    mid=(start+end)//2

    count=0
    for num in arr:
        count+=(mid//num)

    if count>=n:
        answer=min(answer,mid)
        end=mid-1
    else:
        start=mid+1

print(answer)