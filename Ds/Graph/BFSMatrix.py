#Find the length of the shortest path from the top left of the grid
#to thr bottom right
#BFs is quite efficient


def Bfs(grid):
    Rows,Cols=len(grid),len(grid[0])
    visit=set()
    queue=[]
    queue.append((0,0))
    visit.add((0,0))

    length=0
    while queue:
        for i in range(len(queue)):
            print(queue)
            r,c=queue.pop(0)
            if r==Rows-1 and c==Cols-1:
                print(length)
            neighbors=[[0,1],[0,-1],[1,0],[-1,0]]
            for dr,dc in neighbors:
                if(min(r+dc,c+dr))<0 or r+dr ==Rows or c+dc==Cols or(r+dr,c+dc) in visit :
                    continue
                queue.append((r+dr,c+dc))
                visit.add((r+dr,c+dc))
        length+=1
       




if __name__=="__main__":
          #c
    grid=[[1,12,11,10],#<--r
          [2,13,16,9],
          [3,14,15,8],
          [4,5,6,7]]
    print(Bfs(grid))