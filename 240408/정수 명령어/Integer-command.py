from sortedcontainers import SortedSet

ss=SortedSet()

t=int(input())

for i in range(t):
    k=int(input())

    for j in range(k):
        op = list(input().split())

        if op[0]=='I':
            ss.add(int(op[1]))
        elif op[0]=='D' and op[1]=='1':
            if len(ss):
                ss.remove(ss[-1])
        elif op[0]=='D' and op[1]=='-1':
            if len(ss):
                ss.remove(ss[0])

    if len(ss):
        print(str(ss[-1])+' '+str(ss[0]))
    else:
        print('EMPTY')