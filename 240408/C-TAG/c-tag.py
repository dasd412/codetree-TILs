n,m = list(map(int, input().split()))

a=[]
for _ in range(n):
    s=input()
    a.append(s)

b=[]
for _ in range(n):
    s=input()
    b.append(s)

answer=0
#O(50^3*500)<O(10^8)
for i in range(m):
    for j in range(i+1,m):
        for k in range(j+1,m):

            a_set=set()
            b_set=set()

            for x in range(n):
                a_set.add(a[x][i]+a[x][j]+a[x][k])
                b_set.add(b[x][i]+b[x][j]+b[x][k])
                
            if len(a_set&b_set)==0:
                answer+=1


print(answer)