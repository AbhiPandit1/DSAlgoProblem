# 0 -1 2
# 1 -0 2 3
# 2 - 0 1
# 3- 1
#Representing it in python list
# Vertices=4
#in python term[[1,2][0,2,3][0,1][1]]

#In list we have many benefit as we can represent in Q(v+e) space and for matric it is Q(v^2)
#
#
#
def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def printGraph(adj):
    for l in adj:
        print(l)

if __name__=="__main__":
    v=4
    adj=[[] for i in range(v)] #[[][][][]] list of list v empty list
    addEdge(adj,0,1)# [[1][0][][]] it an undirected graph it add a list form 0 to 1 as well as 1 to 0
    addEdge(adj,0,2)#[[1,2][][0][]]
    addEdge(adj,1,2)#[[1,2][1,2][0,1][]]
    addEdge(adj,1,3)#[[1,2][0,2,3][0,1][1]]
    printGraph(adj)
