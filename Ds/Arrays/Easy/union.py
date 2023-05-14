

def union(arr1,arr2):

    arr=[]
    m=len(arr1)
    n=len(arr2)
    print(m,n)
    i=0
    j=0
    d={}
    while i<m and j<n:
        if arr1[i]<arr2[j]:
            arr.append(arr1[i])
            i+=1
        
        elif arr2[j]<arr1[i]:
            arr.append(arr2[j])
            print(arr)
            j=j+1
        else:
            arr.append(arr1[i])
            j=j+1
            i=i+1
            
    while i<m:
        arr.append(arr1[i])
        i=i+1
    while j<n:
        arr.append(arr2[j])
        j=j+1
    for i in range(len(arr)):
        d[arr[i]]=i
    
    print(arr)
    
    
   





"""

def baoln(arr1,arr2):
    
    
    
    map={}
    for i in range(len(arr1)):
       map[arr1[i]]=i

    arr=map.keys()
    
    for i in range(len(arr2)):
        map[arr2[i]]=i
    
    arr=map.keys()

    print(arr)

      
    """
 



if __name__=='__main__':
    arr1=[2,3,4,5,7,6,8,8,8]
    arr2=[3,4,11,12,5,6]

    arr1.sort()
    arr2.sort()
   
    union(arr1,arr2)
    

