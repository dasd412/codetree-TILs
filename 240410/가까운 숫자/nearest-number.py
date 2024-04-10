from sortedcontainers import SortedSet
import sys

ss=SortedSet()

n=int(input())

arr = list(map(int, input().split()))

ss.add(0)

answer=sys.maxsize

for elem in arr:
    ss.add(elem)

    # elem 오른쪽을 찾는다.
    right_index=ss.bisect_right(elem)

    # elem 왼쪽을 찾는다.
    left_index=right_index-2

    right_length=ss[right_index]-elem if right_index<len(ss) else sys.maxsize
    left_length=elem-ss[left_index] if left_index>=0 else sys.maxsize
    
    answer=min(answer,right_length,left_length)

    print(answer)