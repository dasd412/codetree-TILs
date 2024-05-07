class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

def insert_next(target,node):
    node.prev=target
    node.next=target.next

    if node.next is not None:
        node.next.prev=node
    if node.prev is not None:
        node.prev.next=node

def insert_prev(target,node):
    node.next=target
    node.prev=target.prev

    if node.prev is not None:
        node.prev.next=node
    
    if node.next is not None:
        node.next.prev=node


s_init=input()

current=Node(s_init)

n=int(input())

for i in range(n):
    op=list(input().split(' '))
    if op[0]=='1':
        node=Node(op[1])
        insert_prev(current,node)
    elif op[0]=='2':
        node=Node(op[1])
        insert_next(current,node)
    elif op[0]=='3':
        if current.prev is not None:
            current=current.prev
    elif op[0]=='4':
        if current.next is not None:
            current=current.next

    if current.prev is not None:
        print(current.prev.data,end=' ')
    else:
        print('(Null)',end=' ')

    print(current.data,end=' ')

    if current.next is not None:
        print(current.next.data,end=' ')
    else:
        print('(Null)',end=' ')
    print()