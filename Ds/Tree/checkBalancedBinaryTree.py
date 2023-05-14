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


#Checkin for balance binary tree
#Balance Binary tree for every node the difference bw left subtree and 
# right subtree should be less than equal to one
def isBalanced(root):
    if root is None: return [True,0]

    left,right=isBalanced(root.left),isBalanced(root.right)
    balance=(left[0] and right[0] and abs(left[1]-right[1])<=1)
    # basically this line means
    # left[0]and right[0]should return true
    # and height of left at 1 position should be balance as height start from 1
    return [balance,1 +max(left[1],right[1])] 
    #it wwill return balance position and height from 1 