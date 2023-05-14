#Good nodes in binary tree
# A good node is define if in a path there is no value larger than it

#                    3
#                   / \
#                  1   4
#                 /   / \
#                3   1   5
# in this 5 is a good node as in path you caen 4 and 3 is smaller than thise
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
a =  Node("3")
b =  Node("1")
c =  Node("3")    
d =  Node("4")
e =  Node("5")
f =  Node("1")
#           A     <--Start from here
#          / \ 
#         B   C
#        / \   \
#       D   E   F

a.left=b
a.right=d
b.left=c
d.right=e
d.left=f



#for counting no of good value in subtree we will go in left direction and check greatest value
# 
#
#
#

def dfs(root,maxVal):
    if root is None:
        return 0
    root.val=max(maxVal,root.val)
    res=0
    if root.val>=maxVal:
        res+=1
    else:0
    dfs(root.left,maxVal)
    dfs(root.right,maxVal)


