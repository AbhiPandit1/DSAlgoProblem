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



def Invert(root):
    if root is None: return None

    temp=root.left
    root.left=root.right
    root.right=temp

    Invert(root.left)
    Invert(root.right)
    return root
