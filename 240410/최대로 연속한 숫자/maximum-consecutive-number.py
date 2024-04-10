from sortedcontainers import SortedSet

ss=SortedSet()

n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))

# O(n)
for i in range(0,n+1):
    ss.add(i)

# O(mn)으로 하면 10^14이므로 너무 크다. 시간초과가 난다.
# O(m)은 절대로 줄일 수 없는 상수이므로 O(log n) 풀이가 필요하다. 즉, O(m log n)풀이를 해야 한다.
# 연속하여 나타난 수라는 것은 어찌보면 범위라고 할 수 있다. 길이에 대한 파라메트릭 서치가 되지 않을까 싶다.
for i in range(m):
    ss.remove(arr[i]) # O(log n)

    # 길이의 범위는 최소 1에서 최대 len(ss)
    start=1
    end=len(ss)

    answer=1

    while start<=end:
        mid=(start+end)//2

        is_ok=False
        
        for j in range(len(ss)-mid):
            if ss[j+mid]==ss[j]+mid:
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