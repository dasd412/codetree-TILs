class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

n=int(input())

nodes=[Node(i+1) for i in range(n)]

q=int(input())

def insert_next(target,node):
    node.prev=target
    node.next=target.next

    if node.prev is not None:
        node.prev.next=node
    if node.next is not None:
        node.next.prev=node

def insert_prev(target,node):
    node.next=target
    node.prev=target.prev
    if node.prev is not None:
        node.prev.next=node
    if node.next is not None:
        node.next.prev=node

def pop(node):
    if node.prev is not None:
        node.prev.next=node.next
    if node.next is not None:
        node.next.prev=node.prev

    node.prev=None
    node.next=None

for i in range(q):
    op=list(input().split(' '))

    # pop
    if op[0]=='1':
        pop(nodes[int(op[1])-1])
    # insert_prev
    elif op[0]=='2':
        insert_prev(nodes[int(op[1])-1],nodes[int(op[2])-1])
    # insert_next
    elif op[0]=='3':
        insert_next(nodes[int(op[1])-1],nodes[int(op[2])-1])
    elif op[0]=='4':
        node=int(op[1])-1

        if nodes[node].prev is not None:
            print(nodes[node].prev.data,end=' ')
        else:
            print('0',end=' ')
        
        if nodes[node].next is not None:
            print(nodes[node].next.data,end=' ')
        else:
            print('0',end=' ')
        print()

for i in range(n):
    if nodes[i].next is not None:
        print(nodes[i].next.data,end=' ')
    else:
        print('0',end=' ')