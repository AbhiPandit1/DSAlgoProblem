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

def Bfs(root):
    q=[root]
    result=[]

    while q:
        curr=q.pop(0)
        
        result.append(curr.val)
        

        if curr.left:
            q.append(curr.left)
            
            
        if curr.right:
            q.append(curr.right)
    print(result)      
Bfs(a)


def Dfs(root):
    stack=[root]
    result1=[]
    while stack:
        curr=stack.pop()
        result1.append(curr.val)
        
        if curr.right:
          stack.append(curr.right)
        if curr.left:
          stack.append(curr.left)
        
    print(result1)
Dfs(a)

def DfsRecursive(root):
    
    if root is None:
        return
    print(root.val)
    DfsRecursive(root.left)
    DfsRecursive(root.right)
    
DfsRecursive(a)

def Inorder(root):
    if root is None:
        return 
    Inorder(root.left)
    print(root.val)
    Inorder(root.right)

Inorder(a)


def Postorder(root):
    if root is None:
        return 
    Postorder(root.left)
    Postorder(root.right)
    print(root.val)

Postorder(a)


    
def Preorder(root):
    if root is None:
        return 
    print(root.val)
    Preorder(root.left)
    Preorder(root.right)
    

Preorder(a)



