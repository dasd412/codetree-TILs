n,m = list(map(int, input().split()))

arr=[]

for i in range(m):
    a,b=list(map(int, input().split()))
    arr.append((a,b))

arr.sort()

start=1
end=arr[-1][1]-arr[0][0]

"""
[0,10]에서 가장 가까운 두점의 거리의 최댓값을 x, 만들 수 있는 점의 개수를 y라하자. 
x   y
10  2개
9   2개 
8   2개 
7   2개 
6   2개 
5   3개 
4   3개 
3   4개 
2   6개
1  11개

x와 y는 단조 감소 형태를 띄기때문에 파라메트릭 서치를 활용한다.
"""

# 가장 가까운 거리 distance일 때 만들 수 있는 점의 개수 리턴
def get_count(distance:int)->int:
    count=0

    for a,b in arr:
        count+=1
        count+=(b-a)//distance

    return count

answer=0


while start<=end:
    mid=(start+end)//2
    
    # n개보다 부족하게 만들어진다면, 길이를 줄인다.
    count=get_count(mid)

    if count<n:
        end=mid-1
    else:
        if count==n:
            answer=max(answer,mid)
        start=mid+1

print(answer)