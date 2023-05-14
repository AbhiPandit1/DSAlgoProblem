#count the unique path from top left to the bottom right
#A single path may only move along 0's and cant visit the same cell more than once
# it is example of backtracking

#count path (backtracking)
def dfs(grid,r,c,visit):
    ROWS,COLS=len(grid),len(grid[0])#it will give no of rows and columns
    if(min(r,c)<0 or r==ROWS and c==COLS or#min(r,c)<0 means rows or coulmn can go ou of bound
    (r,c) in visit or grid[r][c] ==1):#r==rows and c==cols is also not appicabe as we have no of rows and colums are equal to 3 whereas it can go upto 4 so that why its equal is out of bound
      return 0
    if r==ROWS-1 and c==COLS-1:
        return 1

    visit.add((r,c))
    count=0
    count+=dfs(grid,r+1,c,visit)
    count+=dfs(grid,r-1,c,visit)
    count+=dfs(grid,r,c+1,visit)
    count+=dfs(grid,r,c-1,visit)

    visit.remove((r,c))
    return count
#Time complexity --->q(4^m+n)

if __name__=="__main__":
          #c
    grid=[[0,0,0,0],#<--r
          [1,1,0,0],
          [0,0,1,1],
          [0,1,0,0]]
    print(dfs(grid,0,0,set()))