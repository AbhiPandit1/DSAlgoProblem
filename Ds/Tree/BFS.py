class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
a =  Node("A")
b =  Node("B")
c =  Node("C")    
d =  Node("D")
e =  Node("E")
f =  Node("F")
g =  Node("G")
h =  Node("H")
#           A     <--Start from here
#          / \ 
#         B   C
#        / \   \
#       D   E   F
#      /
#     G
#    /
#   H
a.left=b
a.right=c
b.left=d
b.right=e
c.right=f
d.right=g
d.left=h
h.right=e




def BFS(root):
    if root==None:
        return []
    queue=[root]
    result=[]
    lh=[]
    rh=[]
    while queue:
        current=queue.pop(0)
        result.append(current.val)
       
        if current.left:
            queue.append(current.left)
            lh.append(current.left.val)

        if current.right:
            queue.append(current.right)
            rh.append(current.right.val)
    print(result,len(lh),lh,len(rh),rh)
    height=max(len(lh),len(rh))+1
    print(height)

BFS(a)

