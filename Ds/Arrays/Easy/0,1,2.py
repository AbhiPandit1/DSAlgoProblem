

"""
def sort(arr):
    arr.sort()
    print(arr)

"""
"""
def better(arr):
    c0=0
    c1=0
    c2=0
    for i in range(len(arr)):
        if arr[i]==0:
            c0=c0+1
        elif arr[i]==1:
             c1=c1+1
        else: 
             c2+=1
    print(c0,c1,c2)
    
    for i in range(c0):
       arr[i]=0
    for i in range(c0,c0+c1):
        arr[i]=1
    for i in range(c0+c1,len(arr)):
        arr[i]=2
    print(arr)
"""


if __name__=='__main__':
    arr=[0,2,1,1,0,2,0,1,0]
    better(arr)
