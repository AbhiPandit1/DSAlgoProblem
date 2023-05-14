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


def MaxD(root):
    if root==None:
        print(0)
    lh=MaxD(root.left)
    rh=MaxD(root.right)

    print(1+max(lh,rh))

MaxD(a)

def DepthM(self,root):
    if root==None:
        return 0
    lh=DepthM(root.left)
    rh= DepthM(root.right)
    return 1 +max(lh,rh)

DepthM(a)