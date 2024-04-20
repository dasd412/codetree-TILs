from sortedcontainers import SortedSet
import sys

ss=SortedSet()

n=int(input())
arr = list(map(int, input().split()))
ss.add(0)

answer=sys.maxsize
for elem in arr:

    ss.add(elem)

    right=ss.bisect_right(elem)
    left=ss.bisect_left(elem)-1

    right_length=ss[right]-elem if right<len(ss) else sys.maxsize
    left_length=elem-ss[left] if 0<=left<len(ss) else sys.maxsize

    answer=min(answer,left_length,right_length)

    print(answer)