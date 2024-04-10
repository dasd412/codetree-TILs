from sortedcontainers import SortedSet

removed=SortedSet()

n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))


# O(mn)으로 하면 10^14이므로 너무 크다. 시간초과가 난다.
# O(m)은 절대로 줄일 수 없는 상수이므로 O(log n) 풀이가 필요하다. 즉, O(m log n)풀이를 해야 한다.
# 연속하여 나타난 수라는 것은 어찌보면 범위라고 할 수 있다. 길이에 대한 파라메트릭 서치가 되지 않을까 싶다.
for i in range(m):
    removed.add(arr[i])

    # 길이의 범위
    start=1
    end=n-len(removed)

    answer=1

    while start<=end:
        mid=(start+end)//2

        is_ok=False
        
        for j in range(n-mid+1):
            idx1=removed.bisect_left(j)
            idx2=removed.bisect_left(j+mid)

            if idx1<len(removed) and j<=removed[idx1]<=j+mid:
                continue
            if idx2<len(removed) and j<=removed[idx2]<=j+mid:
                continue

            is_ok=True
            break
            
        # 길이 mid로 수열을 만들 수 있다면, 더 길게 해보자.
        if is_ok:
            answer=max(answer,mid+1)
            start=mid+1
        # 길이 mid로 수열을 만들 수 없다면, 더 짧게 해야 한다.
        else:
            end=mid-1

    print(answer)