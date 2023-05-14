from collections import deque
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


def maxDepth(root):

    queue=[root]
    leftH=[]
    rightH=[]
    
    while queue:
        queue.pop(0)
        if root.left:
            leftH.append(root.left.val)
            queue.append(root.left)
        
        if root.right:
            rightH.append(root.right.val)
            queue.append(root.right)
    print(leftH,rightH)
maxDepth(a)


    
    
