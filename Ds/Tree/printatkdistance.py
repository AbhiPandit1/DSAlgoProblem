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
root=a


def printk(root,k):
    if root is None:
        return
    if k==0:
        return root.val
    printk(root.left,k-1)
    printk(root.right,k-1)
