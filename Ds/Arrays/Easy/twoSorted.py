

def sorted(arr,target):
    n=len(arr)-1
    d={}
    c=0
    for i in range(len(arr)):
        if arr[i]<0:
            c+=1
            
    if c//2==0:
        comp=target-arr[i]
        if comp in d:
            print(d[comp],d[i])
        else:
            d[arr[i]]=i
    else:
        comp=target+arr[i]
        if comp in d:
            print(d[comp],d[i])
        else:
            d[arr[i]]=i
            print(d)
    

    




if __name__=='__main__':
    arr=[-1,2,3,5,-1]
    sorted(arr,8)
