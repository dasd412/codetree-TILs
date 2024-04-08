n=int(input())

hash_set=set()

for i in range(n):
    s=list(input().split())

    if s[0]=='add':
        hash_set.add(int(s[1]))
    elif s[0]=='remove':
        hash_set.remove(int(s[1]))
    elif s[0]=='find':
        if int(s[1]) in hash_set:
            print('true')
        else:
            print('false')