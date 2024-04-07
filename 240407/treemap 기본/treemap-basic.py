from sortedcontainers import SortedDict

sd=SortedDict()

n=int(input())

for i in range(n):
    s=list(input().split())
    if s[0]=='add':
        sd[int(s[1])]=int(s[2])
    elif s[0]=='remove':
        sd.pop(int(s[1]))
    elif s[0]=='find':
        if int(s[1]) in sd:
            print(sd[int(s[1])])
        else:
            print('None')
    elif s[0]=='print_list':
        if len(sd):
            for key,value in sd.items():
                print(value,end=' ')
            print()
        else:
            print('None')