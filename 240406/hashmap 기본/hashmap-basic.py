import sys
from collections import defaultdict

n=int(sys.stdin.readline().rstrip())

answer=[]

hash_map=defaultdict(int)

for i in range(n):
    s=list(sys.stdin.readline().split(' '))
    if s[0]=='add':
        hash_map[int(s[1])]=int(s[2])
    elif s[0]=='remove':
        hash_map.pop(int(s[1]))
    elif s[0]=='find':
        if int(s[1]) in hash_map:
            answer.append(hash_map[int(s[1])])
        else:
            answer.append('None')

for elem in answer:
    print(elem)