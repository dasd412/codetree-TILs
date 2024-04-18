n,m= list(map(int, input().split()))

arr=[['']* m for _ in range(2*n)]

for i in range(2*n):
    split=list(input())
    for j in range(m):
        arr[i][j]=split[j]

#O(2N)
def get_combination(i:int,j:int,k:int)->bool:
    A=set()
    B=set()

    for x in range(n):
        A.add(arr[x][i]+arr[x][j]+arr[x][k])
    for x in range(n,2*n):
        B.add(arr[x][i]+arr[x][j]+arr[x][k])

    # 교집합이 있는지 확인해서 없다면, 완벽하게 구분할 수 있는 그룹이다.
    if len(A&B):
        return False
    else:
        return True

answer=0

# O(m^3)* O(2n)이지만 m이 50, n이 500이므로 충분함.
for i in range(m):
    for j in range(i+1,m):
        for k in range(j+1,m):
            if get_combination(i,j,k):
                answer+=1

print(answer)