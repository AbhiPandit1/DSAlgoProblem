#BFS for unidirected graph where we have given source vertex
#we want to print every vertex once so once something is printed we dont want to print it again
def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def printGraph(adj):
    for l in adj:
        print(l)

def BFS(adj,s):
    visited=False*len(adj)
    q=[]
    q.append(s)
    visited[s]=True
    while q:
        s=q.pop(0)
        print(s,end=" ")
        for u in adj[s]:
            if visited[u]==False:
                q.append(u)
                visited[u]==True





if __name__=="__main__":
    v=7
    adj=[[] for i in range(v)] #[[][][][]] list of list v empty list
    addEdge(adj,0,1)# [[1][0][][]] it an undirected graph it add a list form 0 to 1 as well as 1 to 0
    addEdge(adj,0,2)#[[1,2][][0][]]
    addEdge(adj,0,5)#[[1,2][1,2][0,1][]]
    addEdge(adj,1,3)
    addEdge(adj,2,4)
    addEdge(adj,4,5)
    addEdge(adj,3,5)
    
    printGraph(adj)
    BFS(adj,1)
