class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
a =  Node("1")
b =  Node("2")
c =  Node("3")    
d =  Node("4")
e =  Node("5")
f =  Node("6")
g =  Node("7")
h =  Node("8")
i =  Node("9")
#           1     <--Start from here
#          / \ 
#         2   3
#        / \   \
#       4  5     6
#      /\         \
#     8  9          7 
#  

a.left=b
a.right=c
b.left=d
b.right=e
c.right=f
f.right=g
d.left=h
d.right=i


def maxValue(root):
    if root is None:
        return -999999
    else:
        lh=maxValue(root.left)
        rh=maxValue(root.right)
        print(max(root.val,lh,rh))