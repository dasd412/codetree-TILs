from sortedcontainers import SortedSet

n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))

# n이 10^9이므로 0부터 n까지를 관리하는 배열을 만들면 안된다. 메모리 초과

# (시작,끝)
area=SortedSet()
area.add((-(n+1),-1,n+1))

removed=SortedSet()
removed.add(-1)
removed.add(n+1)

for elem in arr:
    removed.add(elem)
    right_idx=removed.bisect_right(elem)
    left_idx=removed.bisect_left(elem)-1

    right=removed[right_idx]
    left=removed[left_idx]

    area.remove((-(right-left-1),left,right))

    area.add((-(elem-left-1),left,elem))
    area.add((-(right-elem-1),elem,right))
    print(-area[0][0])