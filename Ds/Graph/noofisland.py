
def island(grid):
    if not grid:
        return 0
    rows,cols=len(grid),len(grid[0])
    visited=set()
    island=0
    
    def bfs(r,c):
        q=[]
        visited.add((r,c))
        print(visited)
        q.append((r,c))

        while q:
            row,col=q.pop(0)
            direction=[[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in direction:
                
                if ((r+dr) in range(rows) and 
                (c+dc) in range(cols) and
                grid[r+dr][c+dc]=="1" and
                (r+dr, c+dc) not in visited):
                  q.append((r+dr,c+dc))
                  visited.a(r+dr,c+dc)
    
    
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=="1" and (r,c) not in visited:
                bfs(r,c)
                island+=1








if __name__=="__main__":
  grid1= [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

island(grid1)
island(grid2)