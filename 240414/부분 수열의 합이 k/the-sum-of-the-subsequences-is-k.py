n,k = list(map(int, input().split()))
arr = list(map(int, input().split()))

prefix_sum=[0]*(n+1)

val=0
for i in range(1,n+1):
    val+=arr[i-1]
    prefix_sum[i]=val

answer=0

# 10^3 * 10^3=10^6이므로 충분한 시간복잡도.
# 구간 크기
for area in range(1,n+1):
    for i in range(area,n+1):
        sums=prefix_sum[i]-prefix_sum[i-area]
        if sums==k:
            answer+=1

print(answer)