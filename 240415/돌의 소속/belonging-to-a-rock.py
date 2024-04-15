n,q= list(map(int, input().split()))

a=[0]*(n+1)
b=[0]*(n+1)
c=[0]*(n+1)

a_val=0
b_val=0
c_val=0

for i in range(n):
    n=int(input())
    if n==1:
        a_val+=1
    elif n==2:
        b_val+=1
    elif n==3:
        c_val+=1
    
    a[i+1]=a_val
    b[i+1]=b_val
    c[i+1]=c_val


for i in range(q):
    s,e=list(map(int, input().split()))
    print(a[e]-a[s-1],end=' ')
    print(b[e]-b[s-1],end=' ')
    print(c[e]-c[s-1],end=' ')
    print()