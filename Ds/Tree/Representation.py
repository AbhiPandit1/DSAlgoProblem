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



    
    
def DFS(root):
    if root==None:
        return[]

    result=[]
    stack=[root]


    while len(stack)>0:
        current=stack.pop()
        result.append(current.val)
            
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    print(result)
#Recursive 
def UsingRecursion(root):
    if root==None:
        return[] 
    UsingRecursion(root.left)
    UsingRecursion(root.right)
    return[root.val]


UsingRecursion(a)


        


















