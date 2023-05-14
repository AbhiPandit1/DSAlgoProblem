def Binary(arr,l,r,target):
    n=len(arr)
    if n is None:
        return 0

    mid=(l+r)//2

    if target==mid:
        return mid
    

    if target<mid:
        Binary(arr,l,mid-1,target)
    if target >mid:
        Binary(arr,l+1,mid+1,target)

if __name__=="__main__":
    arr=[2,3,4,5,6,7,8,9,10,11]
    n=len(arr)
    Binary(arr,0,n-1,5)