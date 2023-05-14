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

def dfs(node,currSum,target):
    if not node: return False

    currSum+=node.val
    if not node.left and not node.right :
        return currSum == target
    
    return dfs(node.left,currSum,target) or dfs(node.right,currSum,target)

