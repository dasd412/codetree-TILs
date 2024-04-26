n,m,k= list(map(int, input().split()))

arr=[[0]*m for _ in range(n)]

for i in range(n):
    s=list(input())
    for j in range(m):
        arr[i][j]=s[j]

a=[[0]*(m+1) for _ in range(n+1)]
b=[[0]*(m+1) for _ in range(n+1)]
c=[[0]*(m+1) for _ in range(n+1)]

def make_prefix_sum(ch,d:list[list[int]])->list[list[int]]:
    count=0
    for i in range(1,n+1):
        if arr[i-1][0]==ch:
            count+=1
        d[i][1]=count
    
    count=0
    for j in range(1,m+1):
        if arr[0][j-1]==ch:
            count+=1
        d[1][j]=count

    for i in range(2,n+1):
        for j in range(2,n+1):
            d[i][j]=d[i][j-1]+d[i-1][j]-d[i-1][j-1]
            if arr[i-1][j-1]==ch:
                d[i][j]+=1
        
    return d

def get_count(r1,c1,r2,c2,d:list[list[int]])->int:
    return d[r2][c2]-d[r1-1][c2]-d[r2][c1-1]+d[r1-1][c1-1]

aa=make_prefix_sum('a',a)
bb=make_prefix_sum('b',b)
cc=make_prefix_sum('c',c)

for i in range(k):
    r1,c1,r2,c2= list(map(int, input().split()))

    a_count=get_count(r1,c1,r2,c2,aa)
    b_count=get_count(r1,c1,r2,c2,bb)
    c_count=get_count(r1,c1,r2,c2,cc)
    
    print(str(a_count)+' '+str(b_count)+' '+str(c_count))