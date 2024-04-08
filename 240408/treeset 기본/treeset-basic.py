from sortedcontainers import SortedSet

ss=SortedSet()

n=int(input())

for i in range(n):
    string = list(input().split())
    if string[0]=='add':
        ss.add(int(string[1]))
    elif string[0]=='remove':
        ss.remove(int(string[1]))
    elif string[0]=='find':
        if int(string[1]) in ss:
            print('true')
        else:
            print('false')
    elif string[0]=='lower_bound':
        index=ss.bisect_left(int(string[1]))

        if index>=len(ss):
            print('None')
        else:
            print(ss[index])

    elif string[0]=='upper_bound':
        index=ss.bisect_right(int(string[1]))

        if index>=len(ss):
            print('None')
        else:
            print(ss[index])

    elif string[0]=='largest':
        if len(ss):
            print(ss[-1])
        else:
            print('None')

    elif string[0]=='smallest':
        if len(ss):
            print(ss[0])
        else:
            print('None')