class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
a =  Node(2)
b =  Node(3)
c =  Node(3)    
d =  Node(4)
e =  Node(5)
f =  Node(6)
#           A     <--Start from here
#          / \ 
#         B   C
#        / \   \
#       D   E   F

a.left=b
a.right=c
b.left=d
b.right=e
c.right=f

def sum(root,target):
    stack=[root]
    sum=0
    while stack:
        curr=stack.pop()
        sum=sum+curr.val
        
        if sum==target:
            break
        print(True)

        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    print(sum)
   
sum(a,11)





