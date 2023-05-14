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


def target(root,target):
    if root==None:
        return -1
    queue=[root]
    while len(queue)>0:
        current=queue.pop(0)
        if current.val==target:
            print(current.val)
            print(True)
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
                
    
         

target(a,"A")

def Recursive(root,target):
    if root==None:
        return False
    if root.val==target:
        return True
    return Recursive(root.left,target) or Recursive(root.right,target)
Recursive(a,c)

