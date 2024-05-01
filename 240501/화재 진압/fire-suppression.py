import sys
n,m = list(map(int, input().split()))
fire = list(map(int, input().split()))
station = list(map(int, input().split()))

fire.sort()
station.sort()
"""
정렬하고 나서 화재 위치를 i, 가장 가까운 소방서 위치를 j라 하자.
화재 위치 i가 증가할수록 가장 가까운 소방서 위치 j 역시 증가하는 단조 증가 관계이다. 따라서 투포인터를 활용한다.
"""

answer=0

j=0
for i in range(n):

    # 화재 위치 i에서 가장 가까운 소방서 위치를 찾는다.
    while j+1<m:
        
        dist_current=abs(fire[i]-station[j])
        dist_next=abs(station[j+1]-fire[i])

        # 현재 위치보다 다음 위치가 더 가깝다면, 더 가까운 쪽으로 소방서 위치를 옮긴다.
        if dist_current>dist_next:
            j+=1
        # 다음 위치보다 현재 위치가 가깝다면 소방서 찾기 종료.
        else:
            break
            
    answer=max(answer,abs(fire[i]-station[j]))
    
print(answer)