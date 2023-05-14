

def convert(a):
   
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]==0:
                
                markrow(i)
                markrow(j)

    again(a)           
    print(a)


def markrow(i):
   for k in range(len(a)):
    if a[i][k]!=0:
        a[i][k]=-1


def markrow(j):
   for i in range(len(a)):
    if a[i][j]!=0:
        a[i][j]=-1
def again(a):

    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]==-1:
                a[i][j]=0
                
           

if __name__=='__main__':
    a=[[1,0,1],[0,1,1],[1,1,1]]

    convert(a)
