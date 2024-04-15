n,m,k = list(map(int, input().split()))

arr=[['']*m for _ in range(n)]

for i in range(n):
    split=list(input())
    for j in range(m):
        arr[i][j]=split[j]

a=[[0]*(m+1)for _ in range(n+1)]
b=[[0]*(m+1)for _ in range(n+1)]
c=[[0]*(m+1)for _ in range(n+1)]

a_val=0
b_val=0
c_val=0

for j in range(1,n+1):
    if arr[0][j-1]=='a':
        a_val+=1

    elif arr[0][j-1]=='b':
        b_val+=1

    elif arr[0][j-1]=='c':
        c_val+=1

    a[1][j]=a_val
    b[1][j]=b_val
    c[1][j]=c_val

a_val=0
b_val=0
c_val=0

for i in range(1,n+1):
    if arr[i-1][0]=='a':
        a_val+=1

    elif arr[i-1][0]=='b':
        b_val+=1

    elif arr[i-1][0]=='c':
        c_val+=1

    a[i][1]=a_val
    b[i][1]=b_val
    c[i][1]=c_val

for i in range(2,n+1):
    for j in range(2,m+1):
        a[i][j]=a[i-1][j]+a[i][j-1]-a[i-1][j-1] 
        if arr[i-1][j-1]=='a':
            a[i][j]+=1

        b[i][j]=b[i-1][j]+b[i][j-1]-b[i-1][j-1]

        if arr[i-1][j-1]=='b':
            b[i][j]+=1

        c[i][j]=c[i-1][j]+c[i][j-1]-c[i-1][j-1]

        if arr[i-1][j-1]=='c':
            c[i][j]+=1

for _ in range(k):
    r1,c1,r2,c2=list(map(int, input().split()))

    a_cnt=a[r2][c2]-a[r2][c1-1]-a[r1-1][c2]+a[r1-1][c1-1]
    b_cnt=b[r2][c2]-b[r2][c1-1]-b[r1-1][c2]+b[r1-1][c1-1]
    c_cnt=c[r2][c2]-c[r2][c1-1]-c[r1-1][c2]+c[r1-1][c1-1]

    print(str(a_cnt)+' '+str(b_cnt)+' '+str(c_cnt))