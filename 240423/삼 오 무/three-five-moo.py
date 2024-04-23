import math
n=int(input())

"""
19는 11번째 수이다. 이는 19-6-3+1=11인데, 6은 19까지의 3의 배수이고 3은 19까지의 5의 배수
1은 19까지의 15의 배수다.

일반화하면, 수를 x라 할때 
수의 번호 n은 x-(x까지의 3의 배수 개수)-(x까지의 5의 배수 개수)+(x까지의 15의 배수 개수)이므로
x가 커질수록 n도 커진다. => 단조 증가
"""

def get_count(number:int)->int:
    count=number
    count-=(number//3)
    count-=(number//5)
    count+=(number//15)
    return count

left=1

right=int(math.pow(10,30))

while left<=right:
    mid=(left+right)//2

    count=get_count(mid)

    if count>=n:
        if count==n and mid%3!=0 and mid%5!=0:
            print(mid)
            break
        right=mid-1
    else:
        left=mid+1