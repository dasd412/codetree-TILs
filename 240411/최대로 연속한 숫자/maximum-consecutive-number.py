from sortedcontainers import SortedSet

n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))

# 지워지는 것을 관리하는 자료구조. <- n이 10^9이므로 전체를 관리하게 되면 메모리 초과가 나므로 지워지는 것만 관리함.
removed=SortedSet()
removed.add(-1)
removed.add(n+1)

# (-구간의 길이, 시작 숫자, 끝 숫자) <- 내림 차순을 위해 - 구간의 길이를 함.
area=SortedSet()
area.add((-(n+1),-1,n+1))

for x in arr:
    # 지워진 것 중 왼쪽과 오른쪽을 각각 찾자.
    left=removed.bisect_left(x)-1
    right=removed.bisect_right(x)

    # 해설에서 감탄했던 부분. 구간을 이용한 풀이가 신기하다.
    area.remove((-(removed[right]-removed[left]-1),removed[left],removed[right]))

    area.add((-(x-removed[left]-1),removed[left],x))
    area.add((-(removed[right]-x-1),x,removed[right]))

    removed.add(x)

    print(-area[0][0])