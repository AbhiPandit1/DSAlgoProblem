


def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def printGraph(adj):
    for v in range(len(adj)):
        print(v,  adj[v])
        
# in dfs we can pick any adjacent first 
def DFSRec(adj,s,visited):
    visited[s]=True
    print(s,end=" ")
    for u in adj[s]:
        if visited[u]==False:
            DFSRec(adj,u,visited)
def DFS(adj,s):
    visited=False*len(adj)
    DFSRec(adj,s,visited)




if __name__=="__main__":
    v=7
    adj=[[] for i in range(v)] #[[][][][]] list of list v empty list
    addEdge(adj,0,1)# [[1][0][][]] it an undirected graph it add a list form 0 to 1 as well as 1 to 0
    addEdge(adj,0,4)#[[1,2][][0][]]
    addEdge(adj,1,2)#[[1,2][1,2][0,1][]]
    addEdge(adj,2,3)
    addEdge(adj,4,5)
    addEdge(adj,4,6)
    addEdge(adj,5,6)
    
    printGraph(adj)


    
