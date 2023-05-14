def sort(arr):
    if len(arr)<=1:
        return 

    mid=len(arr)//2

    left=arr[:mid]
    right=arr[mid:]

    sort(left)
    sort(right)

    merge_sort(left,right,arr)

    
    








def merge_sort(a,b,arr):
    m=len(a)
    n=len(b)
    
    k=i=j=0

    while i<m and j<n:
        if a[i]<b[j]:
            arr[k]=a[i]
            i=i+1
            
        else:
            arr[k]=b[j]
            j=j+1
        k+=1
    while i<m:
        arr[k]=a[i]
        i+=1
        k+=1
    while j<n:
        arr[k]=b[j]
        j+=1
        k+=1
    
    return arr
if __name__=='__main__':
    test_cases=[
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
    [2,3,1,3]
    ,[-1,3,45]]
   
    for arr in test_cases:
        sort(arr)
        print(arr)

    
