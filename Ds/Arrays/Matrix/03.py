


def sorted(arr,c,r):
   
    for i in range(len(arr)):
        
        for j in range(len(arr[0])):
            if arr[i][j]==0:
                c[i]=1
                r[j]=1
                
    
    for i in range(len(c)):
        for j in range(len(r)):
            if c[i] or c[j]==1:
                arr[i][j]==0
    

    return arr


if __name__=="__main__":

    arr=[[1,0,1],[1,1,1],[0,1,1]]
    c=[]
    r=[]
    sorted(arr,c,r)