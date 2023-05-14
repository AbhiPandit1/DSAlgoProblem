"""
def linear(arr,target):
    n=len(arr)
    for i in range(n):
        if arr[i]==target:
            return i
        
   """              
                              
 


        

""""" 
def practice(arr):
    n=len(arr)
    print(n)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
                
    

    return arr

"""
"""
def linearSearch(arr):
    i=0
    j=len(arr)-1
    if arr(len)<1:
        return -1
    else:
        while i<len(arr) and i<j:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i+=1
            j-=1

        
       
        
        return arr


if __name__=='__main__':

   arr=[2 ]

   print(linearSearch(arr))
   """
   

    

    