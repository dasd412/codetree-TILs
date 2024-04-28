from sortedcontainers import SortedSet

n,t=list(map(int, input().split()))

# (위치, 속력)
people=SortedSet()

# (바로 앞 사람과 마주치는 데 걸리는 시간, 현재 위치, 속력)
event=SortedSet()

positions=[]
speeds=[]

for i in range(n):
    start,speed=list(map(int, input().split()))
    positions.append(start)
    speeds.append(speed)

    people.add((start,speed))

# (pos1,speed1) 앞에 있는 (pos2,speed2) 사람과 마주치는 데 걸리는 시간을 사건 형태로 추적함.

# 사건 정보 추가하기
def add_event(pos1,speed1,pos2,speed2):
    # 만약 바로 뒷사람 속력이 더 크거나 같다면 앞지를 수 없다.
    if speed1<=speed2:
        return

    # (바로 앞 사람과 마주치는 데 걸리는 시간, 현재 위치, 속력)
    event.add((1.0*(pos2-pos1)/(speed1-speed2),pos1,speed1))

# 사건 정보 제거하기
def remove_event(pos1,speed1,pos2,speed2):
    if speed1<=speed2:
        return
    
    event.remove((1.0*(pos2-pos1)/(speed1-speed2),pos1,speed1))

# 초기화. 바로 앞사람과 마주칠 수 있는지 먼저 추적.
for i in range(n-1):
    add_event(positions[i],speeds[i],positions[i+1],speeds[i+1])

# 앞지른 사건이 남아있을 때까지 지속한다.
while event:
    
    # 현재 가장 빨리 마주친 사건을 찾아낸다.
    time,pos,sp=event[0]

    # 이미 t분을 넘어서면 종료
    if time>t:
        break

    # 마주친 사람 제거
    people.remove((pos,sp))
    # 마주친 사람의 사건 제거
    event.remove((time,pos,sp))

    # 바로 앞 사람 찾아내기
    index=people.bisect_right((pos,sp))
    next_pos,next_sp=people[index]

    # 마주친 사람 이전 사람 찾아내기
    if index!=0:
        index-=1
        prev_pos,prev_sp=people[index]

        # 이전 사람과 마주친 사람의 사건을 제거하고
        remove_event(prev_pos,prev_sp,pos,sp)

        # 이전 사람과 바로 앞 사람을 마주친 사건으로 만듬.
        add_event(prev_pos,prev_sp,next_pos,next_sp)
    
print(len(people))