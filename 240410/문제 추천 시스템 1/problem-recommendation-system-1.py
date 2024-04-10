from sortedcontainers import SortedSet

ss=SortedSet()

n=int(input())

for i in range(n):
    p,l = list(map(int, input().split()))
    ss.add((l,p)) # 난이도 순, 문제 번호 순으로 정렬

m=int(input())

for i in range(m):
    op=list(input().split())

    if op[0]=='rc':
        if op[1]=='1':
            print(ss[-1][1])

        elif op[1]=='-1':
            print(ss[0][1])

    elif op[0]=='ad':
        p,l=int(op[1]),int(op[2])
        ss.add((l,p))
    
    elif op[0]=='sv':
        p,l=int(op[1]),int(op[2])
        ss.remove((l,p))