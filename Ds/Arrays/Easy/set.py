

def optimal(arr1,arr2):
    m=len(arr1)
    n=len(arr2)
    i=j=0
    arr=[]
    while i<m and j<n:
        if arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr1[1]:
            j+=1
        else:
            arr.append(arr1[i])
            i+=1
            j+=1
    print(arr)


if __name__=='__main__':
        
    arr1=[1,2,3,4,5,6,7,8,9,23]
    arr2=[4,5,6,7,8,9,23]
    optimal(arr1,arr2)