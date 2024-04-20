from sortedcontainers import SortedSet
import sys

ss=SortedSet()

n=int(input())
arr = list(map(int, input().split()))
ss.add(0)

for elem in arr:
    ss.add(elem)

    answer=sys.maxsize

    for x in ss:
        index=ss.bisect_right(x)
        if index<len(ss):
            answer=min(answer,ss[index]-x)

    print(answer)